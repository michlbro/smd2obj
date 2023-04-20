import SmdLoader
import ObjCreator

file = r"file.smd"
export = r""

smd = SmdLoader.smd(file)
obj = ObjCreator.obj(smd.GetVertexCords(), smd.GetVertexNorm(), smd.GetVertexTex(), smd.GetVertextIndex())
obj.Convert()
obj.ExportObj(r'output path', 'file name')
