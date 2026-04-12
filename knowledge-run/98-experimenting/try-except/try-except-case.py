"""
#############################
# Study case of Try Except
#############################

DATE - 2026-04-03

MILESTONES:
- Study and apply the common excepts [ ]
- Interact with a txt file [ ]
- MILE3 [ ]

PROGRESS:
WHAT - SHORT EXPLAIN

FAILURES:
WHAT - SHORT EXPLAIN
    RIGHT VERSION: Explain fix
"""

####################################
import os

CONST = None

context = {}

# FUNCTIONS
global number


def block_div0():
    try:
        number = int(input("Insert a number: "))
        result = 10 / number

        print(f"The result is: {result}")

    except ZeroDivisionError:
        print("ERROR: You cant divide a number by 0")

    except ValueError:
        print("You have to write a number")

    except Exception as e:
        print(f"Unexpected Erros: {e}")


def finally_function():
    try:
        # write the path
        int(input("Insert a number: "))

    except ValueError:
        # only if there's error in try
        print("Pls insert a number")

    else:
        # olny if try without error
        print("You've used a valid number")

    finally:
        print("No matter what youve wrote finally always come")


# MAIN LOOP

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    block_div0()
    finally_function()
