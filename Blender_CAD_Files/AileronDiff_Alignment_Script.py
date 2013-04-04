import bpy
#What's this do EXACTLY?
#Makes the handler trigger persistent across file reloads. (AKA only good for a global addon, hence disabled here.)
#from bpy.app.handlers import persistent

class aileronDiffAlignmentOperator(bpy.types.PropertyGroup):
    #MUST BE LOWERCASE
    bl_idname = "object.aileron_diff_alignment_operator"
    bl_label = "Aileron Diff Alignment Script"

    def scene_update(context):
        if bpy.data.objects.is_updated:
            print("One or more objects were updated!")
            for ob in bpy.data.objects:
                if ob.is_updated:
                    print("=>", ob.name)
        #.wing_sweep_avg_angle = 100

            for i in range(0,2):
                bpy.data.objects['Aileron_Boolean_Difference'].rotation_axis_angle[i] = 0
        
            #context.active_object.rotation_euler[2] = 0
            #context.active_object.location.x += 1.0
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
