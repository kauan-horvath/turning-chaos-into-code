"""
####################
# Create an Upscaling Feature
####################

DATE -

MILESTONES:
- Fatorial Calculator [x]
- Scientific Calculator []
- Programming Calculator []

PROGRESS:

Uso de Fatorial  - Definir ele como incremento multplicanto a si mesmo e provocar o calculo correto
    Fatorial é o produto de todos os int positivos anteriores
    (n! = n * (n-1)*(n-2))
    fatorial de 2 = 2* 2-1 #return 2
    fatorial de 3 = 3 * 3 *2 *1 # return 6

Try Except para impedir caracteres invalidos


FAILURES:
Range(1, num + 1) - Falhei algumas vezes na sintaxe dos dois argumentos de Range
    estava usando Min e Max desnecessariamente
    range(1) pra nunca dar DIV/0
    num+1 para nao excluir o ultimo
"""

####################################
import os


def calcular_fatorial():
    try:
        num = int(input("Digite o número: "))
        if num < 0:
            print("Erro: números negativos não têm fatorial.")
        else:
            fatorial = 1
            for i in range(1, num + 1):
                fatorial *= i
                # fat = fat * i
                # fat(3) = fat(3) * 2
            print(f"O fatorial de {num} é {fatorial}")

    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")


def calcula_potencia():
    try:
        base = input("Digite o número da base: ")
        base = int(base)

        expoente = input("Digite o expoente: ")
        expoente = int(expoente)

        if base < 0:
            print("A base precisa ser maior que 0")
            return ValueError
        elif expoente <= 1:
            print("O Exponte precisa ser maior que 1")
            return ValueError

        resultado = base**expoente

        print(f"{base} elevado à {expoente} é igual a: {resultado}")

    except ValueError:
        print("O número informado não é válido")


# VARIAÇÃO PERCENTUAL


def varia_percent():
    try:
        val_inicial = input("Digite o valor inicial: ")
        val_inicial = int(val_inicial)

        val_final = input("Digite o valor final: ")
        val_final = int(val_final)

        if val_inicial <= 0:
            print("O valor inicial precisa ser maior que 0")
            return ValueError
        elif val_final <= 0:
            print("O valor final precisa ser maior que 0")
            return ValueError

        valor_diff = val_final - val_inicial
        percentual = (abs(valor_diff) / val_inicial) * 100

        if valor_diff < 0:
            print(
                f"de {val_inicial} para {val_final}, A variação percentual é -{percentual}%"
            )
        else:
            print(
                f"de {val_inicial} para {val_final}, A variação percentual é +{percentual}%"
            )

    except ValueError:
        print("Os valores inseridos são inválidos")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    # calcula_potencia()
    varia_percent()
