# 🛠️ Raw Sketches & Experimental Scripts

This directory is a dedicated space for my **initial coding drafts, logic exercises, and unfinished projects**. 

While the core of this repository focuses on refined solutions, I believe that showing the "raw" process is essential to demonstrate growth, troubleshooting skills, and consistent daily practice.

## 📌 What to find here:
- **Daily Logic Drills**: Quick scripts to test specific Python concepts.
- **WIP (Work in Progress)**: Projects currently being refactored or expanded.
- **Legacy Training**: My very first steps in Python, kept here for historical context.

## 🚧 Status: Unrefined
The code in this folder may contain:
- Internal comments in Portuguese/English mix.
- Non-standard naming conventions.
- Bugs or edge cases yet to be handled.

---
*“Done is better than perfect. Refinement comes with iteration.”*

```Python
#actual working code, copy and paste to try it!
import time

# Kauan Horvath - The Saiyan Evolution + 🥚

def grinding_skill_points():
    power_level = 1000.0
    vegeta_triggered = False # Trava para o grito não repetir infinitamente
     
    print("\n[ ERROR: SAIYAN EVOLUTION OVERFLOW DETECTED ]")
    
    try:
        while True:
            # Mostra o nível de poder atualizando na mesma linha
            print(f"increasing_power_level... {power_level:.1f}", end="\r")
            
            # O Trigger do Vegeta
            if power_level >= 8000 and not vegeta_triggered:
                print(f"\n\n🔥 Vegeta says: IT'S OVER EIGHT THOUSAND!!!!!!!!!!!!! 🔥\n")
                vegeta_triggered = True # Garante que ele só grite uma vez
                time.sleep(1) # Pausa dramática após o grito
            
            power_level += 100.0
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        status = "Super Saiyan" if power_level > 8000 else "Junior Warrior"
        print(f"\n\nFinal Power Level: {power_level:.1f} ({status} Mindset)")

if __name__ == "__main__":
    print("Feel free to contact me if you're looking for a high-potential developer!")
    grinding_skill_points()

    
