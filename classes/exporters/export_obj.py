import os

class OBJ:
    def __init__(self, bridge):
        self.meshbridge = bridge

    def ExportFile(self, filepath, override=True):
        fullFilePath = os.path.splitext(filepath)[0] + '.obj'

        if os.path.exists(fullFilePath):
            if override:
                os.remove(fullFilePath)
            else:
                return

        vertexList = self.meshbridge.verticies
        polygonList = self.meshbridge.polygons
        vertexs = ''
        normals = ''
        uvs = ''
        faces = ''

        for vertex in vertexList:
            vertexs += f"v {vertex.x} {vertex.y} {vertex.z}\n"

        self.meshbridge.printProgressBar(0, len(polygonList), prefix = 'Exporting Geometry to OBJ', suffix = 'Completed')
        polygonListLength = len(polygonList)
        for polyCount in range(0, polygonListLength):
            polygon = polygonList[polyCount]
            face = 'f'
            for i in range(0, 3):
                normals += f"vn {polygon.normals[i][0]} {polygon.normals[i][1]} {polygon.normals[i][2]}\n"
                uvs += f"vt {polygon.uvs[i][0]} {polygon.uvs[i][1]}\n"
                lineCount = ((polyCount + 1) * 3 - 2) + i
                
                face += f" {polygon.indicies[i] + 1}/{lineCount}/{lineCount}"
            faces += face + "\n"
            if polyCount % 100 == 0 or polyCount == polygonListLength - 1:
                self.meshbridge.printProgressBar(polyCount + 1, polygonListLength, prefix = 'Exporting Geometry to OBJ', suffix = 'Completed')
        print("\nOBJ Exported")
        with open(fullFilePath, 'w') as file:
            file.write(vertexs + normals + uvs + faces)
            file.close()

        self.meshbridge.polygons.clear()
        self.meshbridge.verticies.clear()
        self.meshbridge.vertexDict.Clean()


            
        

def export_file(meshbridge):
    return OBJ(meshbridge).ExportFile