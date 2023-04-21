import bpy
import os

smdFiles = r'<file input here>'
exportFiles = r'<file output here>'
for root, _, files in os.walk(smdFiles):
    for name in files:
        if name.endswith('smd'):
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete()
            bpy.ops.import_scene.smd(filepath=os.path.join(root, name))
            os.makedirs(root.replace(smdFiles, exportFiles))
            bpy.ops.export_scene.obj(filepath=os.path.join(root.replace(smdFiles, exportFiles), name+'.obj'))
            print(root.replace(smdFiles, exportFiles))