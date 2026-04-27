# 📂 Seção 13 : Estruturas Condicionais (If, Else, Elif)

## 📑 Condicionais

> **Status:** 🟡 CONCLUIDA | **Data:** 18/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../../0-organization/python-artigas-home.md) |
| :------------------- | :---------------------------------------------------------------- |
| &#8657; **Anterior** | [ANTERIOR](../s02-data-colection/matrizes-arrays.md)              |
| &#8659; **Próximo**  | [PROXIMO](./loops-repeticao.md)                                   |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 61](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28730208#overview):** Estruturas condicionais — _(14min)_
- [✅] **[Vídeo 62](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28730222#overview):** ShortHand If — _(10min)_
- [✅] **[Vídeo 63](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28730232#overview):** Operadores Lógicos — _(10min)_
- [✅] **[Vídeo 64](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28730236#overview):** Estruras Cond. Aninhadas — _(11min)_
- [✅] **[Vídeo 65](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28730244#overview):** Declaração de Passagem — _(5min)_

> **Nota rápida:** [Espaço para algum insight importante do conjunto de vídeos]

---

### 📝 Anotações e Conceitos Chave

#### 1. Condicionais

- informa que são verificações lógicas a partir de booleanos.
- Explica as relações de retorno entres os operadores bool.
- inform sobre elif (else if) só executa se a anterior for False

- Exemplo de sintaxe ou regra:

```python
    #Exemplos
    freeza = True


    if freeza == False:
        print("fiz nada não meu parcero")

    elif freeza:
        #if var: direto é o mesmo que "== True"
        print("porque você matou o kuririn")
        for repeat in range(2):
            print("eu estou nervoso!")

            #alterar a var depois do caminho tomado nao altera o rumo do condicional, ou seja ainda vai ignorar o else
            freeza = False
    else:
        print("goku calminho")

    #goku de verdade kk
    print("FREEEEEEEEZAAAAAAAAAAAA!")

```

#### 2. SHORTHAND IF | Aninhamento

- informa que é possível abreviar os condicionais.
- é uma forma muito pythonica de escrever ifs.
- informa sobre operador ternário ou shorthand if else
  - informa que op tern pode ser comprido
- Exemplo de sintaxe ou regra:

```python
    #exemplos
    freeza = False

    #tudo na mesma linha
    if freeza == False: print("ó o bixo vino mlk")

    #shorthand if else (operador ternário)
    print("eu sou o freeza") if freeza == True else print("Eu matei o kuririn porque eu quis")

   #varios elses em sequencia
    var = "cond_2"
    print(1) if var == "cond_1" else print(2) if var == "cond_2" else print(3)
        #return print(2)
    #⚠️ NOTA: usar elif dentro do aninhamento da syntaxError

    #o objetivo do aninhamento é retornar um valor bool objetivo da verificação
    o_freeza_matou_o_kururin = "Sim" if freeza else "Não"
        #removi os prints de print("sim") senão ele executa o print e retorna None
        print(o_freeza_matou_o_kururin) #agora return "sim"
```

| Tipo           | Sintaxe Tradicional                 | Shorthand (Pythonic)                |
| :------------- | :---------------------------------- | :---------------------------------- |
| **If Simples** | `if cond: print("Ok")`              | `if cond: print("Ok")`              |
| **If / Else**  | `if cond: a() else: b()`            | `a() if cond else b()`              |
| **Aninhado**   | `if c1: a() elif c2: b() else: c()` | `a() if c1 else b() if c2 else c()` |

```python
    #exemplos de aninhamento PYRAMID OF DOOM

    #Na pratica é assim que funciona mas não é elegante usar assim
    if a > b:
        print("==> a maior que b")
        if b > c:
            print("====> b maior que c")
            if c > d:
                print("======> c maior que d")
            else:
                print("======> c não maior que d")
        else:
            print("====> b não maior que c")
    else:
        print("==> a não maior que b")

    # Forma elegante e linear
    if a > b and b > c and c > d:
        print("Caminho direto: a > b > c > d")
    elif a > b and b > c:
        print("Parou no b > c")
    else:
        print("A condição inicial (a > b) falhou")
```

#### 3. Operadores Lógios | Declaração de Passagem

- informa que é possível combinar os operadores com `and` e `or`.
- informa a complexidade de vários operadores combinados.
- Exemplo de sintaxe ou regra:

```python
    #exemplos

    #and para 2 Trues
    if big_num > small_num and other_big > small_num:
        print("True porque big and other_big > small")

    #or para ao menos 1 True
    if lower_num > small_num or big_num > small_num:
        print("True porque pelo menos big > small")

    if lower_num > small_num or smaller_num > small_num:
        print("False porque None > small")

    #prioridade do and
    var_true = 10 > 9 or 10 > 11 and 1 < 10
        #o codigo lê tudo antes o AND 10 > 11 and 1 < 10 # return False pois 10 nãoé maior 1ue 11
             #e depois o OR 10 > 9 OR False #retornando True pois ao menos 10 é maior que 9

    #esse codigo não funciona porque tem um false antes do And
     #if 10 > 9 or 10 > 11 or 10 > 12  and 1 < 10 or 11 < 10 or 12 < 10:

        #se isolar com parenteses funciona
     if (10 > 9 or 10 > 11 or 10 > 12) and (1 < 10 or 11 < 10 or 12 < 10):
        print("True porque ao menos uma da esquerda E ao menos um da esquerda são True")

```

```python
    #exemplos de declaração de passagem

    if b > a:
        #não é possível um if vazio
            #entao usa-se pass para pular sem dar erro
        pass
```

### x. 🛠️ Revisões

Pontos fortes
Conceitos Fundamentais de Condicionais: Você demonstrou um excelente entendimento sobre o propósito das palavras-chave `elif`, `else`, `pass` e o conceito de 'truthiness' em Python.
Estrutura de Código e Boas Práticas: Identificou corretamente problemas de legibilidade como a 'Pyramid of Doom' e como evitá-la utilizando operadores lógicos.
Operador Ternário Básico: Sabe aplicar o operador ternário para atribuições simples e entende por que certas funções, como o `print()`, podem não ser ideais dentro dessa estrutura.
Áreas a melhorar
Precedência de Operadores Lógicos: Houve erros em expressões que combinam `and` e `or`. Lembre-se que, sem parênteses, o `and` tem precedência maior e é avaliado antes do `or`.
Fluxo de Execução if-elif-else: É importante reforçar que o Python interrompe a verificação de uma estrutura condicional assim que a primeira condição verdadeira é encontrada, ignorando todos os blocos subsequentes.
Sintaxe de Shorthand If: Você confundiu o 'Shorthand If' (`if condicao: acao`) com a estrutura do Operador Ternário. Praticar a escrita de comandos simples em uma única linha ajudará a distinguir as duas sintaxes.

::last-review:: 21-04-2026 :: Estruturas Condicionais ::

> > > > Aproveitamento 83% - revisão média

::last-review:: 27-04-2026 ::Estruturas Condicionais 2::

> > > > Aproveitamento 92% - revisão média

::to-review:: 27-05-2026 ::TITLE::
