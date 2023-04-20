import SmdLoader
import ObjCreator

file = r"C:\Users\wnace\Documents\Developing\Assets\Portal\Portal_Decompiled_Models\root\models\props\wall_pipes_terminate01\wall_pipes_terminate01\wall_pipes_terminate01.smd"
export = r""

smd = SmdLoader.smd(file)
obj = ObjCreator.obj(smd.GetVertexCords(), smd.GetVertexNorm(), smd.GetVertexTex(), smd.GetVertextIndex())
obj.Convert()
obj.ExportObj(r'C:\Users\wnace\Documents\Developing\Assets\test', 'test')