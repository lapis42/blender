for obj in bpy.context.scene.objects:
    if obj.type=='MESH':
        if "_wallHall" in obj.name:
            obj.dimensions[1] = 15


for obj in bpy.context.scene.objects:
    if obj.type=='MESH':
        if "Beacon" in obj.name:
            obj.dimensions[1] = 0.1
            obj.location[1] += 3