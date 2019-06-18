import bpy
from mathutils import Matrix

mylayers = [False]*20
mylayers[0] = True
add_cube = bpy.ops.mesh.primitive_cube_add

O_interval=100
M_interval=0
z_pos=21
O_dimensions=[50, 50, 30]
count= 1
mat = bpy.data.materials.new('cue')
bpy.data.materials["cue"].diffuse_color=[0,0,1]
mat2 = bpy.data.materials.new('rep')
bpy.data.materials["rep"].diffuse_color=[1,0,0]
row_num = 2
colomn_num = 2 




add_cube(location=(1*M_interval+(1-((row_num + 1)/2))*O_interval, 1*M_interval+(1-((colomn_num + 1)/2))*O_interval, z_pos), layers=mylayers)
bpy.context.active_object.dimensions = O_dimensions
bpy.context.active_object.name="cue"
bpy.context.active_object.data.materials.append(mat)




for index_x in range(1, row_num + 1):
    for index_y in range(1,colomn_num + 1):
        add_cube(location=(index_x*M_interval+(index_x-((row_num + 1)/2))*O_interval, index_y*M_interval+(index_y-((colomn_num + 1)/2))*O_interval, z_pos), layers=mylayers)
        bpy.context.active_object.dimensions = O_dimensions
        bpy.context.active_object.name="_rep.%03d_pr_" % count
        bpy.context.active_object.data.materials.append(mat2)
        count+=1

