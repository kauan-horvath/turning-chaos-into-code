"""
####################
# PROJECT: MODULAR CALCULATOR
####################

03/28 - Studying Software Engineering

MILESTONES:
- Create Pure Aritmetic []
- Input and Data Validation []
- Precedence Order? []
- Data persistance "M+" []

PROGRESS:
lambda in constants - SHORT EXPLAIN
shortif syntax - tell in a row
except Exception as var - Smart way to debug
    print{var}

FAILURES:
WHAT - SHORT EXPLAIN
    RIGHT VERSION
WHAT - SHORT EXPLAIN
    RIGHT VERSION

"""

####################################
import os  # noqa

a = 0
b = 0

OPERATIONS = {
    "+": a + b,
    "-": a - b,
    "*": a * b,
    "/": a / b if b != 0 else "Error: Div/0",
}

context = {"last_result": 0, "history": []}

# FUNCTIONS


def calculate(val1, val2, op):
    try:
        operation_function = OPERATIONS.get(op)
        if operation_function:
            return operation_function(val1, val2)
        return "Invalid Operator"

    except Exception as e:
        return f"Error: {e}"


def logic_function():
    pass


# Main Loop

if __name__ == "__main__":
    print("--- Modular Calculator Initializing ---")
    a = input("Digite um número:  ")
    op = str(input("Digite um operador: "))
    b = input("Digite outro número:  ")

    print(calculate(a, b, op))
