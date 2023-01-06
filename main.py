import time
import os
from uteis import *
from cores import *



linha(f"{green('CALCULADORA PYTHON')}")
linha(f"{blue('Digite a opção desejada: ')}")
yellow(f"""Multiplicação    [1]
Soma             [2]
Subtração        [3]
Divisão          [4]
Fatorial         [5]""")
print(25*'-')
  
while True:
  resp = leiaInt("Digite sua opção: ")
  if resp == 1:
    mult()
  elif resp == 2:
    soma()
  elif resp == 3:
    sub()
  elif resp == 4:
    divi()
  elif resp == 5:
    fatorial()
  if resp > 5 or resp < 1:
    print()
    red("ERRO! Digite uma opção válida.")
    print()
    continue
  linha("Deseja voltar à calculadora? ")
  continuar = input("Opção [s/n]: ")
  if continuar in "Nn":
    break  
  else:
    caculadora()
    
os.system('clear')
linha("OBRIGADO! Volte sempre.")