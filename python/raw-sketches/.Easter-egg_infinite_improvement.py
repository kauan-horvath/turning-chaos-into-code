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
                print(f"\n\n🔥 Vegeta says: IT'S OVER EIGHT THOUSAND!!!!!!!!!!!!!!!!!!!!!!!!!!! 🔥\n")
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
