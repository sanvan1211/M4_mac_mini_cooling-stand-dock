# M4 Mac Mini Cooling Stand / Dock
 
An elevated cooling stand for the Apple M4 Mac mini, designed from scratch in Onshape. It lifts the mini off the desk, mounts a 120mm fan underneath that blows cool air up into the mini's bottom intake, and adds RGB underglow — powered over USB with a single on/off switch.
 
My first CAD project, built through [Hack Club Stardance](https://stardance.hackclub.com/home) to learn mechanical CAD. 
 
> **Status:** Design complete. ready to ship

> <img width="780" height="662" alt="Screenshot 2026-07-17 at 11 40 56" src="https://github.com/user-attachments/assets/da7d0dc7-d77d-468b-b856-0ac66ace3a1e" />
 
## How it works
 
The enclosure sits under the mini. A 120mm aRGB fan mounts to the underside of the top plate and blows **up** through a central airflow cutout into the mini's intake. Intake air reaches the fan through vent slots on all four walls. Fan + LEDs run over USB (dock or wall adapter), with one rocker switch cutting power to both.
 
```
USB-A power -> trunk cable (switch inline) -> Y-splitter
   -> boost cable (5V->12V) -> fan motor (4-pin PWM)
   -> aRGB controller       -> fan LEDs (3-pin aRGB)
```
 
## Specs
 
| Feature | Spec |
|---|---|
| Footprint | 130 × 130 mm |
| Plate thickness | 6 mm |
| Wall height | 32 mm (fits the 25 mm fan with clearance) |
| Airflow cutout | ~108 mm, radiused inlet to reduce flow separation |
| Fan mounting | 4 bosses + M4 heat-set inserts, 105 mm pattern |
| Reinforcement | Corner gussets bracing bosses to walls |
| Venting | Vertical slots on all four walls |
| Rear | Switch cutout (19.2 × 12.7 mm) + cable hole (~10 mm) |
 
## Files
 
- **[BOM.md](BOM.md)** — full parts list, links, cost (~$115 core build)
- **[reflections.md](reflections.md)** — what I learned building it
- `cad/` — STEP (source) + STL (for printing)
## Assembly notes
 
- Melt M4 heat-set inserts into the four bosses.
- Bolt the fan to the underside, airflow arrow pointing **up**.
- Splice the switch inline on the USB 5V wire, then split to the boost cable (motor) and aRGB controller (LEDs).
- Walls are 8 mm — thicker than the switch's snap clips, so it's friction-fit for v1 (thinned pocket planned for v2).
- Add silicone feet for grip and a small air gap.
## Roadmap
 
- [ ] Print v1 and test-fit
- [ ] Assemble and verify wiring
- [ ] Thermal test: temps with stand off vs. on
- [ ] v2 tweaks from the print
- [ ] Future: CFD airflow sim
