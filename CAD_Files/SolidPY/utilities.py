#!/usr/bin/python
# Random Utilities
from __future__ import division
from SolidPy import *
import math

import config


# Makes an object insubstantial
def make_Insubstantial(self):
    self.Color
    
    
def extrude_Blank(Extrusion_Blank, extrusion_Radians = config.Wing.wing_Sweep_Radians, extrusion_Bounds = [0, config.Airfoil.global_Wingspan]):
    
    # Extrude the airfoil to 1/2 the wingspan (it will be mirrored later in a different function)
    
    # Use a for loop to create slices
    extrusion_Length = extrusion_Bounds[1] - extrusion_Bounds[0]
    
    slices = int(extrusion_Length / config.Wing.extrusion_Slice_Width)
    #DEBUG
    # print("slices %d" % slices)
    
    airfoil_Solid = None
    
    
    # Extrude and sweep the wing
    for i in range(0, slices):
        
        # Create a small slice of the wing.
        current_slice = Linear_extrude(Extrusion_Blank, height = config.Wing.extrusion_Slice_Width, center = False)
        
        #current_slice.translate([0,0,-config.aerofoil_Plank_Wingspan/2])
        
        # Rotate the airfoil (currently parrallel to the z axis), so that it is parallel to the x axis.
        current_slice.rotate([90,0,-90])
        
        # Move the slice so that it is on the other side of the y axis
        current_slice.translate([config.Wing.extrusion_Slice_Width, 0, 0])
        
        # Calculate for far along this slice will be placed on the x axis
        x_Offset = (i*config.Wing.extrusion_Slice_Width) + extrusion_Bounds[0]
        
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

# The class that will hold all of the functions necessary for making laserable parts of our model.
class Laser:
    
    def cut_Slices(cut_Spacing, start_Point, end_Point):
        pass
        