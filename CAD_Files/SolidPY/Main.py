#!/usr/bin/python
from __future__ import division
from SolidPy import *
import math

#import "bus_Fuctions.py"
#import "gimbal_Functions.py"

# Adjust Rendering Settings
# May have to set these individually instead
#$fn=100

# ## BUS SIZE VARIABLES ## #


### CAMERA SIZE VARIABLES ###
#Dimensions of the camera
#Assumes that the x axis of the camera is the sensor's x axis.
camera_Height = 20 #mm
camera_Width = 20 #
camera_Depth = 20 #
camera_Lense_Depth = 10
camera_Lense_Diameter_1 = 10
camera_Lense_Diameter_2 = 3


### GLOBAL GIMBAL SIZE VARIBALES ###
#Bounding container ball
gimbal_Ball_Diameter = 100

#Height of all gimbal rings
gimbal_Ring_Height = 5


### GIMBAL JOINT SIZE VARIABLES ###
#Diameter of skate bearings
gimbal_Skate_Bearing_Diameter = 10

#Depth of skate bearings
gimbal_Skate_Bearing_Depth = 5

### GIMBAL SEPERATION (TOLERANCE) VARIABLES ###
#Padding between interior of camera ball and first gimbal ring
tolerance_Gimbal_Ball_Pitch_seperation = 2 #mm

#Diagonal Padding between each edge of the camera and the edge of the mounting platform
tolerance_Gimbal_Yaw_Base_Padding = 0

#Hole shrinkage stretch amount (in mm)
tolerance_Gimbal_Hole_Stretch = 0

#Universal Fudge Number (to compensate for graphics card binary roundoff errors)
fudge = 0.01


### GIMBAL AXIS VARS ###


### PITCH ###
#Pitch Ring Width
gimbal_Pitch_Ring_Width = 5
#Pitch Ring Outer Diameter (taking tolerance into account)
gimbal_Pitch_Ring_Outer_Diameter = gimbal_Ball_Diameter - tolerance_Gimbal_Ball_Pitch_seperation
#Pitch Ring Inner Diameter
gimbal_Pitch_Ring_Inner_Diameter = gimbal_Pitch_Ring_Outer_Diameter - 2*(gimbal_Pitch_Ring_Width)

### ROLL ###
#Roll Axle Diameter
gimbal_Roll_Isolation_Axle_Diameter = gimbal_Ring_Height
#Roll Axle Length
gimbal_Roll_Isolation_Axle_Length = gimbal_Pitch_Ring_Inner_Diameter

### YAW ###
#Yaw Base Diameter (diagonal footprint + padding)
gimbal_Yaw_Base_Diameter = tolerance_Gimbal_Yaw_Base_Padding + math.sqrt( math.pow(camera_Width, 2) + math.pow(camera_Depth, 2))
#Yaw Base Height (thickness)
gimbal_Yaw_Base_Height = gimbal_Ring_Height/2

### DUMMY CAMERA ###
#Z Offset
camera_Offset_Z = -gimbal_Yaw_Base_Height-camera_Height/2


# ## WING SIZE/SWEEP VARIABLES ## #

# Aircraft weight in grams. Is used to compute the needed wing area and wingspan
aircraft_Weight = 300

# Maximum wing loading (grams/square mm)
# REF BASE: recommended wing loading for a math.powered trainer is 15oz/sq.ft. (0.004577 grams/sq. mm.) For a glider, 10oz/sq.ft. (0.003052 grams/sq. mm) 
# Taking the average, we get: 0.0038145 (grams/sq. mm). This is our max wing loading.
wing_Max_Loading = 0.003052

# Target surface area of wing in mm^2
wing_Surface_Area = aircraft_Weight/wing_Max_Loading

# Target wing sweep angle (degrees).
wing_Sweep_Angle = 4

# Wing Target chord to wingspan ratio (Chord/Wingspan.) -> This will define how stable the pitching moment of the craft is.  
wing_Chord_to_Wingspan_Ratio = 1/4

# Aerofoil Default Dimensions
aerofoil_Default_Chord = 1 # in mm

# Calculate the total localized wingspan of the aircraft. (I.E. Measuring the wing as a mirrored plank. No sweep.) -> This will be used for many later calculations
# Maths:
	# Surface Area (mm^2) = calculated chord (mm) * calculated wingspan(mm)
	# calculated chord = ratio * calculated wingspan
	# ratio * calculated wingspan^2 = surface area
	# calculated wingspan^2 = SA/ratio
	# calculated wingspan = math.sqrt(SA/ratio)
aerofoil_Plank_Wingspan = math.sqrt(wing_Surface_Area / wing_Chord_to_Wingspan_Ratio)

aerofoil_Calculated_Chord = aerofoil_Plank_Wingspan * wing_Chord_to_Wingspan_Ratio

# Extrusion slices per mm (resolution)
extrusion_Slices_Per_Mm = 1

# The global wingspan of the airfoil
# Maths: I want the math.sin
# math.sin = opp/hyp
# hyp*math.sin = opp
global_Wingspan = aerofoil_Plank_Wingspan * math.sin(wing_Sweep_Angle) 



def main():
    
    
    
    Assembly=Cylinder(h=10,r=5)
    writeSCADfile('Main.scad',Assembly)

if __name__ == '__main__':
	main()