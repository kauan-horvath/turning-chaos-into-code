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


if __name__ == "__main__":
    calcular_fatorial()
