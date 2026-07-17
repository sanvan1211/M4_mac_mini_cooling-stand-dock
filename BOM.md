# Bill of Materials — M4 Mac Mini Cooling Stand / Dock
 
**Project:** Elevated aRGB cooling stand for the M4 Mac mini
**Author:** Sanhith Vandara
**Version:** v1
**Last updated:** July 2026
 
Prices are estimates from mid-2026 listings and will vary — check live pricing before ordering. Links point to representative products; equivalent parts from other reputable brands work fine where noted.
 
## Core components
 
| # | Part | Purpose | Qty | Est. Price | Link |
|---|------|---------|-----|-----------|------|
| 1 | Razer Kunai Hydraulic 120mm aRGB Fan (single) | Main cooling fan + underglow lighting | 1 | ~$35 | [Amazon](https://www.amazon.com/Razer-Kunai-Hydraulic-120MM-aRGB/dp/B09JRMGLQF) |
| 2 | CRJ 12V Step-Up USB Fan Power Adapter Cable | Boosts USB 5V → 12V to run the fan motor | 1 | ~$13 | [Amazon](https://www.amazon.com/CRJ-Voltage-Step-Up-Sleeved-Adapter/dp/B07QFG6LFR) |
| 3 | ELFJMZP USB-Powered 5V 3-Pin ARGB Controller (w/ remote) | Drives the fan's aRGB LEDs from USB, no motherboard needed | 1 | ~$10 | [Amazon](https://www.amazon.com/ELFJMZP-ARGB-LED-Controller-3-Pin/dp/B0FLY3J3YZ) |
 
## Power switch & wiring
 
| # | Part | Purpose | Qty | Est. Price | Link |
|---|------|---------|-----|-----------|------|
| 4 | DaierTek Mini Rocker Switch KCD1, 2-pin SPST (10-pack) | Master on/off for the whole unit | 1 | ~$9 | [Amazon](https://www.amazon.com/DaierTek-250VAC-Rocker-KCD1-101-Plastic/dp/B07S2QJKTX) |
| 5 | USB-A 1-male-to-2-female Y splitter cable | Splits switched power to the fan branch + the LED branch | 1 | ~$8 | [Amazon](https://www.amazon.com/Splitter-Female-Adapter-Extension-Devices/dp/B0B4MZLY6W) |
| 6 | USB 2.0 A-male to A-female extension cable (~3ft) | "Trunk" cable — cut and splice the switch inline on this | 1 | ~$7 | [Amazon](https://www.amazon.com/AmazonBasics-Male-Female-Extension-Cable/dp/B001TH7GV4) |
| 7 | Heat shrink tubing assortment | Insulate the soldered switch splice | 1 | ~$7 | [Search](https://www.amazon.com/s?k=heat+shrink+tubing+kit+assorted) |
 
## Fasteners & assembly
 
| # | Part | Purpose | Qty | Est. Price | Link |
|---|------|---------|-----|-----------|------|
| 8 | M4 brass heat-set threaded inserts (50-pack) | Reusable threads in the printed bosses for fan mounting | 1 | ~$9 | [Amazon](https://www.amazon.com/Threaded-Inserts-Plastic-Printing-Components/dp/B0DNTVDGMB) |
| 9 | M4 machine screws assortment | Mount the fan into the inserts | 1 | ~$9 | [Search](https://www.amazon.com/s?k=m4+machine+screws+assortment+kit) |
| 10 | Silicone/rubber adhesive feet | Anti-slip, adds a small bottom air gap | 1 set | ~$7 | [Search](https://www.amazon.com/s?k=silicone+adhesive+bumper+feet) |
 
## Consumables & tools
 
| # | Part | Purpose | Qty | Est. Price | Link |
|---|------|---------|-----|-----------|------|
| 11 | PETG filament, 1kg (or PLA) | 3D printing the enclosure | 1 | ~$20 | [Search](https://www.amazon.com/s?k=petg+filament+1.75mm+1kg) |
| 12 | Soldering iron kit (60W adjustable) | Switch splice + setting heat-set inserts | 1 | ~$22 | [Search](https://www.amazon.com/s?k=soldering+iron+kit+60w+adjustable) |
| 13 | Digital calipers | Measuring parts for CAD | 1 | ~$10 | [Search](https://www.amazon.com/s?k=digital+calipers+6+inch) |
 
## Key specifications
 
**Fan — Razer Kunai 120mm**
- Dimensions: 120 × 120 × 25 mm
- Rated voltage / current: 12V DC / 0.28 A
- Connectors: 4-pin PWM (motor) + 3-pin 5V aRGB (lighting)
- Mounting: standard 120mm pattern — 105 × 105 mm hole square, M4 screws
- 18 addressable LEDs
**Enclosure (3D printed)**
- Footprint: 130 × 130 mm (matches M4 mini's 127 mm footprint with a slim border)
- Plate thickness: 6 mm (thickened from 4 mm for rigidity under the mini's weight)
- Wall height: 32 mm (houses the 25 mm-thick fan with clearance)
- Central airflow cutout: ~108 mm, with a filleted (radiused) inlet to reduce flow separation
- Fan mounting: four raised bosses with M4 heat-set inserts, corner gussets for load distribution
- Venting: vertical intake slots on all four walls (finer on sides, wider on back)
- Rear: switch cutout (19.2 × 12.7 mm) + cable exit hole (~10 mm)
**Power / wiring topology**
```
USB-A power (dock or wall)
   → trunk cable (switch spliced inline on the 5V wire)
      → Y-splitter
         → CRJ boost cable (5V→12V) → fan 4-pin PWM (motor)
         → ELFJMZP aRGB controller → fan 3-pin aRGB (LEDs)
```
The single switch cuts power to both the fan motor and the LEDs at once.
 
---
 
## Notes & considerations
 
- **Power source:** designed to run off a powered USB-A source (dock or wall adapter), independent of the Mac mini's own ports — this keeps the mini's ports free and avoids drawing the combined fan + LED current through one port.
- **Switch snap-fit:** the printed walls are 8 mm thick; the KCD1's snap clips are designed for ~2 mm panels. For v1, friction-fit or adhesive is used; a thinned mounting pocket is a planned v2 improvement.
- **Airflow direction:** fan blows **up** into the mini's bottom intake (intake-assist). The wall vents are **intake** for the fan; the mini exhausts its own hot air out its rear, above the enclosure.
## Rough cost
 
- **Core build (fan, power, switch, wiring, fasteners):** ~$115
- **With consumables/tools (filament, iron, calipers):** ~$167
*Costs assume no tools on hand. If you already own a soldering iron, calipers, and filament, the core build is the relevant number.*
