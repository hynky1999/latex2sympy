from sympy import *
import sys
sys.path.append("..")
from process_latex import process_sympy

latex = "\\begin{pmatrix}1\\\\2\\\\3\\end{pmatrix}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "\\begin{pmatrix}1\\\\2\\\\3\\end{pmatrix},\\begin{pmatrix}4\\\\3\\\\1\\end{pmatrix}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
