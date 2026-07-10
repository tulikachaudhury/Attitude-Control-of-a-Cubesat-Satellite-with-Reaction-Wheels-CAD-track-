"""
disturbance_models.py
=====================

Environmental disturbance torques for the ADCS simulation. This is a NEW
module — no existing core module (kinematics, dynamics, wheels, RK4) is
touched. Each model is a pure function: (state, parameters) -> body-frame
torque [N m]. simulate.py sums the enabled models into the tau_ext that
AttitudeSimulator already accepts.

Models
------
1. Gravity gradient
   Earth's gravity is slightly stronger on the near side of the satellite
   than the far side. For a rigid body in a circular orbit with mean motion
   n, the resulting torque about the CoM is

        tau_gg = 3 n^2  o_hat x (J o_hat)

   where o_hat is the NADIR unit vector (satellite -> Earth centre)
   expressed in the BODY frame: o_hat = R(q)^T @ nadir_inertial.
   Properties worth showing in the report:
     - vanishes when a principal axis points at nadir (o_hat x J o_hat = 0),
     - worst-case magnitude (3/2) n^2 |I_max - I_min|  (~2e-8 N m for our 3U).

2. Aerodynamic drag
   Residual atmosphere at 500 km produces a force
        F = 1/2 rho v^2 Cd A      (opposing the velocity direction)
   applied at the centre of pressure. If the CP is offset from the CoM by
   r_cp (body frame), the torque is
        tau_aero = r_cp x F_body,   F_body = R(q)^T @ F_inertial.
   rho at 500 km is ~1e-13..1e-12 kg/m^3 depending on solar activity, so it
   is a config parameter, not a constant.

3. Constant torque
   Passed straight through from the config (already existed) — kept here so
   all disturbance handling lives in one place.

References: Wertz (ed.), Spacecraft Attitude Determination and Control,
Ch. 17 (environmental torques); Markley & Crassidis Sec. 3.3.
"""

from __future__ import annotations
import numpy as np

from QuaternionLibrary import Quaternion


def gravity_gradient_torque(q_array, inertia_tensor, mean_motion,
                            nadir_inertial=(0.0, 0.0, -1.0)):
    """Body-frame gravity-gradient torque [N m].

    q_array         : current attitude quaternion (w, x, y, z), body->inertial
    inertia_tensor  : (3,3) CoM-referenced inertia [kg m^2]
    mean_motion     : orbital mean motion n [rad/s]
    nadir_inertial  : unit vector from satellite toward Earth centre,
                      inertial frame (fixed-direction simplification —
                      document it; the full model would rotate this with
                      the orbit).
    """
    R = Quaternion(*q_array).to_rotation_matrix()          # body -> inertial
    o_hat = R.T @ np.asarray(nadir_inertial, dtype=np.float64)
    o_hat = o_hat / np.linalg.norm(o_hat)
    J = np.asarray(inertia_tensor, dtype=np.float64)
    return 3.0 * mean_motion**2 * np.cross(o_hat, J @ o_hat)


def aero_drag_torque(q_array, rho, speed, Cd, area, r_cp,
                     flow_dir_inertial=(1.0, 0.0, 0.0)):
    """Body-frame aerodynamic torque [N m].

    rho   : atmospheric density [kg/m^3]      (~5e-13 typical at 500 km)
    speed : orbital speed [m/s]               (7613 for our 500 km orbit)
    Cd    : drag coefficient                  (2.2 is the standard assumption)
    area  : reference (projected) area [m^2]  (0.034 = 0.1 x 0.34 long face)
    r_cp  : centre-of-pressure offset from CoM, body frame [m]
    flow_dir_inertial : unit vector of the satellite's velocity, inertial
                        frame. Drag force opposes it.
    """
    v_hat = np.asarray(flow_dir_inertial, dtype=np.float64)
    v_hat = v_hat / np.linalg.norm(v_hat)
    F_inertial = -0.5 * rho * speed**2 * Cd * area * v_hat   # opposes motion
    R = Quaternion(*q_array).to_rotation_matrix()
    F_body = R.T @ F_inertial
    return np.cross(np.asarray(r_cp, dtype=np.float64), F_body)


def build_tau_ext_func(dist_cfg, inertia_tensor):
    """Assemble a tau_ext_func(t, q, omega) for AttitudeSimulator.run() from
    a DisturbanceConfig. Returns None when nothing is enabled, matching the
    simulator's existing default."""
    terms = []

    if dist_cfg.enabled and np.any(dist_cfg.constant_torque):
        tau_c = np.asarray(dist_cfg.constant_torque, dtype=np.float64)
        terms.append(lambda t, q, om: tau_c)

    gg = getattr(dist_cfg, "gravity_gradient", None)
    if gg is not None and gg.enabled:
        terms.append(lambda t, q, om: gravity_gradient_torque(
            q, inertia_tensor, gg.mean_motion, gg.nadir_inertial))

    aero = getattr(dist_cfg, "aero", None)
    if aero is not None and aero.enabled:
        terms.append(lambda t, q, om: aero_drag_torque(
            q, aero.rho, aero.speed, aero.Cd, aero.area,
            aero.r_cp, aero.flow_dir_inertial))

    if not terms:
        return None
    return lambda t, q, om: sum(f(t, q, om) for f in terms)
