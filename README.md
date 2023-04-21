# smd2obj
Simple SMD to OBJ python script that uses blender python API.
You will need to have blender source tools addon installed for blender to import smd files.
http://steamreview.org/BlenderSourceTools/

Can be used to import other file formats and export them into various file formats depending if an addon or blender supports it.
Generally, ```bpy.ops.export_scene.<format>``` and ```bpy.ops.import_scene.<format>``` is to be edited.