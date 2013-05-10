#!/usr/bin/python
#Bus creation functions
from __future__ import division
from SolidPy import *
import math

import config


def make_Airfoil():
	
	# TODO: Make a for loop replacement for this line
	# Rotate the airfoil to show sweep
	# rotate([0,0,-wing_Sweep_Angle])
	
	
	# Make the airfoil
	airfoil = extrude_With_Sweep()
    
    # Cut the aileron holes
    
	
	# Move the airfoil forward so that it is centered
	
	return airfoil


def extrude_With_Sweep():
	
	# Extrude the airfoil to 1/2 the wingspan (it will be mirrored later, possibly in Blender.)
	
	
	# Import the airfoil outline
	airfoil_Blank = Polygon(points=config.airfoil_Points)
    	
    	# Resize airfoil chord to target chord.
    	airfoil_Blank.scale(config.aerofoil_Calculated_Chord, config.aerofoil_Calculated_Chord, 1)
    	
    	# Use a for loop to create slices
    	slices = int(config.global_Wingspan / config.extrusion_Slice_Width)
        #DEBUG
        # print("slices %d" % slices)
        
        airfoil_Solid = None
        
        for i in range(0, slices):
            
            current_slice = Linear_extrude(airfoil_Blank, height = config.extrusion_Slice_Width, center = True)
        	
        	#current_slice.translate([0,0,-config.aerofoil_Plank_Wingspan/2])
        	
        	# Rotate the airfoil (currently parrallel to the z axis), so that it is parallel to the x axis.
            current_slice.rotate([90,0,-90])
            
            x_Offset = i*config.extrusion_Slice_Width
            
            # Maths:
            # y = -(h*sin(pheta))
            # x = h*cos(pheta)
            # h = (-x)/(cos(pheta))
            # y = ((-x)/cos(pheta)) * sin(pheta)
            hyp = ((-x_Offset) / math.cos(config.wing_Sweep_Angle))
            y_Offset = (hyp * math.sin(config.wing_Sweep_Angle))
            
            current_slice.translate(x_Offset, y_Offset, 0)
            
            if (i == 0):
                airfoil_Solid = current_slice
            else:
                airfoil_Solid = airfoil_Solid + current_slice
        
        
        
        # TODO: Fix this using a for loop. Does not extrude properly.
    	# Extrude
    	#airfoil_Solid = Linear_extrude(airfoil_Blank, height = config.aerofoil_Plank_Wingspan / 2, center = False)
        
        return airfoil_Solid

def print_Bus_Stats():
	# Print out debugging information (measurements and such)
	print("Wing Sweep Radians:")
	print(config.wing_Sweep_Angle)
	
	print("Weight of Airplane")
	print(config.aircraft_Weight)
	
	print("Plank Wingspan:")
	print(config.aerofoil_Plank_Wingspan)
	
	print("Surface Area of Wing:")
	print(config.wing_Surface_Area)
	
	print("Calculated Chord:")
	print(config.aerofoil_Calculated_Chord)
	
	print("Calculated Plank Wingspan:")
	print(config.aerofoil_Plank_Wingspan)
	