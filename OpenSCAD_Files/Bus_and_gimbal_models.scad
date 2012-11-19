// Space project Bus and Gimbal creation OpenSCAD script.
// See www.thewinterland.net for more info
// Copyleft CC BY-SA 3.0 Winter Guerra, 2012.
// Github: github.com/xtremd

//Import Bus and Gimbal libraries
use <gimbal_Functions.scad>;
use <bus_Functions.scad>;

//## BUS SIZE VARIABLES ##//


//## CAMERA SIZE VARIABLES ##//
//Dimensions of the camera
//Assumes that the x axis of the camera is the sensor's x axis.
camera_Height = 20; //mm
camera_Width = 20; //
camera_Depth = 40; //
camera_Lense_Depth = 10;
camera_Lense_Diameter_1 = 10;
camera_Lense_Diameter_2 = 3;


//## GIMBAL SIZE VARIBALES ##//
//Bounding container ball
gimbal_Ball_Diameter = 100;


//## GIMBAL JOINT SIZE VARIABLES ##//
//Diameter of skate bearings
gimbal_Skate_Bearing_Diameter = 10;

//Depth of skate bearings
gimbal_Skate_Bearing_Depth = 5;

//## GIMBAL SEPERATION (TOLERANCE) VARIABLES ##//
//Padding between interior of camera ball and first gimbal ring
tolerance_Gimbal_Ball_Pitch_seperation = 10; //mm

//Diagonal Padding between each edge of the camera and the edge of the mounting platform
tolerance_Gimbal_Yaw_Base_Padding = 0;

//Hole shrinkage stretch amount (in mm)
tolerance_Gimbal_Hole_Stretch = 0;



//## GIMBAL AXIS VARS ##//

//## PITCH ##//
//Pitch Ring Width
gimbal_Pitch_Ring_Width = 10;

//## ROLL ##//
//Roll Axle Diameter
gimbal_Roll_Axle_Diameter = 10;

//## YAW ##//
//Yaw Base Diameter (diagonal footprint + padding)
gimbal_Yaw_Base_Diameter = tolerance_Gimbal_Yaw_Base_Padding + sqrt( pow(camera_Width, 2) + pow(camera_Depth, 2));

//Yaw Base Height (thickness)
gimbal_Yaw_Base_Height = 3;

//#### GENERATOR FUNCTIONS ####//

//### TEST ###//
module rough_Blueprint_All() {
//This will call the gimbal creator
rough_Blueprint_Gimbal();

//This will call the bus creator
rough_Blueprint_Bus();
}

module rough_Blueprint_Gimbal() {
//Make the enclosing ball
*sphere(gimbal_Ball_Diameter/2);

//Make the invisible camera
%camera_Placeholder(camera_Height, camera_Width, camera_Depth, camera_Lense_Depth, camera_Lense_Diameter_1, camera_Lense_Diameter_2);

//Make the invisible camera mounting base
camera_Base(gimbal_Yaw_Base_Diameter, gimbal_Yaw_Base_Height, print=false);
gimbal_Yaw_Isolation_Joint();
camera_Top_Counterweight();
gimbal_Roll_Isolation_Axle();
gimbal_Roll_Isolation_Joint();
gimbal_Pitch_Isolation_Ring();
gimbal_Pitch_Isolation_Joints();

}



module rough_Blueprint_Bus() {

}

rough_Blueprint_All();
