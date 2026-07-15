# M4 Mac mini cooling standProject Journal

## This is my journal for this project

#### I am doing this project for a few different reasons:

1. To improve my CAD skills.
2. To keep my Mac mini cool during heavy workloads.
3. To have fun building small engineering projects.

This project is being completed through Hack Club.

### Tools/Software used: 
Claude - Drafting ideas, searching for similar projects, wiring and techicals


## Entry 1: setting up Onshape and Selecting a fan for project 
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


## Entry 2: desining the dock in onshape 

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

I'm definitely still a beginner, and there were moments today where I questioned if I was doing anything correctly. But compared to where I was this morning—staring at a blank workspace with no idea where to click—I can already see progress. That's probably the coolest part of this project so far. Every mistake is making the next step just a little bit easier.


<img width="886" height="749" alt="Screenshot 2026-07-14 at 21 10 15" src="https://github.com/user-attachments/assets/739361fd-d6f3-4f1c-aa61-54a1db1264ae" />

<img width="896" height="694" alt="Screenshot 2026-07-14 at 19 41 06" src="https://github.com/user-attachments/assets/d4401d4f-da7a-4890-a478-a95e4ec4ec9f" />

<img width="1262" height="784" alt="Screenshot 2026-07-14 at 21 02 02" src="https://github.com/user-attachments/assets/d261f6c0-fbd5-454e-9c6e-411b7d51ce06" />

This is a mac mini display I used as refernce while working on my design: 
https://grabcad.com/library/mac-mini-m4-2024-1

<img width="261" height="185" alt="Screenshot 2026-07-14 at 21 12 35" src="https://github.com/user-attachments/assets/42b29af9-cc76-4268-bf68-4ad9db0cd383" />

<img width="871" height="704" alt="Screenshot 2026-07-14 at 21 11 47" src="https://github.com/user-attachments/assets/2c36702c-38c9-49ef-b373-f469774b228c" />


