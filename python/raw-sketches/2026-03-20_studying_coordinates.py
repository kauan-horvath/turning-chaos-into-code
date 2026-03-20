#Treino de Coordenadas, Dicts aninhados e Distancias

import os

MAX_DISTANCE = 15

frota = {
    "Caminhão_A":{"x":10, "y":20},
    "Caminhão_B":{"x":50, "y":5},
    "Caminhão_C":{"x":2, "y":3},
} #Dicionário aninhado << OK

# ====================================================

def auxiliary_whatever():
    pass

def cal_proximidade(x_cliente, y_cliente, frota):

    vencedor = None
    menor_distancia = float('inf')

    for nome, pos in frota.items():
        dist_total = abs(pos["x"] - x_cliente) + abs(pos["y"] - y_cliente)

        if dist_total <= menor_distancia:
            vencedor = nome
            menor_distancia = dist_total

        if dist_total <= MAX_DISTANCE:
            print(f"O {nome} está a {dist_total} km e poderá te atender!")
        else:
            print(f"O {nome}, está muito distante, {dist_total} km.")
    
    return vencedor, menor_distancia

def main():

    try:
        x_cliente = int(input("Forneça sua coordenada X:  "))
        y_cliente = int(input("Forneça sua coordenada Y:  "))

        melhor_nome, melhor_dist = cal_proximidade(x_cliente, y_cliente, frota)

        print("-" * 30)
        print(f"O Melhor caminhão para você é {melhor_nome} (Distância: {melhor_dist})\n")


    except ValueError:
        print("Insira apenas números")
        return

if __name__ == "__main__":
    os.system('cls')
    main()
    