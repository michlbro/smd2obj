import os

class smd:
    def __init__(self, meshbridge) -> None:
        self.meshbridge = meshbridge

    def import_file(self, filepath):
        self.MainImport(filepath)

    def ReadPoly(self, file, polygonCount):
        current_line = file.readline().strip()
        if 'end' in current_line:
            return False
        
        polygon = self.meshbridge.polygons[polygonCount]
        for i in range(0, 3):
            vertexLine = file.readline().strip()
            vectors = list(filter(None, vertexLine.split(' ')))

            vertex = list(map(float, vectors[1:4]))
            normal = list(map(float, vectors[4:7]))
            uv = list(map(float, vectors[7:9]))

            vertexObj = self.meshbridge.Vertex(vertex)
            polygon.normals[i][0] =  normal[0]
            polygon.normals[i][1] =  normal[1]
            polygon.normals[i][2] =  normal[2]
            polygon.uvs[i][0] = uv[0]
            polygon.uvs[i][1] = uv[1]
            polygon.indicies[i] = self.meshbridge.GetVertexIndex(vertexObj)
        return True
    
    def ReadLineCount(self, filepath):
        triangles = 0
        with open(filepath, 'r') as file:
            while 'triangles' not in file.readline().strip():
                pass

            while 'end' not in file.readline().strip():
                for _ in range(0, 3):
                    file.readline()
                triangles += 1

        print(f"Triangle count: {triangles}\n")
        return triangles

    def MainImport(self, filepath):
        polygonTotalCount = self.ReadLineCount(filepath)
        self.meshbridge.PreAllocatePolygons(polygonTotalCount, 3, 3, 3)
        polygonCount = 0
        with open(filepath, 'r') as file:
            while 'triangles' not in file.readline().strip():
                pass
            self.meshbridge.printProgressBar(0, polygonTotalCount, prefix = 'Getting Geometry: ', suffix = 'Complete')
            while self.ReadPoly(file, polygonCount):
                polygonCount += 1
                if polygonCount % 100 == 0 or polygonCount == polygonTotalCount - 1:
                    self.meshbridge.printProgressBar(polygonCount + 1, polygonTotalCount, prefix = 'Getting Geometry: ', suffix = 'Complete')

def import_file(meshbridge):
    return smd(meshbridge).import_file