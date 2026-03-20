#Treino de escopo e estrutura.

""" Modularidade, limpeza e previsibilidade """

""" best order:
imports
constantes
dicts
fun aux
fun log
code
"""

#Treino 1 - Gerenciador de inventário
""" Criar, remover e visualizar itens"""

#Marco 1 - um dict de inventory
#Marco 2 - func adicionar itens
#Marco 3 - func de remover itens
#Marco 4 - func de ver satatus
#Marco 5 - func de log

#eliminatório: Proibido uso de global, inventario negativo, best order elements

# Imports =====================

import os
import random

# Constantes =====================
    #gemini como faço para determinar que algo é uma constante?
USERNAME = None
MAX_GOLD = 9999
AXE_TYPE = []


# Dictionaries =====================

inventory = {
    "Gold":0,
    "New_item":[]

}

items_to_buy = {
    "AXE": 20,
    "FISHING_ROD": 50,
    "TREASURE_CHEST":100
}

# Auxiliar Functions =====================

def buy_itens():
    #Uma especie de função de compra
    """ 1 - lê o inventário
        2 - lê o item e o "preço"
        3 - subtrai o gold e add 1 item """

def remove_itens():
    pass

def show_status(p):
    print("\n Adventurer, here is your inventory: ")
    for item, quantity in p.items():
        
        if item == "New_item":
            pass
        else:
            print(f"\n {item} | Amount: {quantity}")
        #gemini me ensina a sintaxe de chamar chave e valor? quero imprimir o item, a quantidade, mas nao sei chamar direito [ooo dei um google e acho que achei]

              


# Logical functions =====================
    #Gemini, qual a diferença de função lógica para função auxiliar?

def log(option, value=0):
    texts = {
        "presentation":"\n Welcome traveler, here you'll need to work, gather money, \n and buy new things to achieve goals and conquer this world!",
        "verify_name":f"Wonderfull, your name  >> {value} <<, will be part of the history books!",
        "start_journey":f"\n {value}, your journey begins with a few choices:",
        "choices":"\n 1 - Open Inventory | \n 2 - Developing |",
        "NEW_TEXT":[]


    }

    print(texts.get(option, "!TEXTO NAO ENCONTRADO"))

# Main loop =====================
while True:
    os.system('cls')
    confirm_name = True
    
    #dá boas vindas
    log("presentation")

    #anota o nome e checa para personalização dos logs
    #CHANGE_AFTER
    USERNAME = "WARRIOR_NAME"
    #USERNAME = input("Tell us your name warrior?  ")
    #log("verify_name", USERNAME)
    

    #CHANGE_AFTER
    while confirm_name == False: 
        #gemini, acha que devo fazer confirm_name uma função ao inves de um loop direto no main? me ensina sobre essa estruturação do codigo
        confirm_name = input("You wanna change your name?  ")

        if confirm_name.upper() in ["S", "SIM"]:
            USERNAME = input("Tell us your name again?  ")
        else:
            confirm_name = False
            break

    log("start_journey",USERNAME)
    log("choices")
  
    choice = int(input("\n Choose a number:  "))
    
    while not choice == False:
        

        try:
            if choice == 1:
                show_status(inventory)
            
            elif choice == 2:
                print("\n Developing option")

        except ValueError:
            print("wrong option, pick a number")
            #gemini, não sei fazer o except para string "um" ou "open inventory"

        choice = False

    #fim do loop do game
    #CHANGE_AFTER
    end_game = "S"
    #end_game = input("\n deseja encerrar o jogo?  ")
    if end_game.upper() in ["S", "SIM"]:    
        break
    else:
        pass

if __name__ == "__main__":
    print("\n fim do jogo <<<<<<<<<<<<<<<<<<<<<< \n")