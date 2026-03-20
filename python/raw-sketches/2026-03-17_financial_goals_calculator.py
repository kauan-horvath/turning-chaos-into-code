import os
os.system('cls')

# CALCULADORA DE INVESTIMENTO
    # 1. Perguntar o nome do user, o valor que ele quer juntar e o quanto ele guarda por mês
    # 2. quantos meses serao necessario para atingir a meta
    # 3. se menor que 12 meses informar que é proximo, se maior sugerir aumentar o aporte
    # 4. exibir um resumo formatado de tudo


#FUNÇÕES
def calculo(goal,apport):
    meses = goal/apport
    
    if meses < 12:
        print(f"Sua meta levará {meses} meses para ser concluído, parabéns agora falta pouco!")
    elif meses > 12:
        print(f"""
        Com o apport de R${apport}, Sua meta levará {meses} meses para ser concluído

        Metas que levam mais de um ano são mais difíceis de cumprir..""")

        adiamento = input(f"Você não gostaria de ajustar o apport mensal para encurtar o tempo? S | N  ")

        # if adiamento == "S" or "s" or "Sim" or "sim":
            #Correção, função upper in lista de opções
        if adiamento.upper() in ["S", "SIM"]:
            while True:
                try:
                    apport = int(input(f"Ótimo {name}, para a sua meta de R${goal}, qual o novo valor do apport mensal?  "))
                    break
                except ValueError:
                    print("Ops, digite apenas números")
            meses = goal / apport
        else:
            print("Perfeito, de passo a passo se percorre a estrada de mil kilômetros")
    else:
        print("Valores inválidos")
        
    return meses, apport

def resultados(meses):
    print(f"""
            ============== RESUMO DO INVESTIMENTO:\n
            Usuário: {name}
            Meta: R${goal}
            apport: R${apport}

            Tempo até ser concluída: {meses} meses
            ======= Parabéns pelo seu investimento
        
        """)
        
#INTERROGAÇÃO
working = False

print("== #CALCULADORA SIMPLES DE INVESTIMENTO ==")
working = input("Podemos começar? S | N  ")

if working.upper() in ["S", "SIM"]:
    working = True
else:
    working = input("Ok, me avise se mudar de ideia...")
    if working != None:
        working = True


while working == True:
    name = str(input("Seja bem vindo, qual o seu nome?  "))
    while True:
        try:
            goal = int(input(f"Olá {name}, qual sua meta total?  "))
            break
        except ValueError:
            print("Ops, digite apenas números")

    while True:
        try:
            apport = int(input(f"Certo {name}, para a sua meta de R${goal}, qual o valor do apport mensal?  "))
            break
        except ValueError:
            print("Ops, digite apenas números")

    resultado_meses, apport = calculo(goal,apport)
    #gemini o valor do apport nao ta atualizando o resultado meses criando um erro de tempo desatulizado
    resultados(resultado_meses)

    keep_working = input("Deseja fazer mais cálculos? S | N  ")
    if keep_working.upper() in ["S", "SIM"]:
        resultado_meses = calculo(goal,apport)
        resultados(resultado_meses)
    else:
        working = False

if working == False:
    print("Obrigado por usar a calculadora de investimentos\n \n \n \n")