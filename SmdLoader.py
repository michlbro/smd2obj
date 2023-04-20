# STRUCTURE:
# triangles
# <material> -- Defines a new triange
# <int|Parent bone> <float|PosX PosY PosZ> <normal|NormX NormY NormZ> <float|U V> <int|links> <int|Bone ID> <float|Weight>

class smd:
    def __init__(self, file):
        self.vertexCords = []
        self.vertexTex = []
        self.vertexNorm = []
        self.vertexIndex = []
        self.triangles = 0

        # Open file.
        # Read and skip each line until "triangle" is defined
        # under each <material> means a new triangle.
        # read until "end"

        isTriangleBlock = False
        indexCount = 0

        triangleIndex = 0
        for line in open(file, 'r'):
            if isTriangleBlock and line.rstrip() == "end":
                break

            if isTriangleBlock:
                if triangleIndex%4 == 0:
                    triangleIndex = 0

                #material identifier
                if triangleIndex == 0:
                    self.triangles += 1
                    triangleIndex += 1
                    self.vertexIndex.append([])
                    continue
                indexCount += 1
                vertexValues = line.split()
                self.vertexCords.append(vertexValues[1:4])
                self.vertexNorm.append(vertexValues[4:7])
                self.vertexTex.append(vertexValues[7:9])
                self.vertexIndex[self.triangles-1].append([indexCount, indexCount, indexCount])
                # triangleIndex 1 == first vertex
                # triangleIndex 3 == last vertex
                triangleIndex += 1

            # start of triangles
            if line.rstrip() == "triangles":
                isTriangleBlock = True


    def GetVertexCords(self):
        return self.vertexCords
    
    def GetVertexTex(self):
        return self.vertexTex
    
    def GetVertexNorm(self):
        return self.vertexNorm
    
    def GetVertextIndex(self):
        return self.vertexIndex
        