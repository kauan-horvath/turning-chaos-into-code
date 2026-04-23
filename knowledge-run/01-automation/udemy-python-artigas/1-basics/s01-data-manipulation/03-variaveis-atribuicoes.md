# 📂 **Seção 03:** Variáveis e Atribuições

## 📑 [Variaveis e Atribuições]

> **Status:** 🟢 CONCLUIDO | **Data:** 08/04/2026

| **🏠 HOME**          | [Retornar ao Início](../../0-organization/python-artigas-home.md) |
| :------------------- | :---------------------------------------------------------------- |
| &#8657; **Anterior** | [Introdução](../s00-into-config/02-sintaxe-primeiros-passos.md)   |
| &#8659; **Próximo**  | [Primeiros passos](./04-tipos-dados.md)                           |

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 07](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408398#notes):** [Apresentando variáveis] — _(16min)_
- [✅] **[Vídeo 08](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408402#notes):** [Nomes das Variáveis] — _(10min)_
- [✅] **[Vídeo 09](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408498#notes):** [Atribuir Valores] — _(10min)_
- [✅] **[Vídeo 10](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408518#notes):** [Valores de Saída] — _(11min)_
- [✅] **[Vídeo 11](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408528#notes):** [Escopo Global e Local] — _(20min)_
- [✅] **[Teste](https://www.udemy.com/course/python-completo-e-profissional/learn/quiz/5346070#notes):** [Quick Followup] — _(0 min)_
- [✅] **[Exercício](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29393200#notes):** [Exercício de Armazenamento] — _(10 min)_

> **Nota rápida:** [O Professor acaba provando como variáveis e tipos primitivos são conhecimentos muito próximos]

---

### 📝 Anotações e Conceitos Chave

#### 1. [Declarando Variáveis]

- Informa sintaxe básica de atribuição vs comparação: `=` vs `==`
- Informa que variáveis não têm tipo base, e que podem mudar a qualquer momento: `var_str = "teste"` > `var_str = 10` (agora é int)
- Apresenta o **casting**: A capacidade de forçar uma variável a ser de outro tipo primitivo `int(var_str)`
- Apresenta a função `type()` para checar o tipo primitivo de um dado

- Exemplo de sintaxe ou regra:

```python
idade = 29 # Tipo int
nome = "kauan" # Tipo string

#casting de int > str
idade_string = str(idade) #como se: "29"
print(type(idade_string)) #retornará (Str)

#casting de str > float
idade_float = float(idade) #como se: 29.0
print(type(idade_float)) #retornará (Float)

#casting de float > int
idade_int = int(idade_float) #como se: 29
print(type(idade_int)) #retornará (Int)
```

#### 2. [Nomes das Variáveis]

- Informa que Python é **"Case sensitive"**: ele diferencia lowercase de uppercase
- Informa as regras de nomes:
  - O nome não pode iniciar com número
  - O nome não pode ser uma palavra reservada (ex: `if`, `for`, `class`)
  - O nome não pode ter separação no meio com traço, espaço, ou símbolo exceto: `_` (Underscore)
  - Letras maiúsculas ou minúsculas interferem no resultado

- Informa os Cases ou Typecase:
  - **Snakecase**: `tudo_minusculo_separado_underscore` (Padrão para variáveis em Python)
  - **Camelcase**: `cadaPalavraExcetoPrimeiraMaiuscula`
  - **Pascalcase**: `TodasPalavrasInclusivePrimeiraMaiuscula` (Padrão para Classes em Python)

- Exemplo de sintaxe ou regra:

```python
nome = "kauan"
NOME = "doppleganger"

#exemplos de erros
2myvar = False    #erro: começa com número
my-var = False    #erro: separação com traço
my var = False    #erro: separação com espaço
continue = False  #erro: palavra reservada (minúscula)
```

#### 3. [Atribuir valores]

- Informa os operadores de atribuição: `=`
- Informa a atribuição sequencial: `var1, var2 = val1, val2`
- Informa a atribuição coletiva: `var1 = var2 = var3 = "valor"`
- Informa uma descompactação:
  ⚠️ Se o número de variáveis for diferente do número de valores na coleção, retornará `ValueError`.

- Exemplo de sintaxe ou regra:

```python
#==== Descompactação de uma Coleção simples:
diretores = ["Goddard", "Lanthimos", "Villeneuve"]
diretor_cult, diretor_incompreendido, diretor_favorito = diretores
```

#### 4. [Concatenação de Variáveis]

- Concatenação de Strings: `+` junta textos.
- Operação de Inteiros: `+` soma valores numéricos.
- ⚠️ Erro de Tipagem: Tentar somar `String + Int` gera erro. Solução: Casting ou f-string.

```python
#==== Concatenação em Integer
terry_crews = 10000
latrell_spencer = 40000
ofertafinal = terry_crews + latrell_spencer #retorna 50000
```

#### 5. [Var Local e Global]

- **Global**: Fora da função, acessível em qualquer lugar.
- **Local**: Dentro da função, inacessível fora dela.
- **Global Keyword**: Usado para criar ou modificar uma variável global dentro do escopo local.

```python
# Escopo Joanesburgo [Escopo Global]
wikus = "Humano" # Var Global

#--------------------------------------------------------
def entrar_distrito_9(): # Onde é contaminado [Escopo Local]
    global new_wikus

    wikus = "Contaminado"   # Var Local
    #(A mutação não altera ainda como o mundo o vê)

    if wikus == "Contaminado":
        # Fazer a transformação de contaminado para prawn
        new_wikus = "Prawn"
        # Forçada a global (Para ser acessível fora do D9)

    print("No Distrito 9 o Wikus é: " + wikus) # Usa a local
#---------------------------------------------------------

entrar_distrito_9()

# Escopo Joanesburgo
print("Para Joanesburgo ele ainda consta como: " + wikus)      # Usa a global: "Humano"
print("Mas a forma que sobrou para o mundo foi: " + new_wikus) # Acessa a global forçada

```

#### 6. Perguntas do Teste

1. Variável criada no momento da atribuição? **True**
2. Nomes compostos podem conter espaços? **False**
3. Python é Case Sensitive? **True**

#### 7. Exercício

```python
  #Criar um diretorio, e o script armazenamento.py

  """tarefas:
  - Declarar uma variável [✅]
    - Sobreponha o valor de uma var [✅]
  - Atribuir valores à variaveis [✅]
  - Atribuir valor com incremento [✅]
  - Atribua a soma de vars como valor de outra [✅]
  """
  # 1. Declaração e Atribuição inicial
  D = 2
  print("O valor inicial de D é:", D)

  # 1.2 Sobrepondo o valor de D
  D = 0
  print("O valor sobreposto de D é:", D)


  # 2. Atribuindo valores a outras variáveis
  A = 2
  B = 3
  C = 5
  print("A:", A, "| B:", B, "| C:", C)

  # 3. Sobrepondo o valor (Lógica de incremento: C recebe ele mesmo + 1)
  C = C + 1
  print("O valor atualizado de C (C + 1) é:", C)

  # 4. Atribuindo a soma de variáveis a outra
  D = A + C
  print("O valor final de D (A + C) é:", D)
```

#### 8. Revisões

💻 Exercícios Práticos (Desafios de Código)
Para maximizar a sua absorção, crie um arquivo chamado exercicios_fixacao.py e tente implementar as lógicas abaixo usando tudo o que você aprendeu nas suas notas.

Exercício 1: O Caos do Desempacotamento e Casting

Contexto: Você recebeu um registro num sistema antigo na forma de uma lista bruta: dados = ["100", "20.5", "Kauan"].

Tarefa: Utilize a técnica de desempacotamento para salvar esses 3 valores em três variáveis separadas em uma única linha.

Desafio: Após desempacotar, as duas primeiras variáveis ainda serão textos (strings). Faça o casting da primeira para int, da segunda para float, some as duas em uma nova variável chamada resultado_soma, e faça um print() do resultado final e de seu tipo usando type().

Exercício 2: Hackeando a Visibilidade (Local vs Global)

Contexto: Vamos entender na prática como o Python bloqueia informações de funções internas.

Tarefa: No escopo principal do script (lado de fora), crie uma variável sistema_ativo = False.

Desafio: Crie uma função (ex: def forcar_ativacao():). Dentro dela, sem redeclarar nada como global, tente fazer sistema_ativo = True. Imprima a variável dentro da função e logo após executar a função, fora dela.

Resolvendo: Perceba que a original externa não mudou. Agora, reescreva a função usando a instrução global que você anotou do material, e verifique que o script principal obedeceu à alteração interna!

Exercício 3: Atribuição Coletiva e a Armadilha da Concatenação

Contexto: Atribuição múltipla é útil, mas exige cuidado na manipulação mista com tipos numéricos.

Tarefa: Em apenas uma linha, crie 3 variáveis (ex: a, b, c) que recebam simultaneamente a string "Python". (Atribuição coletiva).

Desafio: Mude isoladamente o valor da terceira variável (c) para o número inteiro 3. Em seguida, crie uma variável versao_final concatenando a variável a com a variável c recém-alterada, mas fazendo o tratamento (casting) correto para que o terminal exiba a string "Python 3" em vez de disparar um erro TypeError.

```python
# 1 =================================================================

num_cem, num_vinte, nome = dados
# int(num_cem)
# float(num_vinte) #a var não salva automaticamente o casting

  #correto
num_cem = int(num_cem)
num_vinte = float(num_vinte)

resultado_soma = num_cem + num_vinte
print(f" o reultado é {resultado_soma} do tipo {type(resultado_soma)}")

# 2 =================================================================

sistema_ativo = False

def forcar_ativ():
     sistema_ativo = True
     print(f"a var sistema ativo internamente é: {sistema_ativo}") #deve retornar True

#não esquecer de chamar a função
forcar_ativ()
print(f"a var sistema ativo externamente é: {sistema_ativo}") #deve retornar False

novo_sistema_ativo = False
def forcar_ativ_glob():
     global novo_sistema_ativo
     novo_sistema_ativo = True
     print(f"a var sistema ativo internamente é: {novo_sistema_ativo}") #deve retornar True
forcar_ativ_glob()
print(f"a var sistema ativo externamente é: {novo_sistema_ativo}") #deve retornar True

# 3 =================================================================

a = b = c = "Python"
c = 3
versao_final = a + str(c)
print(versao_final)
```

===================================================================

Resultado revisão:
Pontos fortes
Atribuição e Desempacotamento de Variáveis: Você demonstrou um excelente entendimento sobre atribuições múltiplas, lógicas de incremento e o comportamento do interpretador ao desempacotar listas, identificando com precisão a ocorrência de 'ValueError' devido à incompatibilidade de valores.
Tipagem Dinâmica e Casting: O conceito de tipagem dinâmica e as operações de conversão explícita (casting) de tipos primitivos estão muito consolidados. Você acertou em cheio a resolução técnica das conversões aninhadas entre strings, floats e inteiros.
Manipulação de Escopo (Escrita): Você aplicou corretamente o conceito de escopo no Python, compreendendo de forma exata como a palavra-chave 'global' permite que o escopo local de uma função sobreponha diretamente uma variável externa.
Regras de Nomenclatura e Tipagem Dinâmica: Você tem um excelente entendimento das regras básicas para criar variáveis no Python, incluindo o uso do padrão Snakecase e as restrições de formatação. Além disso, dominou os conceitos de tipagem dinâmica, conversão de tipos (casting) e o uso da função type().
Operações com Coleções e Tratamento de Erros: Você demonstrou grande clareza sobre como descompactar elementos de listas em múltiplas variáveis simultaneamente e conseguiu identificar corretamente as exceções geradas pelo interpretador (como ValueError e erros de tipagem) em operações inválidas.

Áreas a melhorar
Interação Direta Entre Tipos Distintos: Houve uma confusão quanto à concatenação de strings com inteiros. Por ser fortemente tipado, o Python não realiza a junção de forma silenciosa; ele interrompe o código com um 'TypeError'. A solução técnica correta é sempre utilizar o casting, convertendo o inteiro para string com 'str()'.
Escopo Global (Leitura vs. Alteração): É necessário revisar a visualização de escopos. O Python permite que uma função leia e imprima uma variável global de forma nativa e sem erros. A declaração explícita da palavra-chave 'global' no interior da função só se faz obrigatória quando o objetivo é reatribuir ou modificar o valor dessa variável.
Convenções de Nomenclatura (PEP 8): Revise o uso dos padrões (Cases) do Python. O uso de iniciais maiúsculas em todas as palavras (PascalCase, ex: StatusDeLogin) é uma convenção estrita para declarar Classes. Para variáveis que guardam estados simples, o recomendado pelo PEP 8 é continuar utilizando o padrão 'snake_case'.

::last-review:: 10-04-2026 ::Revisão de conceitos básicos::
Aproveitamento 80%
::last-review:: 17-04-2026 ::Refazer prova de operadores simples::
Aproveitamento 100%
.::last-review:: 23-04-2026 ::Criar questionário avançado e exercícios::
aproveitamento 70%
aproveitamento teste 90% - revisão distante
::to-review:: 23-05-2026 ::Conceitos Básicos::
