'''CRIAR CODIGO MODELO COM:
    LIMPEZA
    MODULARIDADE
    E PREVISIBILIDADE
'''

''' best order:
1) imports
2) constantes (MAX_ENERGY)
3) dicts centrais (Central de dados)
4) funções utilitárias
5) funções lógicas
6) loop principal
'''

import random
import os

#==============

MAX_ENERGY = 100
USERNAME = None

#==============

player_stats = {
    "energy":100,
    "wood":0,
    "days":0,
    "name": ""
}

#===============

def chop_wood(p):
    #gerar madeira e diminuir energia
    cost = random.randint(10,20)
    p["energy"] -= cost #gemini, porque p ao inves de player_status?
    p["wood"] += random.randint(2,5)

def get_rest(p):
    p["energy"] = min(p["energy"] + 30, 100)
    log("descanso", p["energy"])

    if p["energy"] > MAX_ENERGY:
        exc_energy = 100 - p["energy"]
        p["energy"] -= exc_energy
        log("exc_energy", exc_energy)

def show_status(p):
    print(f""" PLAYER STATUS:
    GUERREIRO(a): {USERNAME}
        DIA: {p["days"]}
        ENERGIA: {p["energy"]}
        MADEIRA: {p["wood"]}

""")

def log(msg_type, value=None):

    messages = {
        "wood": f"{value} madeiras coletadas!",
        "energy_lost": f"{value} energia perdida!",
        "energy_rem": f"{value} energia restante",
        "get_name": f"Qual o seu nome?",
        "presenting": f"Olá {value},seja bem vindo ao jogo de RPG de texto",
        "start": f"Podemos começar? S | N ",
        "descanso": f"Você descansou e obteve {value} energia",
        "exc_energy":f"Você dormiu demais e desperdiçou {value} energia, mantendo o máximo: 100",
        "Marjorie":"Te amo",
        "Kauan":"Ética e Metafísica"
    }

    print(messages.get(msg_type, "Ação desconhecida"))
    #gemini porque há ação desconhecida? como funciona o get?


#================

def game(p):
    playing = False

    p["name"] = input(f"{log("get_name")}")
    print("nome", USERNAME)

    log("presenting",USERNAME)

    playing = input(f"{log("start")}")
    

    if playing.upper() in ["S", "SIM"]:
        playing == True
    else:
        playing == False

    while playing:
        show_status(player_stats)
        choice = log("Choice")

os.system('cls')
log("Kauan")


#=================


while False:
    
    os.system('cls')
    game(player_stats)

    break
