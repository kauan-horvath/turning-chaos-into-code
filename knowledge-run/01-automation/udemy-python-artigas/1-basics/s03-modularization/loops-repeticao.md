# 📂 Seção 14 : Estruturas de Repetição (While, For)

## 📑 Loopings

> **Status:** 🟡 ANDAMENTO | **Data:** 19/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../../0-organization/python-artigas-home.md) |
| :------------------- | :---------------------------------------------------------------- |
| &#8657; **Anterior** | [ANTERIOR](./condicionais-if-else.md)                             |
| &#8659; **Próximo**  | [PROXIMO](./arquivo2.md)                                          |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 01](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28730276#overview):** Loop While — _(10min)_
- [✅] **[Vídeo 02](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28730280#overview):** Loop For — _(10min)_
- [✅] **[Vídeo 03](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28730286#overview):** Range() — _(10min)_
- [✅] **[Vídeo 04](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794040#overview):** Break — _(10min)_
- [✅] **[Vídeo 05](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794056#overview):** Continue — _(10min)_
- [✅] **[Vídeo 06](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794062#overview):** Loop Aninhados — _(6min)_
- [✅] **[Vídeo 07](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794064#overview):** Declaração de passagem — _(5min)_

> **Nota rápida:** [Estruturas de repetição]

---

### 📝 Anotações e Conceitos Chave

#### 1. Loop While

- informa a estrutura do loop enquanto True
- informa sobre o loop infinito.
- ⚠️Atenção à lógica de parada
- Exemplo de sintaxe ou regra:

```python
    #exemplo
    tiro = 100

    # while tiro < 101:
    #     print("POW")
    #     tiro -= 1 #só diminuir vai tornar negativo que ainda é menor portanto True infinito

    #sem incremento gera loop infinito
    while tiro < 101 and tiro > 0:
        print("POW")
        tiro -= 1 #dessa forma o loop nunca para


    print("carregando rifle")

    while tiro > 1000:
        print("Bazooca")
        tiro -= 100
        #nunca executa
    else:
        print("pegar a bazooca")
        tiro += 1000
        #executa se o while for false
        #⚠️ MUITOS ESQUECEM DO ELSE WHILE

```

#### 2. Loop For

- informa que percorre dados iteráveis (com index).
- informa que o loop acaba ao fim dos iteraveis.
- reforça que pode iterar em seq de caracteres (str)

- Exemplo de sintaxe ou regra:

```python
    #exemplos

    vegeta = ["AAA", "GALICK HOOOO "]

    for grito in vegeta:
            print(10 * grito)

    print("Vegeta ironico:")
    for letra in "GALICK HOO":
        print(letra) #return G depois A e etc

```

#### 3. Função Range

- informa que retorna uma sequencia de números a partir do menor ao maior.
- relembro que range() é off by one por começar em 0, indo de min a max -1.
- informa um terceiro parametro de range (intervalo de incremento)
- Exemplo de sintaxe ou regra:

```python
    #exemplos
    for turn in range(11):
        print(f"eu começo em 0 até 10: {turn}")

    for turn in range(2, 6):
        print(f"my turn is: {turn}")
        #return de 2 a 5

    #LOGICA DE STEP
    for dezena in range(0, 101, 10):
        print(f"O decimental é: {dezena}")

```

#### 4. Break | Continue | Aninhamento de loop | pass

- informa que o break interrompe repetições.
- informa que se houver um else após o break, o else é ignorado.
- informa que continue interrompe mas pulando pro proximo iterador ao inves de parar o loop
- informa que pass apenas pula um iteração vazia sem dar erro
- Exemplo de sintaxe ou regra:

```python
    #exemplo
    murros = 1

    while murros < 11:

        print("toma um murro")
        murros += 1

        if murros == 7:
            print("Voce ja levou 7 murros")
            print("e por hoje está bom")
            break

    golpes_marciais = ["Voadora", "Hadouken", "Chute", "Abraço"]

    for golpe_no_ar in golpes_marciais:
        #ele itera os golpes no ar, mas nao faz nada e nao da erro
        pass

    for golpe in golpes_marciais:
        print(golpe)
        if golpe == "Chute":
            print("Parei Chute, é golpe baixo")
            break

    #vingança
    vinganca = False

    for golpe in golpes_marciais:
        print(golpe)
        if golpe == "Chute":
            print("Parei Chute, é golpe baixo")
            vinganca = True
            continue
            #⚠️ NAO CONTINUA ESSA ITERAÇÂO E PULA PRA PROXIMA
                #return abraço

    #loop aninhados
    while vinganca == True:
        for vezes in range(0, 11):
            print(f"Eu te devolvo {golpe}")
            if vezes == 10:
                vinganca = False
                break

    #NESTED LOOP
    #⚠️ Muito util [Entra no for 1, e faz todos do for 2, e repete]
    prim_nome = ["JOÃO", "MARIA", "JOSÉ"]
    sobrenomes = ["DA SILVA", "SAURO"]

    for nome in prim_nome:
        for sobre in sobrenomes:
            nome = nome + " " + sobre
            #sobrescrevendo para gerar o nome completo
        print(nome)
            #return JOAO DA SILVA SAURO

        #Aprendi no The farmer was replaced
            #função de linnear sweep com callback
            #callback atua como um minimap da função geral
                #a geral faz o nested loop, e o cbk faz microfunções dentro
        def lin_sweep(callback):
            for linha in range(get_world_size()):
                for coluna in range(get_world_size()):
                    callback() #callback de ações
                move(North)
            move(East)
        def clap_hands_callback():
            print("clap your hand")

        lin_sweep(clap_hands_callback)
            #return em cada stop clap a hand
```

### x. 🛠️ Revisões

::to-review:: 21-04-2026 :: Loops While e For, Nested Loop ::
