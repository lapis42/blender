import bpy

import re

"""
def strip_trailing_number(s):
    m = re.search(r'\.(\d{3})$', s)
    return s[0:-4] if m else s

def unique_name(collection, base_name):
    base_name = strip_trailing_number(base_name)
    count = 1
    name = '*_pic'

    while collection.get(name):
        name = "%s.%03d" % (base_name, count)
        count += 1      
    return name

# check

print(unique_name(bpy.data.objects, "Cube_pic"))
print(unique_name(bpy.data.objects, "Cube.004"))


"""

for obj in bpy.context.scene.objects:
    s=obj.name
    if obj.type == 'MESH':
        m=re.search(r'\.(\d{3})$', s)
        B_s=s[0:-4]
        if m:
            print(B_s)
            n_pic=re.search(r'\_pic$', B_s)
            if n_pic:
                print(obj.name)
                t=s[-3:]
                s=s[0:-8]
                obj.name="%s.%s_pic" % (s,t)
            
            n_pm_=re.search(r'\_pm_$', B_s)
            if n_pm_:
                t=s[-3:]
                s=s[0:-8]
                obj.name="%s.%s_pm_" % (s,t)
