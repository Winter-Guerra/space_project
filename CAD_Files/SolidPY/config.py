#!/usr/bin/python

# All GLOBAL configuration values should go here
from __future__ import division
from SolidPy import *
import math

# Adjust Rendering Settings
# May have to set these individually instead
#$fn=100

# ## BUS SIZE VARIABLES ## #

class Camera:

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

class Gimbal:
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
    gimbal_Yaw_Base_Diameter = tolerance_Gimbal_Yaw_Base_Padding + math.sqrt( math.pow(Camera.camera_Width, 2) + math.pow(Camera.camera_Depth, 2))
    #Yaw Base Height (thickness)
    gimbal_Yaw_Base_Height = gimbal_Ring_Height/2
    
    ### DUMMY CAMERA ###
    #Z Offset
    camera_Offset_Z = -gimbal_Yaw_Base_Height - Camera.camera_Height/2



class Aircraft:

    # Aircraft weight in grams. Is used to compute the needed wing area and wingspan
    aircraft_Weight = 300



# ## WING SIZE/SWEEP VARIABLES ## #

class Wing:
    
    # Maximum wing loading (grams/square mm)
    # REF BASE: recommended wing loading for a math.powered trainer is 15oz/sq.ft. (0.004577 grams/sq. mm.) For a glider, 10oz/sq.ft. (0.003052 grams/sq. mm)
    # Taking the average, we get: 0.0038145 (grams/sq. mm). This is our max wing loading.
    wing_Max_Loading = 0.003052

    # Target surface area of wing in mm^2
    wing_Surface_Area = Aircraft.aircraft_Weight / wing_Max_Loading

    # Target wing sweep angle (degrees).
    wing_Sweep_Angle = 4
    # Radians
    wing_Sweep_Radians = math.radians(wing_Sweep_Angle)

    # The center crease angle (measured from the horizontal) in degrees
    wing_Bend_Angle = 4
    # Radians
    wing_Bend_Radians = math.radians(wing_Bend_Angle)

    # Wing Target chord to wingspan ratio (Chord/Wingspan.) -> This will define how stable the pitching moment of the craft is.
    wing_Chord_to_Wingspan_Ratio = 1/4
    
    # Extrusion slice width in mm. Also defines the resolution of the slices.
    extrusion_Slice_Width = 10

class Airfoil( Wing ):

    # Aerofoil Default Dimensions
    aerofoil_Default_Chord = 1 # in mm

    # Calculate the total localized wingspan of the aircraft. (I.E. Measuring the wing as a mirrored plank. No sweep.) -> This will be used for many later calculations
    # Maths:
        # Surface Area (mm^2) = calculated chord (mm) * calculated wingspan(mm)
        # calculated chord = ratio * calculated wingspan
        # ratio * calculated wingspan^2 = surface area
        # calculated wingspan^2 = SA/ratio
        # calculated wingspan = math.sqrt(SA/ratio)
    aerofoil_Plank_Wingspan = math.sqrt( Wing.wing_Surface_Area / Wing.wing_Chord_to_Wingspan_Ratio )

    aerofoil_Calculated_Chord = aerofoil_Plank_Wingspan * Wing.wing_Chord_to_Wingspan_Ratio
    
    # The global wingspan of the airfoil
    # Maths: I want the math.sin
    # hyp = local wingspan
    # local wingpspan = hyp * cos
    # wingspan/cos = hyp = global wingspan
    global_Wingspan = aerofoil_Plank_Wingspan / (math.cos(Wing.wing_Sweep_Radians))
    
    airfoil_Points = [
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
            [0.99646, 0.00065]]

class Aileron( Wing ):
    
    aileron_Blank_Points = [
            [0,0],
            [0,1],
            [1,1],
            [1,0] ]
            
    # Make the Ailerons 50% of the wing,
    aileron_Bounds = [0.25*(Airfoil.global_Wingspan), 0.75*(Airfoil.global_Wingspan)]


    

