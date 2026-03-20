#TREINO DE SINTAXE - COM CARROS NUM ESTACIONAMENTO

# Imports | Constantes | Dicts

import os
import random

VALOR_HORA = 10
VAGAS_TOTAIS = 5

vagas_ocupadas = [
]

lista_carros = {
"Ford Ka": ["ABC111", 1],
"Jeep Renegade":["ABC222", 2],
"Audi A8":["ABC333", 3],
"Toyota Hyllux":["ABC444", 4],
"Volkswagem Polo":["ABC555", 5],
"Fiat Toro":["ABC666", 6]
}

meu_caixa = {
"Faturamento": 0.0
}

# Func_Auxiliares | Func_Logicas

def estacionar(estacionamento, placa):
    if len(estacionamento) >= VAGAS_TOTAIS:
        print(f"Não há vagas, {placa} placa não estacionada")
    else:
        estacionamento.append(placa)
        #print(f"{placa} Placa estacionada")

def liberar_vaga(estacionamento, placa, hora, caixa):

    if placa in estacionamento:
        estacionamento.remove(placa)
        
        
        cost = hora * VALOR_HORA
        caixa["Faturamento"] += cost

        #print(f"{placa} Placa removida, cobrado {cost}")

    else:
        print(f"{placa} placa não encontrada, cobrado 0")
        pass

def exibir_relatorio(caixa):
    for chave, valor in caixa.items():
        print(f"""
O faturamento total foi de R$ {valor:.2f}
""")
        
# Main_Loop

for carro, dados in lista_carros.items():
    placa = dados[0]
    estacionar(vagas_ocupadas, placa)

for carro, dados in lista_carros.items():
    placa = dados[0]
    hora = dados [1]
    liberar_vaga(vagas_ocupadas, placa, hora, meu_caixa)
    
exibir_relatorio(meu_caixa)
