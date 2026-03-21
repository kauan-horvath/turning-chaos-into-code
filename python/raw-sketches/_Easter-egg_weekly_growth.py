import os
import time

STAGES = {0: "🌱", 5: "🌿", 10: "🌳",20:"🍎"}

def grow():
    level = 0
    while level <= 20:
        os.system('cls' if os.name == 'nt' else 'clear')
        visual = STAGES.get(level, "🌿" if level > 5 else "🌱")
        print(f"Planta: {visual} | Nível: {level}")
        
        if level == 20: 
            print("Growing is a proccess") 
            break
        level += 1
        time.sleep(0.5)

if __name__ == "__main__":
    grow()