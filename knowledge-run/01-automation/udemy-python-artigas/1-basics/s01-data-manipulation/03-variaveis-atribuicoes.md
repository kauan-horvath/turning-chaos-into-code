# 📂 Seção 01: [Manipulação de Dados]
## 📑 [Variaveis e Atribuições]
> **Status:** 🟢 Concluída | **Data:** 08/04/2026

| **🏠 HOME** | [Retornar ao Início](../../0-organization/python-artigas-home.md) |
| :--- | :--- |
| &#8657; **Anterior** | [Introdução](../s00-into-config/02-sintaxe-primeiros-passos.md) |
| &#8659; **Próximo** | [Primeiros passos](./04-tipos-dados.md) |

### 📺 Conteúdo em Vídeo (Udemy)
- [✅] **[Vídeo 07](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408398#notes):** [Apresentando variáveis] — *(16min)*
- [✅] **[Vídeo 08](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408402#notes):** [Nomes das Variáveis] — *(10min)*
- [✅] **[Vídeo 09](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408498#notes):** [Atribuir Valores] — *(10min)*
- [✅] **[Vídeo 10](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408518#notes):** [Valores de Saída] — *(11min)*
- [✅] **[Vídeo 11](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408528#notes):** [Escopo Global e Local] — *(20min)*
- [✅] **[Teste](https://www.udemy.com/course/python-completo-e-profissional/learn/quiz/5346070#notes):** [Quick Followup] — *(0 min)*
- [✅] **[Exercício](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29393200#notes):** [Exercício de Armazenamento] — *(10 min)*

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

``` python 
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

#### 6. Perguntas do Teste:
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
#### 8. Revisões:
  ```python
      #Previous revisions
      #[LAST-DATE: 2026-04-10] Review very basic functions
      '''
      https://gemini.google.com/share/94fe8611337a
      Pedi uma prova com ia aproveitamento de: 80% (revisão em 1 semana)
      teste se posso apagar o questionario # permitido!'''
````

Resultado revisão:

- Regras de Nomenclatura e Tipagem Dinâmica: Você tem um excelente entendimento das regras básicas para criar variáveis no Python, incluindo o uso do padrão Snakecase e as restrições de formatação. Além disso, dominou os conceitos de tipagem dinâmica, conversão de tipos (casting) e o uso da função type().
- Operações com Coleções e Tratamento de Erros: Você demonstrou grande clareza sobre como descompactar elementos de listas em múltiplas variáveis simultaneamente e conseguiu identificar corretamente as exceções geradas pelo interpretador (como ValueError e erros de tipagem) em operações inválidas.

::to-review:: 17-04-2026 ::Refazer prova de operadores simples::
