# Attitude-Control-of-a-Cubesat-Satellite-with-Reaction-Wheels-CAD-track-
Designing a 3U cubesat satellite with at least 3 mutually perpendicular reaction wheels for attitude control, wheel mounting brackets, motor housing and structural supports. Ensure the design is dimensionally consistent and physically plausible.

<ins>The decision to use a 3U form factor</ins>
| Parameter         | 1U        | 2U       | 3U        |
| ----------------- | --------- | -------- | --------- |
| Volume            | Small     | Medium   | Large     |
| Wheel Integration | Difficult | Moderate | Easy      |
| CAD Complexity    | Easy      | Medium   | Medium    |
| Realism           | Moderate  | Good     | Excellent |

The 1U form factor faces a volume crisis, allowing no room for a payload.
The 2U form factor does allow space for a small payload but the asymmetric physics due to the centre of mass lying between the 2 1U units make it an unfavourable choice. Moreover, the 2U form factor is much less common in the industry so it is hard to find references.
The 3U form factor ultimately wins out as the segments can be divided cleanly(payload, ADCS, avionics), and it solves the centre of mass and volume issues. The larger surface area also allows for massive power generation from solar panels. 
The 3U CubeSat has become the industry standard for commercial applications, offering the optimal balance between payload capacity, power generation, and cost-effectiveness. Companies like Planet Labs operate entire Earth observation constellations using 3U Dove satellites, while 6U and 12U platforms enable more sophisticated missions including deep space exploration and advanced propulsion systems.

<ins>The Subsystems</ins>


| Component                 | What to Include (High Detail)                                                                                                                            | What to Simplify / Skip (Low Detail)                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Chassis / Frame**       | Continuous 8.5 mm corner rails, external face plates, specific cutouts/holes for the camera lens, and structural assembly bolts.                         | trusses on the sides for lightweight support.                               |
| **Reaction Wheels**       | The precise shape of the flywheel discs (maximize rim mass for higher inertia), the motor shafts, and the orthogonal mounting bracket.                   | no internal motor copper wiring and individual ball bearings.                                   |
| **Payload Camera**        | A realistic multi-lens cylinder assembly, a hollow baffle tube, and a back-end sensor housing board.                                                     | Glass lens placeholder insdie.                        |
| **Electronics (OBC/EPS)** | Simple rectangular plates (PCBs) representing each board, featuring standard PC104 stack-through connectors (the blocky pins connecting stacked boards). |not individual resistors, chips, or capacitors.  |
| **Batteries**             | A clustered pack of cylindrical cells (modeled as simple smooth cylinders, e.g., standard 18650 size dimensions) enclosed in a securing clip.            | no wiring leads and individual solder tabs.                                                     |
| **Solar Panels**          | Thin external PCB sheets bolted to the frame faces, with shallow extruded rectangular shapes (~0.3 mm thick) representing the solar cells.               | Skip the micro-wires connecting the cells together.                                               |

The rails must be the longest part of the body, therefore a standoff offset of 2mm on either side is taken.
As stated in the Cal Poly blueprint, I have followed the standoff contact detail, and the max allowable protrusion on the faces is the rail width.

References:
International Journal of Aerospace
hexstaruniverse.com
nanoavionics.com
