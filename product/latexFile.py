import subprocess, os

def init():
    with open('output/latex_output.tex','w') as f:
        f.write('\\documentclass{article}\n')
        f.write('\\usepackage{amsmath}\n')
        f.write('\\usepackage{graphicx}\n')
        f.write('\\usepackage{hyperref}\n')
        f.write('\\title{TRUYEN SO LIEU VA MANG}\n\n')
        f.write('\\begin{document}\n\n')
        f.close()

def end():
    with open('output/latex_output.tex','a') as f:
        f.write('\\end{document}\n')
        f.close()

def init_item():
    with open('output/latex_output.tex','a') as f:
        f.write('\\begin{itemize}\n')
        f.close()

def end_item():
    with open('output/latex_output.tex','a') as f:
        f.write('\\end{itemize}\n')
        f.close()

def addString(input_string=None, item=None, enter=0, math=None):
    with open('output/latex_output.tex','a') as f:
        if math is not None:
            f.write('\\[\n')
        if item is not None:
            f.write('\\item ')
        f.write(input_string)
        if math is not None:
            f.write('\n\\]')
        f.write('\n')
        f.close()
