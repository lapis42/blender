for obj in bpy.context.scene.objects:
    if obj.type=='MESH':
        if "DoorBR" in obj.name:
            obj.dimensions[0] = 3.0
            obj.location[0] = obj.location[0] + 1.55
        if "DoorBL" in obj.name:
            obj.dimensions[0] = 3.0
            obj.location[0] = obj.location[0] - 1.55


for obj in bpy.context.scene.objects:
    if obj.type=='MESH':
        if "DoorBR" in obj.name:
            obj.location[0] = obj.location[0] + 0.4
        if "DoorBL" in obj.name:
            obj.location[0] = obj.location[0] - 0.4

lightGray = bpy.data.materials['LightGray']
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        if ("DoorB" in obj.name) or ("DoorL" in obj.name) or ("DoorR" in obj.name):
            nMaterial = len(obj.material_slots)
            for iMat in range(nMaterial):
                obj.active_material_index = iMat
                if obj.active_material.name=='White':
                    obj.active_material = lightGray

for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        if 'Cube' in obj.name:
            if obj.dimensions == Vector((0.5, 30, 30)):
                nMaterial = len(obj.material_slots)
                for iMat in range(nMaterial):
                    obj.active_material_index = iMat
                    if obj.active_material.name=='White':
                        obj.active_material = lightGray

for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        if 'Wall' in obj.name:
            if obj.dimensions == Vector((0.5, 15, 30)):
                nMaterial = len(obj.material_slots)
                for iMat in range(nMaterial):
                    obj.active_material_index = iMat
                    if obj.active_material.name=='White':
                        obj.active_material = lightGray