# Reflections — My First CAD Project
 
This was my first CAD project ever. No class, no YouTube tutorials, no prior experience. Just me, Onshape, an idea for a cooling stand, and a lot of trial and error. But I do have *Claude Pro*, and that saved me multiple times but anyway here's what I learned.
 
## What I thought CAD would be
 
Going in, I figured CAD would be pretty easy. Draw a few lines, grab the little arrows, pull stuff in and out, done. I knew there'd be some math involved, but I didn't realize how much of it would be *geometry* — angles, references, measurements, everything relating to everything else. It's less "drawing" and more "defining exactly where every point lives and how it relates to every other point."
 
The hardest part wasn't the tools themselves. It was taking the picture in my head and actually getting it onto the screen. I'd know exactly what I wanted the stand to look like, and then spend forever figuring out which combination of sketches, extrudes, and fillets would actually produce that shape. There were a *lot* of changes along the way. The design I ended up with is not the design I started with.
 
## Trial and error (with worse error messages)
 
CAD reminded me a lot of programming — it's iterative, you break things constantly, and you fix them one at a time. But there's one big difference: when you write code and something breaks, it *tells* you what went wrong. Syntax error, runtime error, logic error, whatever. You get a hint, or your program just dosent work as intended.
 
CAD doesn't do that. When something's wrong, it just turns red. That's it. No explanation, no error type, no line number. Just red, and you're on your own to figure out what it's mad about. "Sketch could not be solved" became a phrase I saw in my sleep.
 
Honestly though, none of those errors really stuck with me as *the* moment, because I overcame all of them. It was just a constant loop: something breaks, figure out why, fix it, keep moving. That loop got faster the more I did it.
 
## The skills I actually picked up
 
For a first project, I ended up learning way more than I expected:
 
- **Sketching and dimensioning** — center-point and corner rectangles, circles, and the golden rule I learned the hard way: *dimension holes from the center, not the edge* (this is why one of my fan holes was misaligned for a while).
- **Extrudes** — both adding material and cutting through it (Remove / Through all).
- **Fillets** — for looks (rounding the corners into a soft box) and for function (radiusing the airflow inlet and the interior corners).
- **Bosses** — building up thicker cylinders around holes so my M4 brass heat-set inserts would have something to grip.
- **Parametric editing** — when my plate was too thin for the mini's weight, I just changed one number (4mm → 6mm) and watched the *entire* model rebuild itself around it. That was the moment CAD clicked as something powerful, not just fiddly.
- **Linear patterns** — repeating the vent slots across a wall instead of drawing 15 of them by hand.
- **Mirror** — copying features to the opposite side.
- **Sketching on vertical faces** — not just the flat top, which is more disorienting than it sounds.
- **Diagnosing red errors** — the actual core skill of the whole thing.
- **Designing for real-world assembly** — corner gussets for strength, clearance for the fan, cutouts for the switch and cable, and applying fluid dynamics (a radiused inlet to reduce flow separation and turbulence) to actually optimize airflow into the mini.

## How it turned out
 
Really well, I'm proud of it. It went from "I can't get a dimension box to open" to a clean, structurally sound enclosure with vents on all four walls, a switch, a cable pass-through, and airflow I thought about instead of just guessing at.
 
## What's next
 
I can't wait to do more projects. I might try a **liquid-cooled Mac mini** as a future build,  it probably wouldn't improve performance much, but it'd definitely help with thermals and keep things cool. In case I ever decide to sacrifice my Mac mini to OpenClaw.
