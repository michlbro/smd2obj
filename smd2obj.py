import bpy
import os

smdFiles = r'<file input here>'
exportFiles = r'<file output here>'
removeMTLFiles = True

for root, _, files in os.walk(smdFiles):
    for name in files:
        if name.endswith('smd'):
            fileName = root.replace(smdFiles, exportFiles)
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete()
            bpy.ops.import_scene.smd(filepath=os.path.join(root, name))
            os.makedirs(fileName, exist_ok= True)
            bpy.ops.export_scene.obj(filepath=os.path.join(root.replace(smdFiles, exportFiles), name.replace('.smd', '')+'.obj'))
            if removeMTLFiles:
                os.remove(os.path.join(fileName, name.replace('.smd', '')+'.mtl'))
