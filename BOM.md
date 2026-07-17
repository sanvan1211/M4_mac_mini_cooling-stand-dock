# Bill of Materials — M4 Mac Mini Cooling Stand / Dock
 
**Project:** Elevated aRGB cooling stand for the M4 Mac mini
**Author:** Sanhith Vandara
**Version:** v1
**Last updated:** July 2026
 
Prices are mid-2026 estimates and will vary — check live listings before ordering. The tables separate what the build actually **consumes** from **one-time tools** you keep and reuse, and note where a part is sold in a multi-pack (so the real per-unit cost is lower than the pack price).
 
---
 
## Parts consumed in one build
 
These are the parts that actually go into (or get used up by) a single cooling stand.
 
| # | Part | Purpose | Pack | Used | Est. pack price | Link |
|---|------|---------|------|------|----------------|------|
| 1 | Razer Kunai Hydraulic 120mm aRGB Fan | Main cooling fan + underglow | single | 1 | ~$35 | [Amazon](https://www.amazon.com/Razer-Kunai-Hydraulic-120MM-aRGB/dp/B09JRMGLQF) |
| 2 | CRJ 12V Step-Up USB Fan Power Cable | Boosts USB 5V → 12V for the fan motor | single | 1 | ~$13 | [Amazon](https://www.amazon.com/CRJ-Voltage-Step-Up-Sleeved-Adapter/dp/B07QFG6LFR) |
| 3 | ELFJMZP USB 5V 3-Pin ARGB Controller (w/ remote) | Drives the fan's aRGB LEDs from USB | single | 1 | ~$10 | [Amazon](https://www.amazon.com/ELFJMZP-ARGB-LED-Controller-3-Pin/dp/B0FLY3J3YZ) |
| 4 | USB-A 1→2 Y splitter cable | Splits switched power to fan + LED branches | single | 1 | ~$8 | [Amazon](https://www.amazon.com/Splitter-Female-Adapter-Extension-Devices/dp/B0B4MZLY6W) |
| 5 | USB 2.0 A-male to A-female extension (~3ft) | "Trunk" cable — switch splices inline here | single | 1 | ~$7 | [Amazon](https://www.amazon.com/AmazonBasics-Male-Female-Extension-Cable/dp/B001TH7GV4) |
| 6 | DaierTek Mini Rocker Switch KCD1 (10-pack) | Master on/off | 10 | 1 | ~$9 | [Amazon](https://www.amazon.com/DaierTek-250VAC-Rocker-KCD1-101-Plastic/dp/B07S2QJKTX) |
| 7 | M4 brass heat-set inserts (50-pack) | Threads in the printed bosses | 50 | 4 | ~$9 | [Amazon](https://www.amazon.com/Threaded-Inserts-Plastic-Printing-Components/dp/B0DNTVDGMB) |
| 8 | M4 machine screws assortment | Mount the fan into the inserts | kit | 4 | ~$9 | [Search](https://www.amazon.com/s?k=m4+machine+screws+assortment+kit) |
| 9 | Heat shrink tubing assortment | Insulate the switch splice | kit | a few | ~$7 | [Search](https://www.amazon.com/s?k=heat+shrink+tubing+kit+assorted) |
| 10 | Silicone/rubber adhesive feet | Grip + small bottom air gap | set | 4 | ~$7 | [Search](https://www.amazon.com/s?k=silicone+adhesive+bumper+feet) |
| 11 | PETG (or PLA) filament, 1kg | Prints the enclosure (uses only a fraction of a spool) | 1kg | ~150g | ~$20 | [Search](https://www.amazon.com/s?k=petg+filament+1.75mm+1kg) |
 
## One-time tools (bought once, reused on every project)
 
| # | Part | Purpose | Est. price | Link |
|---|------|---------|-----------|------|
| 12 | Soldering iron kit (60W adjustable) | Switch splice + setting heat-set inserts | ~$22 | [Search](https://www.amazon.com/s?k=soldering+iron+kit+60w+adjustable) |
| 13 | Digital calipers | Measuring parts for CAD | ~$10 | [Search](https://www.amazon.com/s?k=digital+calipers+6+inch) |
 
---
 
## What it actually costs
 
Because several parts are multi-packs or tools, the sticker total overstates the cost of one unit. The honest numbers:
 
- **Full pack/kit total (buying everything fresh):** ~$137 for consumables + ~$32 tools = **~$169**
- **Realistic cost of one stand** (you keep the leftover inserts, screws, switches, filament, and tools): **~$70**
- **If you already own a soldering iron, calipers, and filament:** the remaining spend is just the fan, boost cable, controller, splitter, trunk cable, and switch ≈ **~$82** for those specific parts, most of it the fan.
The single biggest line item is the **Razer Kunai fan (~$35)** — chosen for its look and RGB. A functionally identical build using the **Arctic P12 PWM PST A-RGB (~$16)** would cut roughly $19; it uses the same 4-pin PWM + 3-pin aRGB connectors and the same 120mm mount, so nothing else in the design changes.
 
---
 
## Key specifications
 
**Fan — Razer Kunai 120mm**
- Dimensions: 120 × 120 × 25 mm
- Rated voltage / current: 12V DC / 0.28 A
- Connectors: 4-pin PWM (motor) + 3-pin 5V aRGB (lighting)
- Mounting: standard 120mm pattern — 105 × 105 mm hole square, M4 screws
- 18 addressable LEDs
**Enclosure (3D printed)**
- Footprint: 130 × 130 mm
- Plate thickness: 6 mm
- Wall height: 32 mm (houses the 25 mm fan with clearance)
- Central airflow cutout: ~108 mm, radiused inlet to reduce flow separation
- Fan mounting: 4 bosses with M4 heat-set inserts, corner gussets for support
- Venting: vertical intake slots on all four walls
- Rear: switch cutout (19.2 × 12.7 mm) + cable exit hole (~10 mm)
**Power / wiring topology**
```
USB-A power (dock or wall)
   -> trunk cable (switch spliced inline on the 5V wire)
      -> Y-splitter
         -> boost cable (5V->12V) -> fan motor (4-pin PWM)
         -> aRGB controller       -> fan LEDs (3-pin aRGB)
```
The single switch cuts power to both the fan motor and the LEDs at once.
 
---
 
## Notes
 
- **Power source:** runs off a powered USB-A source (dock or wall), independent of the mini's ports — keeps the mini's ports free and avoids drawing the combined fan + LED current through one port.
- **Switch fit:** walls are 8 mm thick; the KCD1's snap clips want ~2 mm, so the switch is friction-fit/adhered for v1. A thinned mounting pocket is a planned v2 improvement.
- **Airflow:** fan blows **up** into the mini's intake. Wall vents are **intake** for the fan; the mini exhausts its own hot air out its rear, above the enclosure.
