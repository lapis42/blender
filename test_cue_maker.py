import bpy
from mathutils import Matrix

mylayers = [False]*20
mylayers[0] = True
add_cube = bpy.ops.mesh.primitive_cube_add

O_interval=40
M_interval=1100
z_pos=21
O_dimensions=[10, 10, 30]
count= 1
mat = bpy.data.materials.new('Hoge')
bpy.data.materials["Hoge"].diffuse_color=[0,0,1]


for index_x in range(1, 6):
    for index_y in range(1,6):
        add_cube(location=(index_x*M_interval+(index_x-3)*O_interval, index_y*M_interval+(index_y-3)*O_interval, z_pos), layers=mylayers)
        bpy.context.active_object.dimensions = O_dimensions
        bpy.context.active_object.name="cue.%03d_r" % count
        bpy.context.active_object.data.materials.append(mat)
        count+=1

