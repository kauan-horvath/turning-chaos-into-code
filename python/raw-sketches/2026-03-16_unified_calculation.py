import os
import random

os.system('cls')

#Criar uma operação de cálculo simples, que demonstra o second order thinking dentro das funções

#fornecer números sozinho para facilitar o treino
a = random.randint(0,9)
b = random.randint(0,9)

#FUNÇÕES DE CALCULO AUXILIARES
def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

#FUNÇÃO DE 2 NIVEL COM ARGUMENTO DE STRING
def calculo_unificado(operation, a,b):

    resultado = 0

    if operation == "Somar":
        resultado = somar(a,b)

    elif operation == "Subtrair":
        resultado = subtrair(a,b)

    elif operation == "Multiplicar":
        resultado = multiplicar(a,b)

    elif operation == "Dividir":
       #Debug DIV/0
       if b == 0:
            b = 1
            print(f"Impossible divide {a} by 0")
           
       else:
           resultado = dividir(a,b)

    else:
        resultado = None
        print(f"{operation} é um operador inválido")

    return resultado

#declaração de lista útil
operation_list = [
        "Somar",
        "Subtrair",
        "Multiplicar",
        "Dividir"
    ]


def all_operations(a,b):
    for operation in operation_list:
     print(f"{operation} ({a} | {b}) é igual a: {calculo_unificado(operation, a,b)}\n")


all_operations(a,b)