//Bus creation functions


module make_Airfoil() {
	
	// TODO: Make a for loop replacement for this line
	// Rotate the airfoil to show sweep
	// rotate([0,0,-wing_Sweep_Angle])
	
	// Rotate the airfoil (currently parrallel to the z axis), so that it is parallel to the x axis.
	rotate([90,0,-90])
	
	//Orient the airfoil so that it is in quadrant 1
	translate([0,0,-aerofoil_Plank_Wingspan/2])
	
	
	extrude_With_Sweep();
	
	
}

module extrude_With_Sweep() {
	
	// Extrude the airfoil to 1/2 the wingspan (it will be mirrored later, possibly in Blender.) 
	
	// Use a for loop to create slices
	slices = global_Wingspan / extrusion_Slices_Per_Mm;
	//for (i = [0:slices]) {
	//	
	//}
	
	// Placeholder. Does not extrude perpendicular to YZ plane.
	linear_extrude(height = aerofoil_Plank_Wingspan / 2, center = false){

		
	// Resize airfoil chord to target chord.
	scale([aerofoil_Calculated_Chord, aerofoil_Calculated_Chord,1])
	// Import the airfoil outline
	polygon(points=[
		[1.00000, 0.00000],
		[0.99669, 0.00104],
		[0.98737, 0.00422],
		[0.97312, 0.00916],
		[0.95431, 0.01501],
		[0.93081, 0.02139],
		[0.90279, 0.02833],
		[0.87072, 0.03576],
		[0.83508, 0.04344],
		[0.79626, 0.05105],
		[0.75457, 0.05841],
		[0.71040, 0.06544],
		[0.66430, 0.07207],
		[0.61682, 0.07813],
		[0.56852, 0.08344],
		[0.51991, 0.08776],
		[0.47142, 0.09093],
		[0.42346, 0.09281],
		[0.37645, 0.09332],
		[0.33076, 0.09241],
		[0.28674, 0.09008],
		[0.24474, 0.08639],
		[0.20510, 0.08142],
		[0.16816, 0.07532],
		[0.13424, 0.06822],
		[0.10365, 0.06028],
		[0.07665, 0.05168],
		[0.05349, 0.04258],
		[0.03434, 0.03321],
		[0.01934, 0.02379],
		[0.00856, 0.01465],
		[0.00210, 0.00619],
		[0.00005, -0.00086],
		[0.00360, -0.00632],
		[0.01326, -0.01087],
		[0.02830, -0.01475],
		[0.04858, -0.01784],
		[0.07390, -0.02011],
		[0.10406, -0.02161],
		[0.13874, -0.02236],
		[0.17759, -0.02245],
		[0.22017, -0.02193],
		[0.26599, -0.02086],
		[0.31449, -0.01928],
		[0.36508, -0.01721],
		[0.41714, -0.01453],
		[0.47030, -0.01100],
		[0.52450, -0.00678],
		[0.57932, -0.00245],
		[0.63400, 0.00155],
		[0.68770, 0.00495],
		[0.73959, 0.00756],
		[0.78883, 0.00923],
		[0.83461, 0.00994],
		[0.87612, 0.00970],
		[0.91265, 0.00862],
		[0.94352, 0.00684],
		[0.96809, 0.00461],
		[0.98582, 0.00235],
		[0.99646, 0.00065]
		]);
		
	
	}
}



module print_Bus_Stats() {
	// Print out debugging information (measurements and such)
	echo("Weight of Airplane");
	echo(aircraft_Weight);
	
	echo("Surface Area of Wing:");
	echo(wing_Surface_Area);
	
	echo("Calculated Chord:");
	echo(aerofoil_Calculated_Chord);
	
	echo("Calculated Plank Wingspan:");
	echo(aerofoil_Plank_Wingspan);
	
}