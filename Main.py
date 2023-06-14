# coding: utf-8
# Your code here!
from escribir import *
from controlador import *
from entrada import *
from menu import *

op=menu()
num1=entrada()
num2=entrada()
res=controlador(op,num1,num2)
escribir(res,op)
