# Using an Unmanned Aerial Vehicle to Gather Data From the "Edge of Space."
*WINTER JOSEPH GUERRA*

**Mentor: THEODORE THEODOSOPOULOS**

Abstract:
=====
Since I had first been introduced to the field of amateur unmanned aerial vehicles (UAVs), I’ve always wanted to build one myself. Although I wanted to build my science research project around this goal, I did not want to simply recreate what others had already done. I wanted to build a UAV from scratch that would not only help me improve my engineering skills, but also serve some greater purpose. Hence, a radical idea began to take shape: could our research team design a UAV that could gather data from the edge of space?

Taking stock of the numerous technological advances pioneered in the burgeoning field of amateur high-altitude ballooning, it seemed quite possible for our team to design an aircraft that would enable us to log video, temperature, location, and altitude data up to heights as high as 30km by utilizing the lifting power of a weather balloon. However, we would still have to manually search for, and recover the aircraft after it returned to earth – perhaps after having drifted more than one hundred miles away from the original launch point. Could we design an aircraft that could travel to the edge of space, but then autonomously return to its original launch location?

Theoretically, using cheap DIY programmable avionics, it seems possible for our team to construct an autonomous UAV that uses a high-altitude weather-balloon to enter the stratosphere, before gently gliding back to its starting location using a small glider airframe, autopilot, GPS, and magnetometer. Fully realized, this type of data gathering UAV could drastically reduce the effort necessary for retrieval while also providing our team with stabilized video not possible using currently existing high-altitude video capture methods. Currently, our team has proved successful in sourcing the avionics needed for autonomous aircraft navigation, and have also managed to research and develop various preliminary designs of various subcomponents of the vehicle such as the airfoil, bus design, and camera subsystem. 

Design stages:
=======
Sending an unmanned aerial vehicle to the edge of space requires a lot of planning, design, and testing before a test launch can ever be achieved. Although our team was not able to complete all of the steps necessary for a launch, we learned quite a bit about what it means to embark upon an ambitious engineering project. For our project, we split our design process into 6 distinct parts that included phases for aircraft hardware design, electronics procurement, and software development. Here's an overview of our current planned and complete development stages.

Development Phases:
------

* Dev. Phase 1 – Software/Hardware Feasibility Tests 				
	* Phase 1.00 - Preliminary Research and Assorted Testing		*[Completed]*
* Dev. Phase 2 – Aircraft Design 									
	* Phase 2.00 - Preliminary Aircraft Design 					*[Completed]*
	* Phase 2.50 – Detailed Aircraft 3D Model 					*[Current]*
* Dev. Phase 3 – Aircraft Fabrication 							
	* Phase 3.00 - Aircraft Airframe Fabrication					*[Future Steps. Awaiting Termination of Phase 2.50]*
	* Phase 3.50 – Hardware/Software Development (Radios, etc.) 	*[Current]*
* Dev. Phase 4 – Aircraft Testing 								
	* Phase 4.00 - R/C Assisted Aircraft Testing 					*[Future Steps]*
	* Phase 4.50 – Electronics Stress Test/HIL Simulation 		*[Future Steps]*
	* Phase 4.75 – Telemetry Antenna Design & Fabrication 		*[Future Steps]*
* Dev. Phase 5 - First High Altitude Autonomous Flight 			
	* Phase 5.00 -  Request FAA Permission to Fly 				*[Future Steps]*
	* Phase 5.50 - First High Altitude Autonomous Flight 			*[Future Steps]*
* Dev. Phase 6 - Analyze Recorded Data 							
	* Phase 6.00 - Retrieve and Plot Gathered Data and Video 		*[Future Steps]*

Dev. Phase 1 – Software/Hardware Feasibility Tests [Completed]
-----
##### Phase 1.00 - Preliminary Research and Assorted Testing		[Completed]
In phase in 1 of our project, our team performed basic feasibility tests and research to verify that our planned project was theoretically possible for us to complete. Before giving the project a final go-ahead, our team researched current UAV designs, technologies available to the amateur UAV hobbyist, various aircraft manufacturing techniques, and the outcome of previous amateur high-altitude ballooning missions. Based on our research, we concluded that it should be possible to design, manufacture, and program a completely autonomous aircraft from scratch before also sending the aircraft up to space via weather balloon. Based on our research we also identified various potential sticking points that might arise during aircraft development including weight restrictions, potential power shortages, and atmospheric-induced maneuverability issues that would ultimately define many of our design choices and constraints.

For example, in addition to the FAA enforced ___ [CITE] pound maximum high altitude balloon payload weight, our aircraft had to be as light as possible to ease the manufacturing process. Operating under the impression that fabricating an aircraft that had a wingspan larger than 2 meters, this gave us an even tighter weight constraint of ___ [CITE] pounds by using a conservative RC glider wing loading rule of thumb. This is because, as the aircraft weight increased, the wingspan and chord of the aircraft had to increase [CITE] but also 

Furthermore, our airplane electronics had to be able to continue to maintain power to critical guidance and telemetry systems in the event of a unexpectedly long flight or   With these issues in mind, Dev. Phase 2 sought to roughly outline a design strategy that would mitigate the largest percentage of "mission critical" issues. 

Dev. Phase 2 – Aircraft Design [Completed]
----
##### Phase 2.00 - Preliminary Aircraft Design [Completed]
During phase 2.00, our team brainstormed various aircraft designs for the reentering craft. The aircraft had to be sturdy and streamlined enough to survive the baffling winds of the jet stream on the way up to the edge of space, while also being large enough to achieve a shallow enough glide slope to return to base. Furthermore, it had to have a design that was naturally stable and was also capable of operating at speeds nearing terminal velocity without catastrophically failing. Our first design, based off of a cylindrical bus design reminiscent of the cruise missile, sought to work within these constraints, but was ultimately written off as being too hard to design and fabricate. In addition, this design was also put under scrutiny for having too many failure points. 
![Photo: Sketch of Javelin-based Aircraft Design][Javlin_Photo]

For our second design, based off of the efficient "flying wing" design of some modern day R/C thermal gliders, we did away with the aircraft's cumbersome body and instead made the aircraft into a large flying wing. By making the aircraft a flying wing, we sacrificed internal space that would house electronics and cameras and also made the plane's wings more vulnerable to the baffling winds of the jet stream, but also immensely simplified the design and fabrication of the airframe. In addition, due to the airframe's simplicity, the design did not suffer from quite as many failure points as its predecessor. Ultimately, we decided to go with this design due to our large time constraint, but we also made sure to try and reduce the design's flaws before moving on with our design process. Namely, we were particularly afraid that the wings (now exposed during both the ascent and descent stage of the aircraft) could be damaged by the high winds of the jetstream. Hence, to try to reduce the potential magnitude of the stresses that such gusts would exert upon the wings, we imposed a 2 meter limit on the aircraft's wingspan, thus reducing the probability for wind-induced premature wing failure.
![Photo: Ted's Sketch of Flying Wing][Flying_Wing_Render]
 
Phase 2.50 – Detailed Aircraft 3D Model [Current]


Dev. Phase 3 – Aircraft Fabrication [Future Steps]
----
##### Phase 3.00 - Aircraft Airframe Fabrication
##### Phase 3.50 – Hardware/Software Development (Radios, etc.) [Current]

Dev. Phase 4 – Aircraft Testing
----
##### Phase 4.00 - R/C Assisted Aircraft Testing [Future Steps]
##### Phase 4.50 – Electronics Stress Test/HIL Simulation [Future Steps]
##### Phase 4.75 – Telemetry Antenna Design & Fabrication [Future Steps]

Dev. Phase 5 - First High Altitude Autonomous Flight
----
##### Phase 5.00 -  Request FAA Permission to Fly
##### Phase 5.50 - First High Altitude Autonomous Flight

Dev. Phase 6 - Analyze Recorded Data
----

Design Process:




Results:


Next Steps:



[Javlin_Photo]: photos/Design_1/Dorsal_View.jpeg
[Flying_Wing_Render]: photos/Design_2/Blender/Render1.png
