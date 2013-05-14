#!/usr/bin/python
#Bus creation functions
from __future__ import division
from SolidPy import *
import math

import config
import utilities

# Takes in a integer arg for the wing bend.
# '1' = left wing, '-1' = right wing, '0' = flat wing (Plank'd for ease of printing)
def make_Wing(wing_Side = 'Right'):
    
    # Prep the airfoil blank
    airfoil_Blank = Polygon(points=config.Airfoil.airfoil_Points)
    
    # Resize airfoil chord to target chord.
    airfoil_Blank.scale(config.Airfoil.aerofoil_Calculated_Chord, config.Airfoil.aerofoil_Calculated_Chord, 1)
    
    # Make the airfoil
    airfoil = utilities.extrude_Blank(airfoil_Blank)
    
    # Cut the aileron holes
    diff_Aileron(airfoil)
    
    # Tilt and mirror the wing
    if (wing_Side == 'Right'):
        # Tilt the airfoil
        rotation_Angle = (-1) * config.Wing.wing_Bend_Angle
        airfoil.rotate(0, rotation_Angle, 0)
    else:
        # Rotate the airfoil in the opposide direction
        rotation_Angle = (-1) * config.Wing.wing_Bend_Angle
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

    
# Makes the Aileron object, not to be confused with the hole cut out to make space for the aileron
def make_Aileron():
    
    return object

# Cut the hole    
def diff_Aileron(airfoil):
    
    # Make the cutting blank
    # Make a square.
    blank = Polygon(points=config.Aileron.aileron_Blank_Points)
    
    # Rotate it so that it is parallel to the direction of the aircraft
    blank.rotate(90,90,0)
    
    # Scale it to the appropriate size
    # Maths:
        # For ever mm of chord, the max thickness of the wing is 0.1mm.
        # Therefore, the aileron thickness should be at least 0.2 times the chord, and the length can be however long we want.
    #blank.scale()
    
    # Extrude the blank so that we can use it as a differencing object
    blank = utilities.extrude_Blank(blank, extrusion_Bounds = config.Aileron.aileron_Bounds)
    
    return airfoil

def print_Bus_Stats():
    # Print out debugging information (measurements and such)
    print("Wing Sweep Angle: %d" % config.Wing.wing_Sweep_Angle )
    
    print("Weight of Airplane %d" % config.Aircraft.aircraft_Weight)
    
    print("Plank Wingspan: %d" % config.Airfoil.aerofoil_Plank_Wingspan)
    
    print("Surface Area of Wing: %d" % config.Wing.wing_Surface_Area)
    
    print("Calculated Chord: %d" % config.Airfoil.aerofoil_Calculated_Chord)
    
    print("Calculated Plank Wingspan: %d" % config.Airfoil.aerofoil_Plank_Wingspan)
    