# CALCULO DE POTENCIA
import os


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
