import os

class obj:
    def __init__(self, v, vn, vt, f):
        print(len(v))
        self.v = v,
        self.vn = vn
        self.vt = vt
        self.f = f
        self._objText = ""

    def Convert(self):
        for v in self.v:
            print(self.v[2])
            self._objText += f'v {v[0]} {v[1]} {v[2]}\n'
        for v in self.vn:
            self._objText += f'vn {v[0]} {v[1]} {v[2]}\n'
        for v in self.vt:
            self._objText += f'vt {v[0]} {v[1]}\n'
        for v in self.f:
            self._objText += f'f {v[0][0]}/{v[0][1]}/{v[0][2]} {v[1][0]}/{v[1][1]}/{v[1][2]} {v[2][0]}/{v[2][1]}/{v[2][2]}\n'

    def ExportObj(self, output, fileName):
        with open(f'{output}\{fileName}.txt', 'a') as text:
            text.write(self._objText)
            text.close()
        os.rename(f'{output}\{fileName}.txt', f'{output}\{fileName}.obj')
    