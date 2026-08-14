# Bill of Materials — M4 Mac Mini Cooling Stand / Dock

**Project:** Elevated aRGB cooling stand for the M4 Mac mini
**Author:** Sanhith Vandara
**Version:** v2 (A-tier submission)
**Last updated:** August 2026

**Requested funding: $64.50 against the $120 A-tier budget.**

Commodity parts are sourced from AliExpress. Two parts stay on Amazon for spec reasons
documented below. Prices are pre-order estimates — confirm against the live listing before
ordering, since AliExpress pricing moves and listings are frequently relisted.

---

## Parts

| # | Part | Purpose | Source | Est. price |
|---|------|---------|--------|-----------|
| 1 | Razer Kunai Hydraulic 120mm aRGB Fan | Main cooling fan + underglow | Amazon | $35.00 |
| 2 | USB 5V→12V step-up cable (3/4-pin fan end) | Boosts USB 5V to 12V for the fan motor | AliExpress | $2.00 |
| 3 | ELFJMZP USB 5V 3-pin ARGB controller | Drives the fan LEDs from USB | Amazon | $10.00 |
| 4 | USB-A 1→2 Y splitter cable | Splits switched power to fan + LED branches | AliExpress | $1.50 |
| 5 | USB 2.0 A-male to A-female extension (1m) | Trunk cable — switch splices inline here | AliExpress | $1.50 |
| 6 | KCD1 mini rocker switch (5-pack) | Master on/off | AliExpress | $1.80 |
| 7 | M4 brass heat-set inserts (20-pack) | Threads in the printed bosses | AliExpress | $2.20 |
| 8 | M4 × 20mm machine screws (20-pack) | Mount the fan into the inserts | AliExpress | $1.80 |
| 9 | Heat-set insert soldering tips | Seats the brass inserts squarely | AliExpress | $3.00 |
| 10 | Heat shrink tubing assortment | Insulate the switch splice | AliExpress | $1.50 |
| 11 | Silicone adhesive feet (20-pack) | Grip + small bottom air gap | AliExpress | $1.20 |
| 12 | PETG filament — 150 g consumed | Prints the enclosure | Amazon | $3.00 |
| | **Total** | | | **$64.50** |

Amazon: $48.00 · AliExpress: $16.50 · **A-tier headroom remaining: $55.50**

**Filament is costed at material consumed, not spool price.** The enclosure uses ~150 g of
a 1 kg PETG spool at ~$20/kg, so the material cost of one unit is $3.00. Note that filament
is not sold in 150 g units — the smallest practical purchase is either a 1 kg spool (~$20)
or a 250 g sample spool (~$8–10). See the pro-rating note below.

Full links are in `BOM.csv`. Spec-critical parts carry direct item links; interchangeable
commodity parts carry AliExpress category search URLs, which stay valid when individual
listings are relisted.

## Covered elsewhere — not funded by this BOM

| Item | Covered by |
|------|-----------|
| Soldering iron | Hackpad Soldering Iron Grant — $18, one-time |
| Enclosure print service | Printing Legion Grant — $5 shipping credit, under 300 g (optional alternative) |
| Digital calipers | Already owned |
| Hot glue gun | Already owned — seats the switch, not the inserts |

---

## Two parts that could not be substituted

**ARGB controller — stays on Amazon.** Nearly every ARGB controller sold on AliExpress
draws power over **SATA**, from a desktop PSU. This build has no PSU; the entire power
topology runs from a single USB-A source. A SATA controller would either not work or
require an additional USB→SATA adapter, adding a part and a failure point to save about
$7 on a budget with $58 of slack. The USB-native ELFJMZP unit is kept.

**Step-up cable — connector type matters.** Most 5V→12V USB boost cables terminate in a
**5.5 × 2.1 mm barrel jack**, which will not mate with a PC fan. The required variant ends
in a 3-pin/4-pin fan connector. Confirm the connector in the listing photos before ordering.

---

## What changed from v1

The v1 BOM totalled ~$134, sourced entirely from Amazon, with a separate tools table.

- **Fan kept as-is.** The Razer Kunai is the one line where the brand buys something real —
  hydraulic bearing, 18 addressable LEDs, a known noise profile. Held at $35.
- **Interchangeable parts moved to AliExpress**, saving ~$55: cables, switch, fasteners,
  heat shrink, feet. Identical specs; the Amazon premium was markup, not quality.
- **Two parts deliberately not moved** — see the section above.
- **Multi-packs downsized.** 50 inserts and a 10-pack of switches exceeded what one build
  needs; 20-packs and 5-packs cost less and waste less.
- **Filament re-added at consumed cost ($3.00), not spool cost ($20).** v1 charged a full
  1 kg spool to a build that uses 150 g.
- **Soldering iron removed ($22).** Covered by the Hackpad grant.
- **Insert-setting tips added ($3).** The iron alone cannot seat inserts squarely.
- **Consolidated to one BOM.** v1 had a `.md` and a `.csv` that disagreed on totals.
  `BOM.csv` is the source of truth; this file mirrors it.

## Sourcing and sequencing notes

- **Claim the Hackpad iron before ordering tips.** Insert tips thread onto the iron and
  thread standards differ between models. Confirm which iron ships, then buy matching tips.
- **AliExpress ships in roughly 2–5 weeks.** The iron gates assembly — both the inserts and
  the switch splice need it. Order early.
- **Buy from as few sellers as possible.** Ten orders means ten shipments and ten chances
  for shipping fees to creep in.
- **Prefer a fluid or hydraulic bearing** if substituting the fan later. This sits on a desk
  at ear level, and sleeve-bearing fans whine.
- **Filament pro-rating.** This BOM lists $3.00 — the value of plastic actually consumed. A
  spool cannot be bought in 150 g units, so the real out-of-pocket purchase is ~$20 for 1 kg
  (leaving 850 g for future prints) or ~$8–10 for a 250 g sample spool. If reimbursement is
  tied to receipts rather than consumption, submit the spool price instead; the budget
  absorbs it either way ($81.50 of $120 at full spool price).
- **Insert-setting temperature:** roughly 20–40 °C above print temperature. PETG prints at
  230–250 °C, so set the iron near 260–270 °C. A hot glue gun tops out around 200 °C and
  cannot do this job.

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
- Print weight: ~150 g (under the Printing Legion 300 g limit)

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

- **Power source:** runs off a powered USB-A source (dock or wall), independent of the
  mini's ports — keeps the mini's ports free and avoids drawing the combined fan + LED
  current through one port.
- **Switch fit:** walls are 8 mm thick; the KCD1's snap clips want ~2 mm, so the switch is
  friction-fit and hot-glued for v1. A thinned mounting pocket is a planned v2 improvement.
- **Airflow:** fan blows **up** into the mini's intake. Wall vents are **intake** for the
  fan; the mini exhausts its own hot air out its rear, above the enclosure.
- **Fan speed:** the PWM pin is currently unconnected, so the motor runs at 100% duty.
  Closed-loop speed control is the obvious use of the remaining headroom.
