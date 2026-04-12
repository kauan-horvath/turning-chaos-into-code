# 📂 Seção 02 : Coleção de Dados

## 📑 Coleções e Listas

> **Status:** 🟡 ANDAMENTO | **Data:** 11/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../Home.md) |
| :------------------- | :------------------------------- |
| &#8657; **Anterior** | [ANTERIOR](./arquivo1.md)        |
| &#8659; **Próximo**  | [PROXIMO](./arquivo2.md)         |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 01](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28490448#content):** Listas Python — _(10min)_
- [✅] **[Vídeo 02](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28490456#content):** Acessando Itens da Lista — _(12min)_
- [✅] **[Vídeo 03](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28490460#content):** Alterar itens da lista — _(11min)_
- [✅] **[Vídeo 04](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28490466#content):** Adicionar itens da lista — _(7min)_
- [✅] **[Vídeo 05](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28490480#content):** Remover itens da — _(00min)_'
- [✅] **[Vídeo 01](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28490494#content):** Compressão de lsitas — _(16min)_
- [✅] **[Vídeo 02](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28490502#content):** Classificação de listas — _(16min)_
- [✅] **[Vídeo 03](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28490512#content):** Copiar listas — _(7min)_
- [✅] **[Vídeo 04](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28528761#content):** Juntar listas — _(6min)_
- [✅] **[Vídeo 05](https://www.udemy.com/course/python-completo-e-profissional/learn/quiz/5346082#content):** Teste — _(00min)_

> **Nota rápida:** [Variações de uso e funções de listas, ironicamente eu ainda nao domino listas com a precisão que eu gostaria então vou anotar ostensivamente.]

---

### 📝 Anotações e Conceitos valor

#### 01. Apresentação Listas

- Informa que guardamos uma coleção de dados.
- Informa que são indexados e ordenados.
- Informa que são mutáveis

```python
# Sintaxe
    sacola_mercado = ["pão", "ovo", "mortandela"]
    tamanho = len(sacola_mercado) #exibe 3

    sacola_mercado.append("maçã")
    #adicionar ao final e mudar a lista original
    tamanho = len(sacola_mercado) #exibe 4

    sacola_variada = ["1", True, "três", sacola_mercado]
    #uma lista pode conter todos tipos de dados inclusive variados e outras listas

    type(sacola_mercado) #retorn <class list>

    #construtor list()
    salsicha_vegana = False
    hot_dog_vegano = False

    #⚠️ IMPORTANTE
    sacola_vegana = list((salsicha_vegana, hot_dog_vegano))
    #list((agrupramento)) necessário agrupar em () dentro de list
    #para não ser identificado como dois argumentos

```

#### 2. iNDEXAÇÃO

- Informa sobre indexação numerada.
- Informa sobre indexação negativa.
- Exemplo de sintaxe ou regra:

```python
    # Index
    import random
    pessoas = ["josé-0", "Maria-1", "joão-bat-2", "jesus-3", "thiago-4"]
    ran_index = random.randrange(0, len(pessoas)) #len(max) retornara 5 e da -1 contemplando todos
    #index
    messias = pessoas[3] #retorna jesus-3

    #ate o final/começo
    irmãos = pessoas[3:] #retorna de 3 pra frente
    pais = pessoas[:2] #retorna ate o index 1 porque o 2 exclue

    #intervalo
    amigos_e_irmãos = pessoas[2:4]

    #índice negativo
    SIAP = pessoas[-5:-3] #equivale a 0:2 com o 2 excluso

    #funções e acessos
    batata_quente = pessoas[ran_index] #retorna o nome do index sorteado
        #forma alternativa ⚠️formato padrão para escolha aleatoria (sem index)
        batata_quente = random.choice[pessoas]

    #perguntando se está na lista
    if "jesus-3" in pessoas:
        print("O messias nasceu")
        #existem formas melhores de tratar a string mas nao vou entrar nisso agora

```

#### 3. Alterar itens da Lista

- Informa que index[n] = "novo_valor" irá sobrescrever o dado da lista.
- informa que funciona em intervalos.
- Exemplo de sintaxe ou regra:

```python
  # ó o apocalipse vino mlk

    #alterando pais com intervalo
    pessoas[0:2] = ("Satanás", "Perséfone")

    #alterando com index específico
    pessoas[2] = "Baphomet"

    pessoas[3] = "Anticristo" #altera no local do index
    pessoas[4] = "Conquista, Guerra, Fome, Morte" #altera tiago por tudo isso

    #metodos para lidar sem alterar a lista existente
    pessoas.insert(2, "Belzebulb") #não remove baphomt, mas adiciona esse no index 2 a mais

    print(pessoas)
    #return ["Satanás", "Perséfone", "Belzebulb", "Baphomet", "Anticristo", "Conquista, Guerra, Fome, Morte"]

```

#### 4. Adicionar itens na lista

- Informa sobre o append() para adiciona a fim.
- informa sobe o insert() que adiciona com indice e move os outros.
- informa o extend() que aumenta a lista com vlaores iteraveis (literal, vars)
  - ⚠️ sutil diferença entre extend() e extend([])
- Exemplo de sintaxe ou regra:

```python
  #Meu heroi nao usa capa, ele usa anéis e selos
    vaso_de_bronze = []

    #Goetia e trabalhos de salomão
    vaso_de_bronze.append("Lampada: Asmodeus (Da Luxúria)")
    vaso_de_bronze.insert(0,"Vaso de Couro: Ephippas (Do Vento)")

    #usando extend literal e var
    the_first_demon = "Selo de Salomão: Ornias (O primeiro)"
    resto = ["Agares (O Duque)", "Vassago (O Príncipe)", "Shamir (Um Verme)", "Etc..."]

    vaso_de_bronze.extend(["Estátua Trivia: Belial (O que responde)"]) #necessário fornecer em list [] para nao extender soletrado

    vaso_de_bronze.append(the_first_demon) #assim adiciona o texto todo
        #vaso_de_bronze.extend(the_first_demon) #assim vai adicionar soletrado, letra por letra
    vaso_de_bronze.extend(resto) #resto sem [] para nao aninhar 2 listas

    def curiosidade(recipiente):
        if "Shamir (Um Verme)" in recipiente:
            print("O unico que não é um demônio")

    curiosidade(vaso_de_bronze)
    print(vaso_de_bronze) #retorna:
    ['Vaso de Couro: Ephippas (Do Vento)', 'Lampada: Asmodeus (Da Luxúria)', 'Estátua Trivia: Belial (O que responde)', 'Selo de Salomão: Ornias (O primeiro)', 'Agares (O Duque)', 'Vassago (O Príncipe)', 'Shamir (Um Verme)', 'Etc...']
```

#### 5. Remover itens da lista

- Informa o método remove() atraves de um item identico.
- informa sobre o pop() remove atraves do indice.
- informa sobre o metodo del (uma palavra valor)
  - que remove de algumas formas diferentes
  - tambem pode apagar a lista toda
- informa sobre o metodo clear()
  - remove todos os itens mas nao apaga a lista
- Exemplo de sintaxe ou regra:

```python
  # Soleyman joga o vaso no Lago da babilônia
    lago_profundo = vaso_de_bronze.copy()
        #quero o vaso de volta
        vaso_de_bronze.clear() #remove tudo mas ainda tem uma lista = [] vazia
            #metodo .copy para ter duas listas uma para del lago e outra para vaso.clear

    lago = lago_profundo # Apelido (Referência de memória)

  #apagando da realidade
    lago.remove("Shamir (Um Verme)")
    lago.pop(0) #remove Ephipas
    lago.pop() #remove o ultimo

    #metodo del
    del lago[1] #remove Belial
    del lago #remove os dados de lago e a var lago em si (Mas não lago_profundo por ser apenas referncia)

```

#### 6. Iteração em listas

- Usando o loop for
  - usar o i para iterar pelo indice
- Usando o loop while

- Exemplo de sintaxe ou regra:

```python
  # Iterando em listas

    bate_oque = ["Betsabá", "Betsabé", "Bathsheba", "Casada", "Gostosa"]

    #Davi tentando muito
    for tentativa in bate_oque:
        #a cada loop repete o bloco de código
        #encerra quando a lista acabar
        print(tentativa) #imprimir uma valor diferente a cada loop
    print("Eu não desisto até perder meu Hallelujah")

    for i in range(len(bate_oque)):
        #iterar pelas vezes do tamanho da lista
        print(bate_oque[i]) #vai imprimir o indice da vez

    #=====================

    i = 0
    while i < 5: #repete ate o tamanho da lista
        print(bate_oque[i])
        i += 1 #necessario incrementar manualmente senao imprime sempre 0

    [print(i) for i in bate_oque] #compressão de lista ⚠️Pesquisar mais no futuro

```

#### 7. Compressão de Listas

- informa que é possível criar uma nova lista com um pedaço da outra.
- EXPLICAÇÃO.
- Exemplo de sintaxe ou regra:

```python
  # Treinando compreesão de lista
    celestiais = ["Deus", "Jesus", "Miguel", "Gabriel", "Uriel", "Kal-el"]
    anjos = [] #precisa existir para o for abaixo na dar erro

    sufixo = "el"
    for valor in celestiais:
        if sufixo in valor:
            anjos.append(valor)

    #literal = [x for x in nomes if "el" in x]
    anjos = [valor for valor in celestiais if sufixo in valor]
    impostor = [valor for valor in celestiais if "Kal" in valor]

    anjos_sem_impostor = [valor for valor in celestiais if valor != "Kal-el"]
        #usar o != só para valores identicos
    #manipulando os valores da lista
    ANJOS_COM_G_MAIUSCULO = [valor.upper() for valor in celestiais]

    Deus_eh_pai_nao_eh_padrasto = [valor if valor == "Deus" else "Celestial" for valor in celestiais] #substitui tudo por "Celestial" exceto gabriel
        #Mantenha o valor 1 se ja for 1, e se não for transforme em 2
```

##### Eu sei que voce tambem nao entendeu nada entao

- Pedi pra IA gerar uma tradução das variações de compressão
- Mas escrito de forma literal

```Python
# Lista Base para os exemplos
lista = ["A", "B", "Texto Exato", "Palavreado", "Proibido", "Alvo"]

# Lista Base para referência
lista = ["A", "B", "Texto Exato", "Palavreado", "Proibido", "Alvo"]

# 1. CÓPIA SIMPLES (Loop Básico)
nova_lista = [item for item in lista]
# Literalmente: [ O que vai sair | Loop ]
#               [ item | for item in lista ]

# Explicação: O primeiro 'item' é o resultado. O loop percorre a lista e entrega cada valor sem alterar nada.


# 2. FILTRO "CONTÉM" (Busca Parcial)
contem_palavra = [item for item in lista if "Palavra" in item]
# Literalmente: [ O que vai sair | Loop | Condição (Se contém) ]
#               [ item | for item in lista | if "Palavra" in item ]

# Explicação: O item só é entregue para a nova lista se o trecho "Palavra" existir dentro dele.


# 3. FILTRO "IDÊNTICO" (Igualdade Total)
identico = [item for item in lista if item == "Texto Exato"]
# Literalmente: [ O que vai sair | Loop | Condição (Se igual) ]
#               [ item | for item in lista | if item == "Texto Exato" ]

# Explicação: O item só é entregue se for 100% igual ao texto entre aspas. Útil para buscas exatas.


# 4. FILTRO "DIFERENTE" (Exclusão)
sobreviventes = [item for item in lista if item != "Proibido"]
# Literalmente: [ O que vai sair | Loop | Condição (Se diferente) ]
#               [ item | for item in lista | if item != "Proibido" ]

# Explicação: O loop entrega todos os itens, exceto aquele que for exatamente igual ao valor proibido.


# 5. TRANSFORMAÇÃO (Se for X, vire Y)
transformado = [item if item == "Alvo" else "Substituto" for item in lista]
# Literalmente: [ Regra (Se/Senão) | Loop ]
#               [ item if item == "Alvo" else "Substituto" | for item in lista ]

# Explicação: Quando há mudança de valor (ELSE), a regra vem para a frente. Se for o Alvo, mantém; senão, troca pelo substituto.
```

```python
# Boss final
    to_perdido = [["a","b"],["c","d"],["e","f"]]

    boss_final = [[valor[i] for valor in to_perdido] for i in range(1)]
    #ele cria um "carimbo triplo" com os valor do index de cada loop
        #range(0) - []
        #range(1) - [a, c, e]
        #range(2) - [a, c, e], [b, d, f]

```

#### 8. Classificação de Lista

- Informa sober o metodo sort().
  - Para classificação ascendente.
- Informa sobre a palavra chave reverse
- informa sobre a palavra chave abs()
  - em string classifica com distincao de maic e minus
  - e o uso de key para classificar por proximidade
  - keu = str(lower()) nao pede funcao e classifica por alfabetica sem distinção
    - porque aplaina tudo como lower (e enxerga igual)
  - metodo reverse()
    - nao é alfabetica e sim "ao contrario do que esta"

- Exemplo de sintaxe ou regra:

```python
  # Uso do métodos de classifciação

# A tropa chega bagunçada
soldados = ["zulu", "Alfa", "bravo", "Charlie", "delta"]
forca_inimiga = [100, 40, 4, 5, 2, 3, 1]

forca_inimiga.sort() #(1, 2, 3, 4, 5, 40, 100).
# [ Método .sort() | Altera a lista original permanentemente ]

forca_inimiga.sort(reverse=True) # (100, 40, 5, 4, 3, 2, 1).

soldados.sort() #['Alfa', 'Charlie', 'bravo', 'delta', 'zulu']
# Explicação: No "ASCII", Maiúsculas têm prioridade sobre Minúsculas.
# O "bravo" ficou atrás do "Charlie" porque o 'b' é minúsculo.

soldados.sort(key=str.lower) #['Alfa', 'bravo', 'Charlie', 'delta', 'zulu']
# Explicação: O 'key' aplica uma regra ANTES de comparar.
# Ele "enxerga" todo mundo como minúsculo só para organizar, mantendo o nome original.

# KEY COM FUNÇÃO PERSONALIZADA (Proximidade do Alvo)
def proximidade_do_alvo(n):
    return abs(n - 50) # abs() remove o sinal de negativo (distância pura)

forca_inimiga.sort(key=proximidade_do_alvo) #[40, 5, 4, 3, 2, 1, 100]
# Explicação: Quem está mais perto de 50 (o alvo) ganha a frente da fila.
# 40 está a 10 de distância. 100 está a 50 de distância (fica por último).

soldados.reverse() #resultado delta, Charlie ...
# Explicação: Não olha ordem alfabética. Ele apenas pega a lista atual e vira de ponta-cabeça.

```

#### 9. Copiar e juntar Listas

- informar que atrbiuir uma a outra não é copiar é referência.
- informa o metodo copy().
- informa sobre o operador de concatenação "+"
  - com um loop adicionando uma na outra
- Exemplo de sintaxe ou regra:

```python
# A Ficha Original (O Cofre)
lista_original = ["Agente A"]
referencia_lista = lista_original #Não criou uma lista nova. Se você "queimar" o Agente A aqui,
# ele morre na lista_original também. Eles compartilham a mesma memória.

# A SEGURANÇA: Método .copy()
copia_lista = lista_original.copy() #Criou um clone independente.
# Alterar 'copia_lista' não afeta em nada a 'lista_original'.

copia_lista.append("Agente B") # Agora a cópia tem ["Agente A", "Agente B"]

# A ALTERNATIVA: list()
outra_forma_de_copia = list(lista_original) # Recebe os dados em um novo recipiente.

# ---------------------------------------------------------

# FUSÃO DE DADOS: Operador "+"
concatenar_listas = lista_original + copia_lista #["Agente A", "Agente A", "Agente B"]
# Explicação: Ele cria uma TERCEIRA lista unindo as duas anteriores.

# FUSÃO POR ITERAÇÃO (Loop Industrial)
[valor.append(chave) for chave in lista_original] #Isso é o mesmo que injetar os itens de uma lista dentro da outra,
# um por um, usando o loop para "alimentar" a lista de destino.
```

#### x. Teste

- As listas são usadas para armazenar vários itens em uma única variável | True
- Os itens da lista são indexados, o primeiro item tem índice [1] | False

### x. 🛠️ Revisões

::to-review:: 14-04-2026 ::Listas::

<!-- Criar memes melhores para 8 e 9 quando tiver cerebro pra isso-->

💻 Notas / Código

```python
# Seu código aqui
```
