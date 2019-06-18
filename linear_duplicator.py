import bpy
import numpy as np


obj=bpy.context.active_object
name_S=obj.name
org_loc=obj.location
obj_rot=obj.rotation_euler
tmp=bpy.context.object.data
obj_copy=tmp.copy()





input_i = raw_input('>>> ')

while input_i != 0:

    if input_i == 1:
        if obj_rot[2] == 0:
            new_name="%s.%03d%s" % (base_name, count, tag)
            ob=bpy.data.objects.new(new_name, obj_copy)
            ob_loc_x = org_loc[0] + S_interval*x
            ob_loc_y = org_loc[1] + S_interval*y
            ob.location = [ob_loc_x, ob_loc_y, org_loc[2]]
            ob.dimensions=obj_dim
            ob.rotation_euler=obj_rot
            scene.objects.link(ob)
                    



