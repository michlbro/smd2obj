import os
import importlib.util

class meshbridge:

    def printProgressBar (self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        # Print New Line on Complete
        if iteration >= total: 
            print('\n')
            return
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

    class importFile():
        def __init__(self, bridge, filePath) -> None:
            for root, _, files in os.walk(filePath):
                for file in files:
                    if "import_" in file:
                        spec = importlib.util.spec_from_file_location(file, os.path.join(root, file))
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        setattr(self, file.replace("import_", '').rstrip('.py'), module.import_file(bridge))

    class exportFile():
        def __init__(self, bridge, filePath) -> None:
            for root, _, files in os.walk(filePath):
                for file in files:
                    if "export_" in file:
                        spec = importlib.util.spec_from_file_location(file, os.path.join(root, file))
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        setattr(self, file.replace("export_", '').rstrip('.py'), module.export_file(bridge))

    class LookupDict():
        def __init__(self):
            self.dict = {}

        def Find(self, object):
            try:
                return self.dict[object.ToString()]
            except:
                return False
        
        def Append(self, object):
            object.index = len(self.dict)
            self.dict[object.ToString()] = object

        def Clean(self):
            self.dict.clear()

    class Polygon():
        def __init__(self, normalSize, uvSize, indicieSize):
            self.normals = [[0,0,0]] * normalSize
            self.uvs = [[0,0]] * uvSize
            self.indicies = [0] * indicieSize

    class Vertex():
        def __init__(self, vector):
            vectorLen = len(vector)
            self.index = 0
            self.x = vector[0] if vectorLen > 0 else 0
            self.y = vector[1] if vectorLen > 1 else 0
            self.z = vector[2] if vectorLen > 2 else 0

        def Compare(self, vector):
            return self.x == vector.x and self.y == vector.y and self.z == vector.z
        
        def ToString(self):
            return f"{self.x}, {self.y}, {self.z}"
        
    def PreAllocatePolygons(self, count, normal, uv, indicie):
        self.polygons = [None] * count
        for i in range(0, count):
            self.polygons[i] = self.Polygon(normal, uv, indicie)

    def GetVertexIndex(self, vertex):
        index = self.vertexDict.Find(vertex)
        if index == False:
            self.vertexDict.Append(vertex)
            self.verticies.append(vertex)
            return len(self.vertexDict.dict) - 1
        return index.index

    def __init__(self) -> None:
        self.polygons = None
        self.vertexDict = self.LookupDict()
        self.verticies = []

        filePath = os.path.dirname(os.path.realpath(__file__))
        self.import_file = self.importFile(self, filePath + "\importers")
        self.export_file = self.exportFile(self, filePath + "\exporters")