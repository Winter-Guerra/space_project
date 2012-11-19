//Gimbal Creation Script

//## Translation Vars ##//


module camera_Placeholder(camera_Height, camera_Width, camera_Depth, camera_Lense_Depth, camera_Lense_Diameter_1, camera_Lense_Diameter_2) {

cube([camera_Width, camera_Depth, camera_Height], center=true);

rotate ([90,0,0])
translate([0,0,-(camera_Depth/2)-(camera_Lense_Depth/2)])
cylinder(r1 = camera_Lense_Diameter_1, r2 = camera_Lense_Diameter_2, h = camera_Lense_Depth, center = true);

}

module camera_Base(diameter,height,print = false) {
	if (print == false) {
	assert()
	}

	translate([0,0,0])
	cylinder(h=height, r=diameter/2, center=true);
}

module gimbal_Yaw_Isolation_Joint() {

}

module camera_Top_Counterweight() {

}

module gimbal_Roll_Isolation_Axle() {

}

module gimbal_Roll_Isolation_Joint() {

}

module gimbal_Pitch_Isolation_Ring() {

}

module gimbal_Pitch_Isolation_Joints() {

}

module demo() {
}

demo();
