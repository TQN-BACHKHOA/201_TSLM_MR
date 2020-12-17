class latexClass(object):
    def __init__(self, addr=None):
        self.addr = addr

    def init(self):
        with open(self.addr,'w') as f:
            f.write('\\documentclass{article}\n')
            f.write('\\usepackage[utf8]{vietnam}\n')
            f.write('\\usepackage[utf8]{inputenc}\n')
            f.write('\\usepackage{amsmath}\n')
            f.write('\\usepackage{graphicx}\n')
            f.write('\\usepackage{tikz}\n')
            f.write('\\usepackage{forest}\n')
            f.write('\\usetikzlibrary{shapes}\n')
            f.write('\\usepackage{hyperref}\n')

            f.write('\\newcounter{figureCnt}\n\\newenvironment{figureCnt}[1][]')
            f.write('{\\refstepcounter{figureCnt}\\par\\medskip\\textbf{Figure~\\thefigureCnt. #1} \\rmfamily}{\\medskip}')

            f.write('\\title{TRUYEN SO LIEU VA MANG}\n\n')
            f.write('\\begin{document}\n\n')
            f.write('\\begin{center}\n')
            f.write('\\Large\n\\textbf{Truyền Số Liệu và Mạng Mở Rộng}\n')
            f.write('\\large\n\\end{center}\n\n')

    def end(self):
        with open(self.addr,'a') as f:
            f.write('\\end{document}\n')

    def init_item(self):
        with open(self.addr,'a') as f:
            f.write('\\begin{itemize}\n')

    def end_item(self):
        with open(self.addr,'a') as f:
            f.write('\\end{itemize}\n')

    def add_table(self, _array=None):
        with open(self.addr,'a') as f:
            f.write('\\begin{table}[h!]\n')
            f.write('\\centering')
            f.write('\\begin{tabular}{||c c c||}\n')
            f.write('\\hline\n Symbol & Probability & Code \\\ [0.5ex]\n\\hline\n')
            for row in _array:
                f.write('\\hline\n')
                f.write(row[0])
                f.write(' & ')
                f.write(row[1])
                f.write(' & ')
                f.write(row[2])
                f.write(' \\\ \n')
                f.write('\\hline\n')
            f.write('\\end{tabular}\n')
            f.write('\\end{table}\n\n')

    def init_tree(self):
        with open(self.addr,'a') as f:
            f.write('\\begin{center}\n')
            f.write('\\begin{forest}\n')
            f.write('[Root ')

    def addNode_tree(self, _text=None, _type=None):
        with open(self.addr,'a') as f:
            f.write('[')
            f.write(_text)
            if _type == "NODE":
                f.write(', for tree={circle,draw}')
            elif _type == "LEAF":
                f.write(', for tree={rectangle,draw,fill=green}')
                f.write(', rotate={-90}')
    def closeNode_tree(self):
        with open(self.addr,'a') as f:
            f.write(']')

    def end_tree(self):
        with open(self.addr,'a') as f:
            f.write(']')
            f.write('\\end{forest}\n')
            f.write('\\end{center}\n')

    def addString(self, input_string=None, item=None, enter=0, math=None):
        with open(self.addr,'a') as f:
            if math is not None:
                f.write('\\[\n')
            if item is not None:
                f.write('\\item ')
            f.write(input_string)
            if math is not None:
                f.write('\n\\]')
            f.write('\n')
    
    def add_figure(self, _caption=None):
        if _caption is not None:
            with open(self.addr,'a') as f:
                f.write('\\begin{center}')
                f.write('\\begin{figureCnt}\n')
                f.write(_caption)
                f.write('\n\\end{figureCnt}\n')
                f.write('\\end{center}')
