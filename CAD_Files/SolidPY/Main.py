#!/usr/bin/python
from __future__ import division
from SolidPy import *
import math

import config

import bus
#import gimbal



# #### GENERATOR FUNCTIONS #### #

# ### TEST ### #
def rough_Blueprint_All():
    #This will call the gimbal creator
    rough_Blueprint_Gimbal()
    
    #This will call the bus creator
    rough_Blueprint_Bus()


def rough_Blueprint_Gimbal():
    
    #Make the enclosing ball
    enclosing_Ball = sphere(gimbal_Ball_Diameter/2).color('red', 0.2)
    
    #Make the invisible camera
    camera_Placeholder(camera_Height,
    camera_Width,
    camera_Depth,
    camera_Lense_Depth,
    camera_Lense_Diameter_1,
    camera_Lense_Diameter_2,
    offset_Z = camera_Offset_Z)
    
    #Make the camera mounting base
    camera_Base(
    gimbal_Yaw_Base_Diameter,
    gimbal_Yaw_Base_Height,
    offset_Z = - gimbal_Yaw_Base_Height)
    
    gimbal_Yaw_Isolation_Joint()
    #TODO: Change this offset to a more accessible variable that also takes the joint separation into account. I.E. Allows for spacer bearings.
    camera_Top_Counterweight(
    gimbal_Yaw_Base_Diameter,
    gimbal_Yaw_Base_Height,
    offset_Z = gimbal_Yaw_Base_Height)
    gimbal_Roll_Isolation_Axle(
    gimbal_Roll_Isolation_Axle_Diameter,
    gimbal_Roll_Isolation_Axle_Length
    )
    gimbal_Roll_Isolation_Joint()
    
    gimbal_Pitch_Isolation_Ring(
    gimbal_Pitch_Ring_Outer_Diameter,
    gimbal_Pitch_Ring_Width,
    gimbal_Ring_Height)
    
    gimbal_Pitch_Isolation_Joint()

def rough_Blueprint_Bus():
    
    airfoil = bus.make_Airfoil()
    
    # Make an invisible copy of the airfoil (for the left side of the plane)
    airfoil_Mirror = airfoil.copy()
    
    airfoil_Mirror.mirror([1,0,0])
    airfoil_Mirror.color('red',0.2)
    
    __bus = airfoil + airfoil_Mirror
    # Debug stats
    bus.print_Bus_Stats()

    # TODO: Make it return!!
    return __bus


def main():
    Assembly = rough_Blueprint_Bus()
    
    writeSCADfile('Main.scad', Assembly)

if __name__ == '__main__':
	main()