# Space project Gimbal creation OpenSCAD library.
# See www.thewinterland.net for more info
# Copyleft CC BY-SA 3.0 Winter Guerra, 2012.
# Github: github.com/xtremd

### Translation Vars ###

#Translated Wrapping Functions


module camera_Placeholder(
camera_Height,
camera_Width,
camera_Depth,
camera_Lense_Depth,
camera_Lense_Diameter_1,
camera_Lense_Diameter_2,
offset_X=0,
offset_Y=0,
offset_Z=0) {

#Allow for external position adjustments (to aid digital assembly)
translate([offset_X, offset_Y, offset_Z]) {

#Make one object
union() {

#Make fake camera body
cube([camera_Width, camera_Depth, camera_Height], center=true);

#Make lens
rotate ([90,0,0])
translate([0,0,-(camera_Depth/2)-(camera_Lense_Depth/2)])
cylinder(r1 = camera_Lense_Diameter_1, r2 = camera_Lense_Diameter_2, h = camera_Lense_Depth, center = true);

}
}
}

module camera_Base(
diameter,
height,
offset_X=0,
offset_Y=0,
offset_Z=0) {

#Assembly Offset
translate([offset_X, offset_Y, offset_Z]) {

#Make one obj
union() {
	
	cylinder(h=height, r=diameter/2, center=true);

}
}
}

module gimbal_Yaw_Isolation_Joint() {

}

module camera_Top_Counterweight(
diameter,
height,
offset_X=0,
offset_Y=0,
offset_Z=0) {

translate([offset_X, offset_Y, offset_Z]) {

#Make one obj
union() {
	
	cylinder(h=height, r=diameter/2, center=true);

}
}
}

module gimbal_Roll_Isolation_Axle(axle_Diameter,
axle_Length,
offset_X=0,
offset_Y=0,
offset_Z=0) {

#Center
translate([offset_X, offset_Y, offset_Z]) {

rotate([90,0,0])
cylinder(r=axle_Diameter/2, h = axle_Length, center=true);

}
}

module gimbal_Roll_Isolation_Joint() {

}

module gimbal_Pitch_Isolation_Ring(
ring_Diameter,
ring_Width,
ring_Height,
offset_X=0,
offset_Y=0,
offset_Z=0) {

#Center Part
translate([offset_X, offset_Y, offset_Z]) {

difference() {
#Outer solid Ring
cylinder(r=ring_Diameter/2, h=ring_Height, center=true);
#Inner difference ring
cylinder(r=(ring_Diameter/2)-ring_Width, h=ring_Height+fudge, center = true);
}
}
}


module gimbal_Pitch_Isolation_Joint() {

}
