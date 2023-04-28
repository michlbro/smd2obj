import sys
import os
from classes.meshbridge import meshbridge as MeshBridge

meshbridge = MeshBridge()

def main():
    print(len(sys.argv))
    if len(sys.argv) != 3:
        exit()

    smdFiles = sys.argv[1]
    exportFiles = sys.argv[2]
    for root, _, files in os.walk(smdFiles):
        for name in files:
            if name.endswith('smd'):
                fileName = root.replace(smdFiles, exportFiles)
                meshbridge.import_file.smd(filepath=os.path.join(root, name))
                os.makedirs(fileName, exist_ok= True)
                meshbridge.export_file.obj(filepath=os.path.join(root.replace(smdFiles, exportFiles), name.replace('.smd', '')), override=True)

if __name__ == "__main__":
    main()