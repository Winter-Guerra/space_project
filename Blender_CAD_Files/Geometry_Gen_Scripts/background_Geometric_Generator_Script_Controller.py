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


# Import other modular generator scripts
# Script for cutting out the aileron slots
# import aileron_Diff_Alignment_Background_Script.py

class background_Geometric_Generator_Script_Controller(bpy.types.PropertyGroup):
    # The bl_idname must be all lowercase!
    bl_idname = "background_scripts.aileron_diff_aligner"
    bl_label = "Aileron Diff Alignment Script"

    def scene_update(context):
        if bpy.data.objects.is_updated:
            print("Changes in scenery detected:")
            for ob in bpy.data.objects:
                if ob.is_updated:
                    print("=>", ob.name)
        
        print("Running background scripts: Aileron Diff Alignment Script")
        
        # Find wing alignment vector
        
        # Align aileron template to vector
        
            for i in range(0,2):
                bpy.data.objects['Aileron_Boolean_Difference'].rotation_axis_angle[i] = 0
        
        return {'FINISHED'}

def register():
    bpy.utils.register_class(aileronDiffAlignmentOperator)
    #Register as a function that updates every time something has changed.
    bpy.app.handlers.scene_update_post.append(aileronDiffAlignmentOperator.scene_update)
    
    

if __name__ == "__main__":
    register()

# Shape_Guide_Nurbs_Curve
#wing_sweep_avg_angle = 100
#
#
#D.objects['Aileron_Boolean_Difference'].rotation_euler[2] = wing_sweep_avg_angle
