# M4 Mac mini cooling dock project Journal

## This is my journal for this project

#### I am doing this project for a few different reasons:

1. To improve my CAD skills.
2. To keep my Mac mini cool during heavy workloads.
3. To have fun building small engineering projects.

This project is being completed through Hack Club.

### Tools/Software used: 
Claude - Drafting ideas, searching for similar projects, wiring and techicals


# Entry 1: setting up Onshape and Selecting a fan for project 
#### July 13 2026: 14:30-16:50 hours 

### Fan Comparison

| Fan | Approx. Price | Connector Type | Pros | Cons | Decision |
|------|--------------:|----------------|------|------|----------|
| **Arctic P12 A-RGB** | ~$16 ($7 on sale (amazon) | Standard 4-pin PWM + 3-pin 5V ARGB | Affordable, quiet, excellent airflow, low power consumption, easy to wire | Simpler appearance than the Razer fan | Excellent value and a strong alternative |
| **Razer Kunai 120mm ARGB** | ~$25–45 | Standard 4-pin PWM + 3-pin 5V ARGB | Premium design, customizable lighting, quality construction, compatible with USB-to-12V conversion | More expensive and slightly louder at higher RPMs | ** Selected for the project** |
| **Corsair iCUE LINK LX120 RGB** | ~$35–45 | Proprietary Corsair iCUE LINK | High-quality fan with premium lighting effects | Requires Corsair's proprietary ecosystem and controller, making integration more difficult | Not selected due to unnecessary complexity |
|**Noctua NF-P12 redux-1700 PWM** | $16 | Standard 4-Pin PWM + 3 pin 5V A-RGB| afforabble| Good value and strong alternate

https://m.media-amazon.com/images/I/611T+f1qgRL._SX385_.jpg

When selecting a fan for this project, I considered three main factors: **compatibility**, **ease of integration**, and **overall appearance**.

While the **Arctic P12 A-RGB** offers the best value for the money, I ultimately chose the **Razer Kunai 120mm ARGB** because I wanted the finished build to be both functional and visually appealing. Since this is my first hardware project through **Hack Club Stardance**, I wanted to create something I would be proud to display and document and share with others.

Unlike the **Corsair iCUE LINK LX120**, which relies on a proprietary ecosystem, the Razer Kunai uses standard **4-pin PWM** and **3-pin 5V ARGB** connectors. This makes it much easier to power and integrate into a custom USB-powered cooling stand without requiring additional proprietary hardware.

I also already own several Razer products, including a **Razer Basilisk (V3) mouse **, **Razer x Gillette razor**, and **Razer Kraken X headset**. As a result, I have developed an appreciation for Razer's design language and product aesthetic and choosing the Kunai allows the project to fit naturally alongside the rest of my setup.

The customizable lighting adds a polished, premium appearance to the final build. Although it does not improve cooling performance, it makes the project more engaging to showcase in photos, videos, and GitHub documentation. I also have the Razer Synapse app installed on my Mac mini- so integrated it with the fan and my mouse would be cool as well. 

The Razer Kunai offers the right balance between performance, compatibility, and aesthetics. While it costs more than the Arctic alternative, I believe the improved appearance and straightforward integration make it the best fit for this project and my learning goals.

I stumbled upon some CAD models of a very similar design that I want to implement in my final design:

<img width="441" height="342" alt="Screenshot 2026-07-13 at 17 11 39" src="https://github.com/user-attachments/assets/55b8b310-771c-4744-a7a2-9c559608cf7c" />

https://makerworld.bblmw.com/makerworld/model/USf0e74c0e39cc1d/design/2025-01-12_810aa729b34ec.jpg?x-oss-process=image/resize,w_1000/format,webp 

https://makerworld.bblmw.com/makerworld/model/USf0e74c0e39cc1d/757755172/instance/b3691a0717b74142.png?x-oss-process=image%2Fformat%2Cwebp

https://makerworld.bblmw.com/makerworld/model/USd09a412849dba9/design/2025-08-04_63280fa71a038.jpg?x-oss-process=image/resize,w_1000/format,webp


After 'Clauding' and searching the internet- ive came up with this brainstorm using canva: 

<img width="1096" height="602" alt="Screenshot 2026-07-13 at 17 41 38" src="https://github.com/user-attachments/assets/971f39cf-1d00-4a51-9c0e-1886a2800eba" />


# Entry 2: Desining the dock in onshape 
#### July 14 2026 

Today was one of those days where I got humbled, I did not know CAD was going to be this tedious. 

I sat down thinking I'd knock out a decent chunk of the stand in a couple of hours. In my head it was basically, "draw a square, cut a few holes, done." Instead, I spent the first hour just learning how Onshape actually wants you to think. It's funny because I'm so used to writing code (or vibecoding) where you can usually figure out what's wrong from an error message. CAD isn't like that at all. If you click the wrong face, forget a constraint, or select one extra sketch region, the entire feature changes and you don't even realize why. Even if its off by a few degrees or millimeters, the entire design can be the opposite of what you intended for. 

I started by creating the base plate for the stand. I sketched out a **150 mm × 150 mm** square, learned how to fully define a sketch with dimensions, and extruded it into a **4 mm thick** plate. That alone taught me more than I expected. I finally understood why people stress making sketches "fully constrained" instead of just eyeballing everything.

After that I worked on the airflow opening. The whole point of this project is to cool the Mac mini better, so getting the fan placement right is one of the most important parts. I cut the large center opening and then added the **four 4.3 mm mounting holes** using the standard **105 mm mounting pattern** for a 120 mm fan. It took me way longer than it probably should have because I kept accidentally selecting the wrong geometry.

At one point I genuinely thought I had destroyed my entire model.

I used **Extrude and Remove** on the mounting holes, hit the green checkmark, and suddenly all of my circles disappeared. My first thought was, "Great... I somehow deleted everything." After a few minutes of panicking (and almost reaching for Ctrl+Z), I realized Onshape was actually doing exactly what it was supposed to do—the sketch gets consumed once it becomes a real feature. 

 I imported a **STEP model of the M4 Mac mini** into Onshape so I could design around the actual computer instead of guessing dimensions. Seeing the Mac mini sitting inside my workspace made the project feel a lot more real. Eventually I'll use that model to make sure the stand, fan, and mounting points all line up correctly before I ever print anything.

The biggest lesson today was that CAD required A LOT of patience.

I came into this project thinking my experience with programming would make learning CAD pretty easy. Instead, I realized they're almost opposite ways of thinking. Programming is logical and sequential. CAD is incredibly visual and detail-oriented. Tiny decisions you make at the beginning affect everything that comes after. It's honestly been a humbling experience.

Even though I probably spent more time troubleshooting than actually designing, I ended the day with a completed base plate, a proper airflow cutout, and correctly spaced fan mounting holes. 

I'm definitely still a beginner, and there were moments today where I questioned if I was doing anything correctly. (But compared to where I was this morning) staring at a blank workspace with no idea where to click—I can already see progress. That's probably the coolest part of this project so far. 

<img width="886" height="749" alt="Screenshot 2026-07-14 at 21 10 15" src="https://github.com/user-attachments/assets/739361fd-d6f3-4f1c-aa61-54a1db1264ae" />

<img width="896" height="694" alt="Screenshot 2026-07-14 at 19 41 06" src="https://github.com/user-attachments/assets/d4401d4f-da7a-4890-a478-a95e4ec4ec9f" />

<img width="1262" height="784" alt="Screenshot 2026-07-14 at 21 02 02" src="https://github.com/user-attachments/assets/d261f6c0-fbd5-454e-9c6e-411b7d51ce06" />

This is a mac mini display I used as refernce while working on my design: 
https://grabcad.com/library/mac-mini-m4-2024-1

<img width="261" height="185" alt="Screenshot 2026-07-14 at 21 12 35" src="https://github.com/user-attachments/assets/42b29af9-cc76-4268-bf68-4ad9db0cd383" />

<img width="871" height="704" alt="Screenshot 2026-07-14 at 21 11 47" src="https://github.com/user-attachments/assets/2c36702c-38c9-49ef-b373-f469774b228c" />

# Entry 3: Applying Fluid Dynamic Principles to the body & getting better at CAD
#### July 16 2026

Today was probably the day where CAD finally started making sense.

When I first started this project, every little thing felt like a battle with the software. I was constantly asking Claude where to click, what tool to use, or what happend to my circles. Today was different though. I was actually able to navigate sketches, change dimensions, and make design decisions without needing someone (or some LLM) to walk me through every single step.

I’m finally starting to get the hang of CAD.

The main goal today was finishing the rest of the enclosure body and making the airflow design cleaner.

The first thing I worked on was the intake opening. Originally, the opening had sharp edges, which technically works, but it isn't ideal for airflow. I decided to add fillets and smooth out the transition into the enclosure.

### Radiused inlet and computational fluid dyanamics (CFD)

The engineering principle behind this design is a **radiused inlet**. Instead of forcing incoming air to make a sudden **90-degree turn** around a sharp edge, the rounded surface creates a smoother transition that allows the airflow to follow the intended path. This reduces the likelihood of **flow separation**, where air detaches from the surface and creates recirculation regions, increased turbulence, and inefficient airflow patterns. By maintaining smoother streamlines and reducing stagnant zones near the intake, a radiused inlet can improve the overall efficiency of the cooling system.

To understand how inlet geometry affects airflow behavior, computational fluid dynamics (CFD) simulations can be used to visualize velocity changes and flow separation regions. The figure below demonstrates how airflow behaves around an intake opening. Areas of lower velocity (blue regions) indicate regions where airflow slows down, which can correspond to recirculation zones and potential flow separation. 

<img width="680" height="571" alt="image" src="https://github.com/user-attachments/assets/e537d03b-eaf0-4873-8bc1-333dcc74f225" />

Sharp edges can create abrupt changes in flow direction, causing the airflow to detach from the surface and form turbulent wake regions behind the intake. By introducing a radiused inlet, the transition into the opening becomes smoother, allowing streamlines to remain more attached and reducing areas of stagnant airflow.

This same principle applies to the enclosure design. A rounded fan intake reduces sudden pressure changes at the entrance, improving airflow consistency and allowing the cooling fan to operate more efficiently.

Source:
"Trust me bro", (jk): 
- Anderson, J. D. *Fundamentals of Aerodynamics*, 6th Edition, McGraw-Hill Education, 2017.
- NASA Glenn Research Center — Boundary Layer and Flow Separation Concepts: (https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/boundary-layer/)
- https://www.researchgate.net/publication/259889963_On_The_Use_Of_InflowOutflow_Boundary_Conditions_In_Incompressible_Internal_Flow_Problems_Using_Smoothed_Particle_Hydrodynamics

I’m not claiming that adding a few fillets will magically drop temperatures by 20 degrees (and thats not the point of this project), but it was cool being able to apply actual fluid dynamics concepts to something I was designing. Even the small details like edge geometry can matter when designing parts that interact with airflow, even on a miniscule applciation like this-cooling an already cool Mac Mini. 

## Fan Reference Dimensions

For the fan mounting system, I used the specifications from Razer’s Kunai Hydraulic Chroma Case Fans as a reference:

- Dimensions: **120mm × 25mm × 120mm**
- Fan size: **120mm**
- Thickness: **25mm**

Sources:
- https://mysupport.razer.com/app/answers/detail/a_id/5732/~/razer-kunai-hydraulic-chroma-case-fans-%7C-rc21-01800-support-%26-faqs
- https://www.youtube.com/watch?v=nCtzMYYiK6Q

<img width="527" height="321" alt="Screenshot 2026-07-16 at 21 03 44" src="https://github.com/user-attachments/assets/19738e82-6abe-427a-af61-abbe5af8e265" />

<img width="1154" height="782" alt="Screenshot 2026-07-16 at 21 01 50" src="https://github.com/user-attachments/assets/ea91190a-7b8a-4fac-a035-2cbc53a3e673" />

### Reinforcing the Fan Mounts

After fixing the airflow, I moved onto strengthening the fan mounting points.

I went back and resized the corner screw holes from **4.3mm to 5.6mm**. Then I created raised mounting bosses around each hole. These add extra material around the mounting points, making the enclosure stronger and giving the screws/inserts more support.

Originally, I was planning on saving these for a later version, but I decided to try making them myself. The gussets connect the fan bosses to the walls of the enclosure, which creates a stronger structure and helps spread out stress instead of concentrating it around one small area.

### Final Result

After a lot of filleting, extruding, tweaking dimensions, and fixing small mistakes, I ended up with this version:

<img width="928" height="770" alt="Screenshot 2026-07-16 at 21 44 50" src="https://github.com/user-attachments/assets/29fb4131-8670-40c4-917b-804a40a72f1d" />

<img width="835" height="651" alt="Screenshot 2026-07-16 at 21 55 36" src="https://github.com/user-attachments/assets/65014937-8787-45a7-aa83-1d9f737c10e9" />

Completed today:
- Smoothed and radiused airflow inlet
- Improved interior airflow 
- Resized fan mounting holes to 5.6mm
- Added reinforced fan bosses
- Added corner gussets for extra structural support
- Added interior and exterior fillets
- Adjusted and finalized bottom geometry

## Remaining Tasks
- Add vents for airflow
- Add switch cutout ( i might do this)
- Add silicone pad mounting locations ( not that important)
- Final CAD cleanup
- Export STL/STEP files for manufacturing and testing
- Put the M4 MAC MINI cad alongside this

I also might do an airflow simulation later to see how it performs and actually visualize those CFD applications on my design. 
