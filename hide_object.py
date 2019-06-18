nObj = 0
for obj in bpy.context.scene.objects:
    if obj.type=='MESH':
        if "_" in obj.name:
            obj.hide = True