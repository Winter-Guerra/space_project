// Space project Bus and Gimbal creation OpenSCAD script.
// See www.thewinterland.net for more info
// Copyleft CC BY-SA 3.0 Winter Guerra, 2012.
// Github: github.com/xtremd

// Import Bus and Gimbal libraries
// May also use "use"
include <gimbal_Functions.scad>;
include <bus_Functions.scad>;

// Adjust Rendering Settings
// May have to set these individually instead
$fn=100;

// ## BUS SIZE VARIABLES ## //


//## CAMERA SIZE VARIABLES ##//
//Dimensions of the camera
//Assumes that the x axis of the camera is the sensor's x axis.
camera_Height = 20; //mm
camera_Width = 20; //
camera_Depth = 20; //
camera_Lense_Depth = 10;
camera_Lense_Diameter_1 = 10;
camera_Lense_Diameter_2 = 3;


//## GLOBAL GIMBAL SIZE VARIBALES ##//
//Bounding container ball
gimbal_Ball_Diameter = 100;

//Height of all gimbal rings
gimbal_Ring_Height = 5;


//## GIMBAL JOINT SIZE VARIABLES ##//
//Diameter of skate bearings
gimbal_Skate_Bearing_Diameter = 10;

//Depth of skate bearings
gimbal_Skate_Bearing_Depth = 5;

//## GIMBAL SEPERATION (TOLERANCE) VARIABLES ##//
//Padding between interior of camera ball and first gimbal ring
tolerance_Gimbal_Ball_Pitch_seperation = 2; //mm

//Diagonal Padding between each edge of the camera and the edge of the mounting platform
tolerance_Gimbal_Yaw_Base_Padding = 0;

//Hole shrinkage stretch amount (in mm)
tolerance_Gimbal_Hole_Stretch = 0;

//Universal Fudge Number (to compensate for graphics card binary roundoff errors)
fudge = 0.01;


//## GIMBAL AXIS VARS ##//


//## PITCH ##//
//Pitch Ring Width
gimbal_Pitch_Ring_Width = 5;
//Pitch Ring Outer Diameter (taking tolerance into account)
gimbal_Pitch_Ring_Outer_Diameter = gimbal_Ball_Diameter - tolerance_Gimbal_Ball_Pitch_seperation;
//Pitch Ring Inner Diameter
gimbal_Pitch_Ring_Inner_Diameter = gimbal_Pitch_Ring_Outer_Diameter - 2*(gimbal_Pitch_Ring_Width);

//## ROLL ##//
//Roll Axle Diameter
gimbal_Roll_Isolation_Axle_Diameter = gimbal_Ring_Height;
//Roll Axle Length
gimbal_Roll_Isolation_Axle_Length = gimbal_Pitch_Ring_Inner_Diameter;

//## YAW ##//
//Yaw Base Diameter (diagonal footprint + padding)
gimbal_Yaw_Base_Diameter = tolerance_Gimbal_Yaw_Base_Padding + sqrt( pow(camera_Width, 2) + pow(camera_Depth, 2));
//Yaw Base Height (thickness)
gimbal_Yaw_Base_Height = gimbal_Ring_Height/2;

//## DUMMY CAMERA ##//
//Z Offset
camera_Offset_Z = -gimbal_Yaw_Base_Height-camera_Height/2;


// ## WING SIZE/SWEEP VARIABLES ## //

// Aircraft weight in grams. Is used to compute the needed wing area and wingspan
aircraft_Weight = 300;

// Maximum wing loading (grams/square mm)
// REF BASE: recommended wing loading for a powered trainer is 15oz/sq.ft. (0.004577 grams/sq. mm.) For a glider, 10oz/sq.ft. (0.003052 grams/sq. mm) 
// Taking the average, we get: 0.0038145 (grams/sq. mm). This is our max wing loading.
wing_Max_Loading = 0.003052;

// Target surface area of wing in mm^2
wing_Surface_Area = aircraft_Weight/wing_Max_Loading;

// Target wing sweep angle (degrees).
wing_Sweep_Angle = 4;

// Wing Target chord to wingspan ratio (Chord/Wingspan.) -> This will define how stable the pitching moment of the craft is.  
wing_Chord_to_Wingspan_Ratio = 1/4;

// Aerofoil Default Dimensions
aerofoil_Default_Chord = 1; // in mm

// Calculate the total localized wingspan of the aircraft. (I.E. Measuring the wing as a mirrored plank. No sweep.) -> This will be used for many later calculations
// Maths:
	// Surface Area (mm^2) = calculated chord (mm) * calculated wingspan(mm)
	// calculated chord = ratio * calculated wingspan
	// ratio * calculated wingspan^2 = surface area
	// calculated wingspan^2 = SA/ratio
	// calculated wingspan = sqrt(SA/ratio)
aerofoil_Plank_Wingspan = sqrt(wing_Surface_Area / wing_Chord_to_Wingspan_Ratio);

aerofoil_Target_Chord = aerofoil_Plank_Wingspan * wing_Chord_to_Wingspan_Ratio;
// ## MAIN FUNCTION ##//

module main(){
rough_Blueprint_Bus();
}

// #### GENERATOR FUNCTIONS #### //

// ### TEST ### //
module rough_Blueprint_All() {
//This will call the gimbal creator
rough_Blueprint_Gimbal();

//This will call the bus creator
rough_Blueprint_Bus();
}

module rough_Blueprint_Gimbal() {

//Make the enclosing ball
%sphere(gimbal_Ball_Diameter/2);

//Make the invisible camera
camera_Placeholder(camera_Height,
camera_Width,
camera_Depth,
camera_Lense_Depth,
camera_Lense_Diameter_1,
camera_Lense_Diameter_2,
offset_Z = camera_Offset_Z);

//Make the camera mounting base
camera_Base(
gimbal_Yaw_Base_Diameter,
gimbal_Yaw_Base_Height,
offset_Z = - gimbal_Yaw_Base_Height);

gimbal_Yaw_Isolation_Joint();
//TODO: Change this offset to a more accessible variable that also takes the joint separation into account. I.E. Allows for spacer bearings.
camera_Top_Counterweight(
gimbal_Yaw_Base_Diameter,
gimbal_Yaw_Base_Height,
offset_Z = gimbal_Yaw_Base_Height);
gimbal_Roll_Isolation_Axle(
gimbal_Roll_Isolation_Axle_Diameter,
gimbal_Roll_Isolation_Axle_Length
);
gimbal_Roll_Isolation_Joint();

gimbal_Pitch_Isolation_Ring(
gimbal_Pitch_Ring_Outer_Diameter,
gimbal_Pitch_Ring_Width,
gimbal_Ring_Height);

gimbal_Pitch_Isolation_Joint();

}

module rough_Blueprint_Bus() {
	
	make_Airfoil();
	
	// Make an invisible copy of the airfoil (for the left side of the plane)
	%mirror([1,0,0])
		make_Airfoil();
	
	// Debug stats
	print_Bus_Stats();

}


main();