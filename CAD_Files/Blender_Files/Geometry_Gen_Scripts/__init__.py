#########################################################################################

# This file runs Blender background scripts to aid in increasing the parametricity of the spacecraft being designed in this project.
# Every time some object in the scene changes, all of the scripts are called again to make sure that all objects are fiting/generating like they should.

# Copyleft Winter J. Guerra (XtremD), CC-BY-SA 3.0. 
# https://creativecommons.org/licenses/by-sa/3.0/

# Project page: https://github.com/xtremd/space_project 

##########################################################################################


bl_info = {
    "name": "Flying Wing UAV Scripts",
    "description": "Solidifies airfoil designs modeled using curves then applies various parametric scripts to cut out slots for ailerons, batteries, servos, etc.",
    "author": "Winter J. Guerra (XtremD)",
    "version": (0, 1, 0),
    "blender": (2, 62, 1),
    "location": "Runs in Background",
    "warning": "Project Specific!",
    # Place github url here
    "wiki_url": "",
    "tracker_url": "",
    "category": "User"}

#if "bpy" in locals():
#    import imp
#    imp.reload(aileronDiffAlignmentOperator.py)
#else:
#    from . import aileronDiffAlignmentOperator.py

# Get Blender functions and object data
import sys
import os
import bpy

# This next line makes the handler triggers persistent across file reloads.
# Since this script is project-specific and not globally useful as an addon, this line is disabled in this instance.
# from bpy.app.handlers import persistent

#def __init__(self):
#        return self

class aileronDiffAlignmentOperator(bpy.types.Operator):

        # The bl_idname must be all lowercase!
    bl_idname = "background_scripts.aileron_diff_aligner"
    bl_label = "Aileron Diff Alignment Script"

    # Aileron boolean difference object name (Default: 'Aileron_Boolean_Difference')
    # TODO: Should be made into a variable controllable through a setting panel, not just code.
    aileron_Difference_Object_Name = 'Aileron_Boolean_Difference'
    wing_Spline_Object_Name = 'Shape_Guide_Nurbs_Curve'

    def execute(scene):

        # This function is not supposed to be attached to the 'bpy.app.handlers.scene_update_post' handler, it has no way to check if the scene data has changed and therefore will needlessly consume much processing power.
        # Instead, this function will be called by the

        # Get the objects that we are going to be using
        # TODO: Change these to reference the object directly! (ATM they seem to be making new copies of the objects.)
            # I.E. Symptoms are that passing this obj directly into the vector setter function does not work.
        wing_Spline_Object = bpy.data.curves[aileronDiffAlignmentOperator.wing_Spline_Object_Name]
        aileron_Diff_Template_Object = bpy.data.objects[aileronDiffAlignmentOperator.aileron_Difference_Object_Name]

        # Find wing alignment vector
        vector = aileronDiffAlignmentOperator.find_Object_Mean_Vector(scene, wing_Spline_Object)

        # Align aileron template to vector
        #aileronDiffAlignmentOperator.set_Aileron_Difference_Template_Vector(scene, aileronDiffAlignmentOperator.aileron_Difference_Object_Name, vector)
        aileronDiffAlignmentOperator.set_Aileron_Difference_Template_Vector(scene, aileron_Diff_Template_Object, vector)

        print("Done.")

        return {'FINISHED'}

    def find_Object_Mean_Vector(scene, object):
        # Finds the average global vector of the airfoil's sweep given the airfoil's guiding object (of type curve)
        # Method: Uses the first and last control point of the guiding curve to find the average object vector. 
        # Assumes: The curve object has the "endpoint" property checked. (AKA: Is anchored to its endpoints.) 
        # TODO: Function still needs to be written 

        # NOTE: vector is [x,y,z]
        vector = [0,0,0]
        return vector

    def set_Aileron_Difference_Template_Vector(scene, object, vector):
        # Set object rotation mode to axis angle
        # @Deprecated
        # object.rotation_mode = 'AXIS_ANGLE'
    
        for i in range(0,2):
            # Set the axis bits for the rotation function (constraints)
            axis = []
            axis[i] = 1
            
                
                
            bpy.ops.transform.rotate(value=vector[i], axis=axis, constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=True)
            object.rotation_axis_angle[i] = vector[i]
            # bpy.data.objects[object_Name].rotation_axis_angle[i] = vector[i]
            # bpy.data.objects[Aileron_Boolean_Difference].rotation_axis_angle[0,0,0] = vector[i]
        return
        

class geometric_generator_script_controller(bpy.types.Operator):
    #
        

    # The bl_idname must be all lowercase!
    bl_idname = "background_scripts.aileron_diff_aligner"
    bl_label = "Aileron Diff Alignment Script"


    #class_Run_List = [aileronDiffAlignmentOperator]

    def scene_update(scene):
        # To disable this script (say, for testing/demonstration purposes) Set the next line to "false"
        run_Script = False
        
        if run_Script == True:
            if bpy.data.objects.is_updated:
                print("Changes in scenery detected: Poking scripts")
                
                # Backup the currently selected object (in case it is changed by later scripts)
                
                
                print("Running: background_scripts.aileron_diff_aligner")
                aileronDiffAlignmentOperator.execute(scene)
        
        
        return {'FINISHED'}


def register():
    bpy.utils.register_class(geometric_generator_script_controller)
    #Register as a function that updates every time something has changed.
    bpy.app.handlers.scene_update_post.append(geometric_generator_script_controller.scene_update)
    pass
    
def unregister():
    bpy.app.handlers.scene_update_post.remove(geometric_generator_script_controller.scene_update)
    bpy.utils.unregister_class(geometric_generator_script_controller)
    pass
    

if __name__ == "__main__":
    register()

