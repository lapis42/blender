bpy.ops.object.select_all(action='DESELECT')

for obj in bpy.data.objects:
    if obj.type == "MESH":
        if 'DoorB' in obj.name:
            obj.select = True

bpy.ops.object.delete()