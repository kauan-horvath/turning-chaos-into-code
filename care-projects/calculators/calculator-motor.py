'''
    ####################
    # PROJECT: MODULAR CALCULATOR
    ####################

    2026/03/28 - Studying Software Engineering

    MILESTONES:
    - Create Pure Aritmetic []
    - Input and Data Validation []
    - Precedence Order? []
    - Data persistance "M+" []

    PROGRESS:
    Lambda in constants - Research how it works [PEND]
    Shortif syntax - tell in a row the args is dope
    except Exception as var - Smart way to debug
        print{var}

    FAILURES:
    GET SYNTAX - How to precisely inform and retrieve
        dict.get(keyname, value)
            key = what yu want to search
            value = a fallback
            output = the right side of the key

    WHAT - SHORT EXPLAIN
        RIGHT VERSION
    
    '''

####################################
import os
os.system("cls" if os.name == "nt" else "clear")
a = 5
b = 2
op = "*"

OPERATIONS = {
    "+": a + b,
    "-": a - b,
    "*": a * b,
    "/": a / b if b!=0 else "Error: Div/0"
}

context = {}

while True:
    try:
        a = int(input("Digite um número:  "))
      
        op = input("Digite um operador: ") 

        debug = op in [OPERATIONS]
        print("debug", debug)

        if op not in [OPERATIONS]:
            ValueError =   False
        else:
            ValueError = True

        b = int(input("Digite outro número:  "))
        break

    except ValueError:
        print("Try again")

# FUNCTIONS

def calculate(val1, val2, op):
    try:
        result = OPERATIONS.get(op)
        return result
    
    except Exception as e:
        return f"Error: {e}"

def logic_function():
    pass

# Main Loop

if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        print("--- Modular Calculator Initializing ---\n")
        print(calculate(a,b,op))

        calculator_on = input("finish the program?  y | n")
        if calculator_on.upper() in ["Y","YES"]:
            break
    
    print("Fim do programa")
        

