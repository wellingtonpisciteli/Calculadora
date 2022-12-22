from cores import*
import time
import os

def caculadora():
  os.system('clear')
  time.sleep(2)
  linha(f"{green('CALCULADORA PYTHON')}")
  linha(f"{blue('Digite a opção desejada: ')}")
  yellow(f"""  Multiplicação    [1]
  Soma             [2]
  Subtração        [3]
  Divisão          [4]
  Fatorial         [5]""")
  print(25*'-')


def leiaInt(num):
  while True:
    try:
      n = int(input(num))
    except Exception as erro:
      print()
      red('ERRO! Digite uma opção válido.')
      print()
      continue
    else:
      return n


def leiaReal(num):
  while True:
    try:
      n = str(input(num)).replace(',', '.') 
      return float(n)
    except Exception as erro:
      print()
      red('ERRO! Tente novamente.')
      blue(f'Tipo de erro: {erro.__class__}')
      print()
      continue


def linha(txt):
  print(len(txt) * '-')
  print(txt)
  print(len(txt) * '-')


def mult():
  mul = 1
  cont = 1
  linha("Você escolheu Multiplicação!")
  while True:
    try:
      numi = leiaReal(f"Digite o {cont}° número que deseja multiplicar: ")
      mul *= numi
      cont += 1
      if cont >= 3:
        respi = input("Deseja continuar multiplicando? [s/n]: ")
        if respi in "Nn":
          break
    except:
      print("ERRO! Digite uma opção válida")
          
  linha(f"O resultado da multiplicação é: {mul:.2f}")


def soma():
  cont = 1
  s = 0
  linha("Você escolheu Soma!")
  while True:
    nume = leiaReal(f"Digite o {cont}° número que deseja somar: ")
    s += nume
    cont += 1
    if cont >= 3:
      respi = input("Deseja continuar somando? [s/n]: ")
      if respi in "Nn":
        break
  linha(f"O resultado da soma é {s:.2f} ")


def sub():
  cont = 1
  linha("Você escolheu Subtração!")
  num = leiaReal(f"Digite o {cont}° número: ")
  while True:
    menos = float(input(f"Digite o {cont}° número que deseja subtrair: "))
    num -= menos
    cont += 1
    respi = input("Deseja continuar subtraindo? [s/n]: ")
    if respi in "Nn":
      break
  linha(f"O resultado da subtração é {num:.2f} ")


def divi():
  linha("Você escolheu Divisão!")
  numd = leiaReal(f"Digite o numerador: ")
  div = leiaReal(f"Digite o denominador: ")
  numd /= div
  linha(f"O resultado da divisão é {numd:.2f} ")


def fatorial():
  print(45*'-')
  fat = leiaInt("Digite o número que deseja ver o  fatorial: ")
  f = 1
  for c in range(1, fat + 1):
    f *= c
  linha(f'O fatorial de {fat} é {f}')