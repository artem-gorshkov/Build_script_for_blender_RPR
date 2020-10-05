# Run as: blender -b <filename> -P <this_script>
import bpy
import sys

bpy.data.scenes[0].render.engine = 'RPR'
bpy.context.scene.render.filepath = sys.argv[6]

if(len(sys.argv) == 8):
    s = sys.argv[7]
    rgb = []
    for i in range(0, 6, 2):
        rgb.append(int(s[i:i+2], 16) / 255)  
    mat = bpy.data.materials.new("RGB")
    mat.use_nodes = True
    mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (rgb[0], rgb[1], rgb[2], 1)
    bpy.data.objects['Object'].active_material = mat

bpy.ops.render.render(write_still=True)
