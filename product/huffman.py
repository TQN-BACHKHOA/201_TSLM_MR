import queue, math, os, subprocess
from graphviz import Digraph
from openpyxl import load_workbook
from sympy import *
import latexFile as latexFile
init_printing()

wb = load_workbook("data.xlsx")
ws = wb.worksheets[0]
dot = Digraph(comment='Huffman Tree')

def create_TreeNode(start=None, end=None, text=None):
    dot.node(end, text, shape='doublecircle')
    dot.edge(start, end)

def create_TreeLeaf(start=None, end=None, text=None):
    dot.node(end, text, shape='invhouse', color='black', fillcolor='yellow', style='filled')
    dot.edge(start, end)

def convert(char_array):
    output_string = ""
    return(output_string.join(char_array))

freq = []

probability_CS = 0
for row in ws.iter_rows(min_col=1, max_col=2, min_row=2):
    row = [cell.value for cell in row]
    freq.append((row[0], str(row[1])))
    probability_CS += row[0]
if round(probability_CS, 5) == 1:
    print("Data satisfied")
else:
    print("Data not satisfied")
    os._exit(0)

average_length = 0 
entropy = 0
efficiency = 0

class HuffmanNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def children(self):
        return (self.left, self.right)
    def preorder(self, path=None):
        global average_length
        if path is None:                                
            path = []
        if self.left is not None:
            if isinstance(self.left[1], HuffmanNode):   
                create_TreeNode(start=convert(path), end=convert(path+['0']), text=convert(path+['0']))
                self.left[1].preorder(path+['0'])
            else:
                create_TreeLeaf(start=convert(path), end=convert(path+['0']), text=convert(self.left[1]+convert([': ']+path+['0']))) 
                latexFile.addString(input_string=convert(self.left[1] + convert([': ']+path+['0'])), item=True)
                average_length += self.left[0]*(len(path)+1)
        if self.right is not None:
            if isinstance(self.right[1], HuffmanNode):
                create_TreeNode(start=convert(path), end=convert(path+['1']), text=convert(path+['1']))
                self.right[1].preorder(path+['1'])
            else:
                create_TreeLeaf(start=convert(path), end=convert(path+['1']), text=convert(self.right[1]+convert([': ']+path+['1'])))  
                latexFile.addString(input_string=convert(self.right[1] + convert([': ']+path+['1'])), item=True)
                average_length += self.right[0]*(len(path)+1)

def encode(frequencies):
    p = queue.PriorityQueue()
    for item in frequencies:
        p.put(item)
    while p.qsize() > 1:
        Left, Right = p.get(), p.get()
        node = HuffmanNode(Left, Right)
        p.put((Left[0] + Right[0], node))
    return p.get()

for item in freq:
    entropy += item[0]*math.log2(1/item[0])
node = encode(freq)

###Write to tex file
latexFile.init()
latexFile.addString(input_string="Từ mã của các nodes: ", enter=1)
latexFile.init_item()
node[1].preorder() 
latexFile.end_item()

i, H, N = symbols('i H N')

latexFile.addString(input_string="Entropy:")
entropy_exp = Eq(Sum(Indexed('p',i)*log(1/(Indexed('p',i)),2),(i,0,'k')), round(entropy,3))
latexFile.addString(input_string=latex(entropy_exp), math=True)

latexFile.addString(input_string="Chiều dài TB từ mã:")
tuma_exp = Eq(Sum(Indexed('p',i)*Indexed('N',i),(i,0,'k')), round(average_length,3))
latexFile.addString(input_string='N = '+latex(tuma_exp), math=True)

latexFile.addString(input_string="Hiệu suất Huffman:")
efficiency = entropy/average_length
efficiency_exp = Eq((H/N), round(efficiency,3))
latexFile.addString(input_string=latex(efficiency_exp), math=True)

latexFile.includeImage('graph.png')
with open('output/latex_output.tex','a') as f:
    f.write('\\begin{center}\n')
    f.write('\\textit{Hình 1. Cây Huffman}\n')
    f.write('\\end{center}\n')
    f.close()

latexFile.end()

###Convert from tex to pdf
x = subprocess.call('pdflatex -output-directory=output output/latex_output.tex', shell=True)
if x != 0:
    print('Exit-code not 0, check result!')
else:
    os.system('start latex_output.pdf')

###Graph the Huffman Tree
with open('output/graph.dot','w') as f:
    f.write(dot.source)
subprocess.call('dot -Tpng output/graph.dot -o output/image/graph.png', shell=True)