#!/usr/bin/python
#Bus creation functions
from __future__ import division
from SolidPy import *
import math

import config

# Takes in a integer arg for the wing bend.
# '1' = left wing, '-1' = right wing, '0' = flat wing (Plank'd for ease of printing)
def make_Wing(wing_Side = 'Right'):
    
    # Prep the airfoil blank
    airfoil_Blank = Polygon(points=config.airfoil_Points)
    
    # Resize airfoil chord to target chord.
    airfoil_Blank.scale(config.aerofoil_Calculated_Chord, config.aerofoil_Calculated_Chord, 1)
    
    # Make the airfoil
    airfoil = extrude_Blank(airfoil_Blank)
    
    # Cut the aileron holes
    
    # Tilt and mirror the wing
    if (wing_Side == 'Right'):
        # Tilt the airfoil
        rotation_Angle = (-1) * config.wing_Bend_Angle
        airfoil.rotate(0, rotation_Angle, 0)
    else:
        # Rotate the airfoil in the opposide direction
        rotation_Angle = (-1) * config.wing_Bend_Angle
        airfoil.rotate(0, rotation_Angle, 0)
        # Mirror the airfoil
        airfoil.mirror([1,0,0])
        
    return airfoil

def make_Wing_Right():
    
    wing_Segment = make_Wing('Right')
    
    return wing_Segment

def make_Wing_Left():
    
    wing_Segment = make_Wing('Left')
    
    return wing_Segment


def extrude_Blank(Extrusion_Blank, extrusion_Radians = config.wing_Sweep_Radians, extrusion_Length = config.global_Wingspan):
    
    # Extrude the airfoil to 1/2 the wingspan (it will be mirrored later in a different function)
    
    # Use a for loop to create slices
    slices = int(extrusion_Length / config.extrusion_Slice_Width)
    #DEBUG
    # print("slices %d" % slices)
    
    airfoil_Solid = None
    
    
    # Extrude and sweep the wing
    for i in range(0, slices):
        
        # Create a small slice of the wing.
        current_slice = Linear_extrude(Extrusion_Blank, height = config.extrusion_Slice_Width, center = False)
        
        #current_slice.translate([0,0,-config.aerofoil_Plank_Wingspan/2])
        
        # Rotate the airfoil (currently parrallel to the z axis), so that it is parallel to the x axis.
        current_slice.rotate([90,0,-90])
        
        # Move the slice so that it is on the other side of the y axis
        current_slice.translate([config.extrusion_Slice_Width, 0, 0])
        
        # Calculate for far along this slice will be placed on the x axis
        x_Offset = i*config.extrusion_Slice_Width
        
        # Calculate the hyp of the right triangle that this slice must traverse along to maintain the correct sweep angle
        # Maths:
        # y = -(h*sin(pheta))
        # x = h*cos(pheta)
        # h = (-x)/(cos(pheta))
        # y = ((-x)/cos(pheta)) * sin(pheta)
        hyp = ((-x_Offset) / math.cos(extrusion_Radians))
        
        # Calculate the y location where this slice must be placed to maintain the correct sweep angle.
        y_Offset = (hyp * math.sin(extrusion_Radians))
        
        # Place the slice
        current_slice.translate(x_Offset, y_Offset, 0)
        
        # Union this slice with the previously made slice. 
        # If this is the first slice to be made, don't try to union yet.
        if (i == 0):
            airfoil_Solid = current_slice
        else:
            airfoil_Solid = airfoil_Solid + current_slice
    
    
    return airfoil_Solid

def print_Bus_Stats():
    # Print out debugging information (measurements and such)
    print("Wing Sweep Angle:")
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
    