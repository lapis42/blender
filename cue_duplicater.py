import bpy
import numpy as np
import re

tags=[r'_camera_',r'_pic',r'_pm_',r'_pr']
S_interval = 1100
scene = bpy.context.scene
# obj=bpy.context.scene.objects

# for j in range (0, len(obj)):
for obj in bpy.context.scene.objects:
    # if obj[j].type=='MESH':
    if obj.type=='MESH':
        # name_S=obj[j].name
        name_S=obj.name
        Sur=[False]*len(tags)
        for i in range (0,len(tags)):
            D_Sur=re.search(tags[i], name_S)
            if D_Sur:
                Sur[i]=True
            else:
                Sur[i]=False

        if Sur[0] != True:
            # bpy.context.scene.objects.active=obj[j]
            bpy.context.scene.objects.active=obj
            # org_loc=obj[j].location
            org_loc=obj.location
            # obj_dim=obj[j].dimensions
            obj_dim=obj.dimensions
            obj_rot=obj.rotation_euler
            tmp=bpy.context.object.data
            obj_copy=tmp.copy()
            if Sur[1] or Sur[2]:
                base_name=name_S[0:-4]
                tag = name_S[-4:]
            else:
                base_name=name_S
                tag = ''

            count=0
            for x in range (1, 6):
                for y in range(1, 6):
                    count+=1
                    new_name="%s.%03d%s" % (base_name, count, tag)
                    ob=bpy.data.objects.new(new_name, obj_copy)
                    ob_loc_x = org_loc[0] + S_interval*x
                    ob_loc_y = org_loc[1] + S_interval*y
                    ob.location = [ob_loc_x, ob_loc_y, org_loc[2]]
                    ob.dimensions=obj_dim
                    ob.rotation_euler=obj_rot
                    # ob.name=new_name
                    scene.objects.link(ob)
                    # scene.update()

scene.update() 
