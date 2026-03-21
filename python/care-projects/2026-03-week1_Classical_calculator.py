#REFATORAÇÃO PROGRESSIVA - WEEK PROJECT (CALCULATOR)

# Imports | Constants | Dicts

import os

# Aux_Funct | Logic_Funct 

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return ">> ERROR, impossible divide by 0"
    return a / b

operator_list = {
    "somar": somar,"+":somar,
    "subtrair": subtrair,"-":subtrair,
    "multiplicar": multiplicar,"*":multiplicar,
    "dividir": dividir, "/":dividir
} #This dict can hold two keys, and call the respective function

def user_choice():
    try: 
        num_1 = int(input("choose a number: "))
        num_2 = int(input("choose a number: "))
        operator = str(input("Choose an operator: "))
        
        if operator in operator_list:
            chosen_funct = operator_list[operator]
            result = chosen_funct(num_1, num_2)
            print(f"\n >> Result: {result}")
        else:
            print(f"Operator: {operator}, NOT FOUND")
    except ValueError:
        print(f"ERROR: Enter a valid number")

# Main Loop

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("---- CALCULATOR ----")

        user_choice()

        keep_working = input("\n wanna keep calculating?  (y/n) ")
        if keep_working != "y":
            print("Thank you, good bye")
            break
            
#==========================================================
"""Progress LOG >> 03-21 - Perferct Base n Structure
    - Apply precise structure [OK]
    - Modular functions for each -basic- operator [OK]
    - Dictionaries for user choice [FAIL]
    - Troubleshoot for DIV/0 [OK]
    - Exhibit result [OK]

    This Week Progress:
    I learned how to map multiple keys to the same function within a dictionary to create a clean "dispatcher" system. Instead of using a complex toggle switch to stop the program, I implemented a simple while loop with a break condition. I also integrated a cross-platform os.system clear command. I'm very proud of how this structure turned out for a starting project!

    Dict Fail:
    # operator_list = {
    #     "sum":somar(num_1, num_2),
    #     '+':somar(num_1, num_2),
    #     "sub":subtrair(num_1, num_2),
    #     "-":subtrair(num_1, num_2),
    #     "mult":multiplicar(num_1,num_2),
    #     "*":multiplicar(num_1,num_2),
    #     "div":dividir(num_1,num_2),
    #     "/":dividir(num_1,num_2),
    # } The original thought was based on providing everything but the dictionary was calculating the numbers (With is not a problem) but i wasn't able to call the final results with the correct sintax
"""