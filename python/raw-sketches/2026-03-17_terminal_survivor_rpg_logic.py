
"""
DESAFIO: O SOBREVIVENTE DO TERMINAL (v1.0)

OBJETIVO:
Sobreviver ao maior número de dias possível gerenciando Energia e Recursos.

DIRETRIZES TÉCNICAS:
1. STATUS INICIAIS: ok
   - Energia: 100 | Madeira: 0 | Dias: 0

2. O LOOP PRINCIPAL (while energia > 0):
   - Cada rodada representa 1 dia. work on
   - Exibir os status atuais no início de cada dia.

3. AÇÕES DO JOGADOR:
   - [1] COLETAR MADEIRA: Ganha entre 5 e 10 de madeira (random) / Gasta 20 de energia.
   - [2] DESCANSAR: Recupera 30 de energia (não pode passar de 100).
   - [3] SAIR: Encerra o jogo.

4. SISTEMA DE EVENTOS (random):
   - Ao coletar madeira, deve haver uma chance (ex: 30%) de um evento ocorrer:
     - Evento Bom: Encontrou frutas (+10 energia).
     - Evento Ruim: Ataque de animal ou cansaço extra (-15 energia).

5. CONDIÇÕES DE FIM DE JOGO:
   - Se energia <= 0: "Game Over" e mostra quantos dias você sobreviveu.
   - Se escolher sair: Mensagem de despedida.

DICAS PYTHON:
- Use 'import random' no topo.
- Use 'random.randint(min, max)' para valores.
- Use 'os.system("cls")' para manter o terminal limpo a cada dia.
"""

import random
import os

# Fazer um joguinho de RPG gerenciando recursos!


# primeira tentativa com dicts
    # my_resources = {
    #     "Energy": 0,
    #     "Wood": 0,
    #     "Days": 0
    # }

    # while Chave " in my_status > 0:
    #     print(f"Teste energia {my_status["Energy"]}")
    #     my_status["Energy"] -= 1

# segunda tentativa com vars
os.system('cls')

energy = 50
wood = 0
days = 0

def day_time(energy, days, wood):
    
    days += 1
    remaining_days = 100 - days

    print(f"""
    Bem vindo ao dia {days}, seus recursos são:
    Energia: {energy} | Madeira: {wood} | Dias Restantes: {remaining_days}

          """)
    return energy, days
    
def descanso(energy):
    energy += 30

    print(f">>>> Você repousa na fogueira e agora têm: {energy} de energia")

    if energy > 100:
        over_energy = energy - 100
        energy -= over_energy
        print(f">>>> Você dormiu demais e {over_energy} energia restante foi descartada")

    elif energy < 20:
        debuff = 10
        energy -= debuff
        print(f">>>> você estava muito exausto não conseguiu se recuperar bem o suficiente e sofreu {debuff} energia de penalidade")

    return energy

def chop_wood(wood):
    logs = random.randint(2,5)
    energy_cost = random.randint(10,20)

    print(f">>>> Você coletou {logs} madeiras, e gastou {energy_cost} energia")
    wood = wood + logs
    return wood, energy_cost

def choice(wood, energy):
    while True:
        try:
            escolha = input(f"""
        Digite sua escolha:
            1) Descanso (Recupera 30 de Energia)
            2) Coletar Madeira (Coleta uma quantidade aleatória de madeira, e consome de 10 a 20 energias)
            
            X) SAIR, Encerra o jogo
                            
            Sua escolha >>>>> """)

            if escolha.upper() in ["1", "DESCANSO"]:
                descanso(energy)
                
                
            elif escolha.upper() in ["2", "MADEIRA"]:
                energy_lost = 0
                wood, energy_lost = chop_wood(wood)
                energy = energy - energy_lost
                

            elif escolha.upper() in ["X", "SAIR"]:
                energy = 0

            else:
                print("Escolha inválida, tente novamente")
            
            break

        except ValueError:
            print("Escolha inválida, tente novamente")   
            break       

    return wood, energy  

print(f"Bem vindo ao jogo de sobrevivencia, seu objetivo é coletar madeira o bastante para realizar projetos e evitar o desgaste extremo")    

while energy > 0:

    energy, days = day_time(energy, days, wood)

    wood, energy = choice(wood, energy)

    if energy <= 10:
        print(f"ALERTA {energy} Energia acabando")
    
    energy -= 1

if energy <= 0:
    print(f"Sua energia esgotou, e atingiu o terrível fim")
    print(f"Você sobreviveu {days} dias, e coletou {wood} Madeira")