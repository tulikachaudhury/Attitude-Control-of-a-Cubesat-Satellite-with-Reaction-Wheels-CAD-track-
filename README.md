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



<ins>The Design Process</ins>
The Chassis
The rails must be the longest part of the body, therefore a standoff offset of 2mm on either side is taken.
As stated in the Cal Poly blueprint, I have followed the standoff contact detail by using chamfer, and the max allowable protrusion on the faces is the rail width. Trusses between the rails ensure a lightweight and sturdy design, and fillets were added to the outer edges to ensure that sharp corners do not cause damage. Aluminium 6061 was my material of choice for the chassis

ACDS Design
Motor : EC22 Flat L High Torque
Reaction Wheel Diameter: 38m
Reaction Wheel Thickness: 10mm


References:
International Journal of Aerospace
hexstaruniverse.com
nanoavionics.com
