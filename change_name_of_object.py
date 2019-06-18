for obj in bpy.context.scene.objects:
    if obj.type=='MESH':
        if ('DoorR' in obj.name) or ('DoorL' in obj.name) or ('DoorB' in obj.name):
            obj.name = obj.name.replace('_p', '') 


for obj in bpy.context.scene.objects:
    if obj.type=='MESH':
        if ('DoorR' in obj.name) or ('DoorL' in obj.name):
            obj.name = obj.name.replace('_p', '') 


for obj in bpy.context.scene.objects:
    if obj.type=='MESH':
        if (('DoorR' in obj.name) or ('DoorL' in obj.name)) and (obj.name[6] == '2'):
            if '.' in obj.name:
                obj.name = obj.name.replace('02', 'A2')
                obj.name = obj.name.split('.')[0]
            obj.name = obj.name + '_p'


findName = '_blocker'
iName = 0
for obj in bpy.context.scene.objects:
    if obj.type=='MESH':
        if findName in obj.name:
            iName = iName + 1
            obj.name = '_blocker' + ('%02d' % iName) + '_p_'