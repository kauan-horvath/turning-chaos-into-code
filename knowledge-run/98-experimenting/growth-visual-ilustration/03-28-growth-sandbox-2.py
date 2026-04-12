"""
####################
# SANDBOX: THE PYTHON TREE
####################

DATE - 28/03/2026

MILESTONES:
- MILE1 [X] The Seed: Handle inputs and convert them to 'Growth Power'.
- MILE2 [X] The Sprout: Create a visual ASCII representation of the growth.
- MILE3 [ ] The Harvest: Calculate total value and store in 'Vault'.

PROGRESS:
- Perfect implemented os.system by head and for a clear animation
- Consulted the syntax from a previous project to reproduce the conditional fallback for growth stages
    - Known as [Stair of reverse verification] on the Emojis choice

FAILURES:
- Unreachable break: put a redundant break after a return
- logig redundance: checking the dict and then making a conditional
- Time Management: exceeded the 45min goal.
    RIGHT VERSION: Break the project into even smaller micro-milestones

"""

####################################

import os
import time

# O cofre onde seus tesouros ficam guardados
context = {
    "vault": [],
    "tree_stages": {0: "🫘", 25: "🌱", 50: "🌿", 75: "🌳", 100: "🌳🌳🌳"},
}

# FUNCTIONS

# def get_investment_data():

#     while True:
#         try:
#             waiting_time = int(input("from 0 to 100, choose a initial period  "))
#             return waiting_time
#         except ValueError:
#             print("Invalid choice, choice a Number")


def animate_growth(time_steps):

    while time_steps < 101:
        # visual = context["tree_stages"].get(time_steps)
        visual = context["tree_stages"].get(
            time_steps,
            (
                "🌳🌳🌳"
                if time_steps > 80
                else (
                    "🌳"
                    if time_steps > 60
                    else "🌿" if time_steps > 40 else "🌱" if time_steps > 20 else "🫘 "
                )
            ),
        )
        os.system("cls" if os.name == "nt" else "clear")
        print("\n---- Python Planting ----")
        print(f"[ Time: {time_steps} | Stage: {visual} ] \n\n")
        time.sleep(0.2)

        time_steps += 1


# Main Loop

if __name__ == "__main__":
    for i in range(3):
        os.system("cls")
        print("\n- Initializing Python Planting -\n\n")
        time.sleep(2)
        animate_growth(0)
        os.system("cls")
