#########################################################################################

# This file runs Blender background scripts to aid in increasing the parametricity of the spacecraft being designed in this project.
# Every time some object in the scene changes, all of the scripts are called again to make sure that all objects are fiting/generating like they should.

# Copyleft Winter J. Guerra (XtremD), CC-BY-SA 3.0. 
# https://creativecommons.org/licenses/by-sa/3.0/

# Project page: https://github.com/xtremd/space_project 

##########################################################################################


# Get Blender functions and object data
import bpy

# This next line makes the handler triggers persistent across file reloads.
# Since this script is project-specific and not globally useful as an addon, this line is disabled in this instance.
# from bpy.app.handlers import persistent

# Note: In blender, self is usually named 'scene'
# TODO: Find out why passing 'self' does not work. Is it implied?


# Import other needed function libraries

# TODO: Import mathutils vector class


class aileronDiffAlignmentOperator(bpy.types.PropertyGroup):
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
        
        print("Running: background_scripts.aileron_diff_aligner")
        
        # Get the objects that we are going to be using
        wing_Spline_Object = bpy.data.curves[aileronDiffAlignmentOperator.wing_Spline_Object_Name]
        aileron_Diff_Template_Object = bpy.data.objects[aileronDiffAlignmentOperator.aileron_Difference_Object_Name]
        
        # Find wing alignment vector
        vector = aileronDiffAlignmentOperator.find_Object_Mean_Vector(scene, wing_Spline_Object)
        
        # Align aileron template to vector
        aileronDiffAlignmentOperator.set_Aileron_Difference_Template_Vector(scene, aileron_Diff_Template_Object, vector)
        
        print("Done.")
        
        return {'FINISHED'}
        
    def find_Object_Mean_Vector(scene, object):
        # Finds the average global vector of the airfoil's sweep given the airfoil's guiding object (of type curve)
        # Method: Uses the first and last control point of the guiding curve to find the average object vector. 
        # Assumes: The curve object has the "endpoint" property checked. (AKA: Is anchored to its endpoints.) 
        
        # TODO: Function still needs to be written 
        
        # TODO: Should return a vector (a mathutils object)
        vector = 0
        return vector
    
    def set_Aileron_Difference_Template_Vector(scene, aileron_Diff_Object, vector):
        for i in range(0,2):
            aileron_Diff_Object.rotation_axis_angle[i] = 0
            
        return

# This should be handled by the controller -> background_Geometric_Generator_Script_Controller

#
#def register():
#    bpy.utils.register_class(aileronDiffAlignmentOperator)
#    #Register as a function that updates every time something has changed.
#
# # To be handled by update script   
#    bpy.app.handlers.scene_update_post.append(aileronDiffAlignmentOperator.execute)
#    
#def unregister():
#    bpy.app.handlers.scene_update_post.delete(aileronDiffAlignmentOperator.execute)
#    bpy.utils.unregister_class(aileronDiffAlignmentOperator)
#    
    

if __name__ == "__main__":
    register()