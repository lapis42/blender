import bpy
import numpy as np
import re

move_interval = (-120, 0, 0)
nMove = 1
for iX in range(nMove):
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":move_interval, "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})


move_distance = (-60, 60, 0)
bpy.ops.transform.translate(value=move_distance, constraint_axis=(True, False, False), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED')