W, H = 1220, 770
INK = "#1a1a1a"
V12 = "#c1440e"
V5 = "#b8860b"
GND = "#2b2b2b"
DATA = "#1f6f8b"
NC = "#9a9a9a"

out = []
A = out.append

A(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" 'f'viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Helvetica, Arial, sans-serif">')
A(f'<rect width="{W}" height="{H}" fill="#fbfbf8"/>')
A(f'<rect x="14" y="14" width="{W-28}" height="{H-28}" fill="none" stroke="{INK}" stroke-width="1.6"/>')


def box(x, y, w, h, ref, value, sub=None):
    A(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#ffffff" 'f'stroke="{INK}" stroke-width="1.8" rx="2"/>')
    A(f'<text x="{x+w/2}" y="{y-16}" font-size="15" font-weight="bold" 'f'fill="{INK}" text-anchor="middle">{ref}</text>')
    A(f'<text x="{x+w/2}" y="{y-2}" font-size="11.5" fill="#555" 'f'text-anchor="middle">{value}</text>')
    if sub:
        A(f'<text x="{x+w/2}" y="{y+h+15}" font-size="10.5" fill="#666" 'f'font-style="italic" text-anchor="middle">{sub}</text>')


def pin(x, y, side, num, name, color=INK, length=34, dashed=False):
    dx = -length if side == "L" else length
    dash = ' stroke-dasharray="4,3"' if dashed else ''
    A(f'<line x1="{x}" y1="{y}" x2="{x+dx}" y2="{y}" stroke="{color}" 'f'stroke-width="2"{dash}/>')
    nx = x + dx/2
    A(f'<text x="{nx}" y="{y-6}" font-size="9.5" fill="#777" 'f'text-anchor="middle">{num}</text>')
    tx = x + (10 if side == "L" else -10)
    anchor = "start" if side == "L" else "end"
    A(f'<text x="{tx}" y="{y+4}" font-size="11" fill="{INK}" 'f'text-anchor="{anchor}">{name}</text>')
    return (x + dx, y)


def wire(pts, color=INK, width=2.2, dashed=False):
    d = " ".join(f"{'M' if i == 0 else 'L'}{px},{py}" for i, (px, py) in enumerate(pts))
    dash = ' stroke-dasharray="5,4"' if dashed else ''
    A(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" 'f'stroke-linejoin="miter"{dash}/>')


def junction(x, y, color=INK):
    A(f'<circle cx="{x}" cy="{y}" r="4" fill="{color}"/>')


def netlabel(x, y, text, color, anchor="middle", dy=-9):
    A(f'<text x="{x}" y="{y+dy}" font-size="11.5" font-weight="bold" 'f'fill="{color}" text-anchor="{anchor}">{text}</text>')


box(70, 300, 118, 116, "J1", "USB-A plug", "powered hub or wall PSU")
j1_v = pin(188, 330, "R", "1", "VBUS +5V", V5)
j1_g = pin(188, 392, "R", "4", "GND", GND)
A('<text x="129" y="368" font-size="10" fill="#999" text-anchor="middle">'f'D- / D+ unused</text>')

A(f'<text x="279" y="286" font-size="15" font-weight="bold" fill="{INK}" 'f'text-anchor="middle">SW1</text>')
A(f'<text x="279" y="300" font-size="11.5" fill="#555" text-anchor="middle">'f'KCD1 SPST</text>')
wire([(222, 330), (252, 330)], V5)
A(f'<circle cx="256" cy="330" r="4.5" fill="#fff" stroke="{V5}" stroke-width="2"/>')
A(f'<circle cx="302" cy="330" r="4.5" fill="#fff" stroke="{V5}" stroke-width="2"/>')
wire([(259, 327), (300, 309)], V5, width=2.4)
wire([(306, 330), (340, 330)], V5)
A('<text x="279" y="356" font-size="10" fill="#666" text-anchor="middle" 'f'font-style="italic">spliced inline on +5V</text>')

wire([(222, 392), (340, 392)], GND)

box(340, 300, 122, 116, "J2", "USB-A Y splitter", "1 male to 2 female")
netlabel(487, 322, "+5V_SW", V5)
netlabel(481, 417, "GND", GND)

junction(462, 330, V5)
junction(462, 392, GND)

wire([(462, 330), (510, 330), (510, 176), (556, 176)], V5)
wire([(462, 392), (492, 392), (492, 214), (556, 214)], GND)

wire([(462, 330), (530, 330), (530, 520), (556, 520)], V5)
wire([(462, 392), (510, 392), (510, 558), (556, 558)], GND)

box(556, 140, 150, 116, "U1", "USB 5V→12V boost", "step-up cable, 1A")
A(f'<text x="566" y="180" font-size="11" fill="{INK}">VIN +5V</text>')
A(f'<text x="566" y="218" font-size="11" fill="{INK}">GND</text>')
u1_v = pin(706, 176, "R", "", "+12V", V12)
u1_g = pin(706, 214, "R", "", "GND", GND)
netlabel(748, 168, "+12V", V12)

box(830, 120, 158, 172, "J3", "Fan motor header", "4-pin PWM — Razer Kunai")
f_g = pin(830, 152, "L", "1", "GND", GND)
f_v = pin(830, 190, "L", "2", "+12V", V12)
f_s = pin(830, 228, "L", "3", "SENSE / TACH", NC, dashed=True)
f_p = pin(830, 266, "L", "4", "PWM CONTROL", NC, dashed=True)

wire([(740, 176), (768, 176), (768, 190), (796, 190)], V12)
wire([(740, 214), (782, 214), (782, 152), (796, 152)], GND)

for yy in (228, 266):
    A(f'<line x1="789" y1="{yy-7}" x2="803" y2="{yy+7}" stroke="{NC}" stroke-width="2"/>')
    A(f'<line x1="803" y1="{yy-7}" x2="789" y2="{yy+7}" stroke="{NC}" stroke-width="2"/>')
A(f'<text x="780" y="232" font-size="10.5" font-weight="bold" fill="#555" text-anchor="end">NC</text>')
A(f'<text x="780" y="270" font-size="10.5" font-weight="bold" fill="#555" text-anchor="end">NC</text>')

box(556, 484, 150, 116, "U2", "USB ARGB controller", "ELFJMZP, IR remote")
A(f'<text x="566" y="524" font-size="11" fill="{INK}">VIN +5V</text>')
A(f'<text x="566" y="562" font-size="11" fill="{INK}">GND</text>')
pin(706, 508, "R", "", "+5V", V5)
pin(706, 534, "R", "", "DATA", DATA)
pin(706, 560, "R", "", "GND", GND)

box(830, 470, 158, 140, "J4", "Fan ARGB header — 3-pin 5V")
pin(830, 502, "L", "1", "+5V", V5)
pin(830, 540, "L", "2", "DATA", DATA)
pin(830, 578, "L", "4", "GND", GND)
A(f'<text x="909" y="600" font-size="9.5" fill="#999" text-anchor="middle">'f'pos. 3 keyed &#183; 18 LEDs</text>')

wire([(740, 508), (796, 508), (796, 502)], V5)
wire([(740, 534), (796, 534), (796, 540)], DATA)
wire([(740, 560), (778, 560), (778, 578), (796, 578)], GND)

A(f'<rect x="60" y="45" width="440" height="130" fill="#f2f2f0" 'f'stroke="#8c8c8c" stroke-width="1.3" rx="2"/>')
A(f'<text x="78" y="69" font-size="12.5" font-weight="bold" fill="{INK}">'f'Design note — J3 pins 3 and 4</text>')
for i, ln in enumerate([
        "PWM CONTROL (pin 4) is left floating, so the motor runs at",
        "100% duty continuously. SENSE (pin 3) is unread, so there is no",
        "RPM feedback. Both are intentional for v1: the single SW1 rocker",
        "is the only control. Closed-loop speed control via an MCU on",
        "these two pins is the planned v2 revision."]):
    A(f'<text x="78" y="{91+i*17}" font-size="11" fill="#3a3a3a">{ln}</text>')

A(f'<rect x="70" y="620" width="440" height="100" fill="#ffffff" 'f'stroke="{INK}" stroke-width="1.2" rx="3"/>')
A(f'<text x="88" y="644" font-size="12" font-weight="bold" fill="{INK}">Nets</text>')
legend = [(V5, "+5V_SW", "switched USB rail — feeds U1 and U2"),
          (V12, "+12V", "boosted rail — fan motor only"),
          (GND, "GND", "common return, unswitched"),
          (DATA, "DATA", "addressable LED serial line")]
for i, (c, nm, desc) in enumerate(legend):
    yy = 665 + i * 16
    A(f'<line x1="88" y1="{yy-4}" x2="118" y2="{yy-4}" stroke="{c}" stroke-width="2.6"/>')
    A(f'<text x="128" y="{yy}" font-size="10.5" font-weight="bold" fill="{c}">{nm}</text>')
    A(f'<text x="196" y="{yy}" font-size="10.5" fill="#555">{desc}</text>')

tb_x, tb_y, tb_w, tb_h = 700, 620, 500, 100
A(f'<rect x="{tb_x}" y="{tb_y}" width="{tb_w}" height="{tb_h}" fill="#ffffff" 'f'stroke="{INK}" stroke-width="1.6"/>')
A(f'<line x1="{tb_x}" y1="{tb_y+38}" x2="{tb_x+tb_w}" y2="{tb_y+38}" 'f'stroke="{INK}" stroke-width="1"/>')
A(f'<line x1="{tb_x+320}" y1="{tb_y+38}" x2="{tb_x+320}" y2="{tb_y+tb_h}" 'f'stroke="{INK}" stroke-width="1"/>')
A(f'<text x="{tb_x+14}" y="{tb_y+25}" font-size="13" font-weight="bold" fill="{INK}">'f'M4 Mac mini Cooling Stand</text>')
A(f'<text x="{tb_x+14}" y="{tb_y+58}" font-size="11" fill="#444">'f'Sanhith Vandara</text>')
A(f'<text x="{tb_x+14}" y="{tb_y+75}" font-size="11" fill="#444">'f'Hack Club Stardance</text>')
A(f'<text x="{tb_x+14}" y="{tb_y+92}" font-size="9" fill="#666" 'f'font-family="DejaVu Sans Mono, monospace">'f'github.com/sanvan1211/M4_mac_mini_cooling-stand-dock</text>')
A(f'<text x="{tb_x+334}" y="{tb_y+58}" font-size="11" fill="#444">2026-08</text>')

A('</svg>')

open("schematic.svg", "w").write("\n".join(out))
print("wrote schematic.svg")
