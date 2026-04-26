# 📂 **Seção 05:** Operadores Aritméticos e Lógicos

## 📑 [Operadores]

> **Status:** 🟡 CONCLUIDO | **Data:** 10/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../../0-organization/python-artigas-home.md) |
| :------------------- | :---------------------------------------------------------------- |
| &#8657; **Anterior** | [Tipos primitivos 1](./04-tipos-dados.md)                         |
| &#8659; **Próximo**  | [PROXIMO](../s02-data-colection/colecoes-listas.md)               |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 25](<(https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28409058#content)>):** [Operadodes Aritméticos] — _(12min)_
- [✅] **[Vídeo 26](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28409072#content):** [Operadores de Atribuição] — _(10min)_
- [✅] **[Vídeo 27](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28409096#content):** [Operadores de Comparação] — _(6min)_
- [✅] **[Vídeo 28](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28409124#content):** [Operadores Lógicos] — _(10min)_
- [✅] **[Vídeo 29](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28409144#content):** [Operadores de Identidade] — _(10min)_
- [✅] **[Vídeo 30](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28409178#content):** [Operadores de Associação] — _(5min)_
- [✅] **[Vídeo 83](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794116#content):** [Entrada de Dados do Usuário] — _(5min)_
- [✅] **[Teste](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/quiz/5346078#content)>):** [Teste] — _(Duração)_

> **Nota rápida:** [Um conjunto de definições e funções para os operadores, o básico nunca deve ser negligênciado]

---

### 📝 Anotações e Conceitos Chave

#### 1. [Matemática em Python]

- Explica novamente sobre o tipo Int
- Detalha a diferença de valores literais e operações matemáticas
- Informa sobre a persistencia PEMDAS

- Exemplo de sintaxe ou regra:

  ```python
  # Explica sobre os operadores matemáticos
  somar = num + num
  subtrair = num - num
  dividir = num / div #tipo float
  multiplicar = num * num

  resto_dividir = num % num
    #util para identificar numero par/impar
    def is_even(num):
        check = num % 2 = 0 #se sobrar zero ao dividir por 2 é par
        return check

  expoente = base ** expoente #base

  #arredonda pra baixo
  floor_division = 15 // 2 # retorna 7
        #regular_division =15 / 2 # retorna 7,5

  #Persistencia da regra PEMDAS
    conta = 9 * 8 + 256 * 20 - 10
    resposta_equipe_g1 = 5182
    resposta_lorenzo_10anos_queremos_injustica = 6550

    if conta == resposta_equipe_g1:
        print("Brasil não vai pra frente")
    if conta == resposta_lorenzo_10anos_queremos_injustica:
        print("Brasil que eu quero")
  ```

#### 2. [Atribuição e Atribuição combinada]

- Explica sobre os tipos de "="
- Explica sobre os incrementos
- Explica sobre o incremente em operadores de atribuição combinada
- Retorno Booleano da comparação

- Exemplo de sintaxe ou regra:

  ```python
  # Explica sobre os operadores de atribuição combinada
    #num == 10 #comparação
    num = 10 #atribuição
    num += 10 # combinada num = num + 10

    num += 1
    num -= 1
    num *= 1
    num /= 1

    #atribuição combinada
    num %= 1 #num = num % 1 (recebe o resto como incremento)
    num //= 1 #num = num // 1 (recebe o resto)
    num **= 1 #num = num ** 1 (recebe o resultado)

    # Explica sobre os operadores de comparação

    comparar = (num == 10) #comparação
    diferente = (num != 10) #se diff True

    maior_qu = (num > 10)
    menor_que = (num <10)
    maior_igual_que = (num >= 10)
    menor_igual_que = (num <= 10)
  ```

#### 3. [Operadores Condicionais]

- Verifica uma estrutura lógica e seu resultado boleano
- informa que "and" precisa que ambas sejam True
- informa que "or" preciso que ao menos uma seja True
- informa que "not" é uma função de inversão

- Exemplo de sintaxe ou regra:

  ```python
    num = 5
    retorno_and = num > 3 and num < 10 #retorna True
    retorno_or = num > 3 or num < 4 # retorna True mesmo com uma expressão False

    pergunta = "Você tá bem?"
    resposta_morena = "SiM, EsToU óTiMa"
    def check_reposta():
        if "any" in resposta_morena: #retorna True pra tudo
            verdade = not(resposta_morena)
            return verdade
  ```

#### 4. [Operadores Identidade e Associação]

- Demonstra que o mesmo valor em outro local, não é o mesmo objeto
- Demonstra que is e is not verificam a exatidão local
- Demonstra que in checa se está

- Exemplo de sintaxe ou regra:

  ```python
    meu_carregador = ["Branco USB-C"]
    carregador_esposa = ["Branco USB-C"]

    na_borsa_da_marvada = meu_carregador

    mesmo_modelo = (meu_carregador == carregadores_esposa) #True porque tem o mesmo valor
    modelos_diferentes = (meu_carregador != carregadores_esposa) #False porque tem o mesmo valor


    carregadorIgual_com_arranhados_e_tudo = na_borsa_da_marvada is meu_carregador
    #True porque é o mesmo local atribuido

    carregadorPerebento_carcomido = na_borsa_da_marvada is not carregador_esposa
    #True por que o dela não é o perebento

    #Operadores de Associação
    cabo_meu_carregador = ["lindo, branquinho, cuidado"]
    cabo_carregador_esposa = ["que cabo?, carcomido, pisado"]

    na_borsa_da_marvada = cabo_meu_carregador
    Investigando = ("carcomido" in na_borsa_da_marvada) #retorna False porque é o mesmo objeto
    Confirmando = ("cuidado" not in na_borsa_da_marvada) #retorna True porque consta la dentro e não era pra constar O.O)
  ```

#### 5. Input e Entrada de Dados

- Informa sobre o método de Input().
- EXPLICAÇÃO.
- Exemplo de sintaxe ou regra:

```python
  #Exemplo de Input
  nome = input("Qual seu nome?")
  print("Seu nome é " + var)

```

#### 5. [Teste]

1. Operadores aritméticos são usados para realizar operações matemáticas | True
2. O operador '=' é um operador de comparação de igualdade | False

💻 Notas / Revisão

🟢 Pontos Fortes (O que já está no "sangue")Esses são os conceitos que você dominou a lógica por trás, não apenas decorou a sintaxe. Na próxima revisão, você pode apenas passar o olho rapidamente:Identidade vs. Igualdade de Valor: Você dominou a diferença entre == (mesmo valor) e is (mesmo objeto na memória). A analogia dos carregadores e da "Borsa da Marvada" fixou muito bem.Comportamento de Lógica Booleana: Excelente compreensão de como o or salva uma condição se apenas um lado for verdadeiro, e como o not inverte o estado lógico (a ironia da "resposta_morena").Ordem de Precedência (PEMDAS): A regra matemática foi bem absorvida. Você entende que o código lê a matemática como uma equação real, o que evita bugs de cálculo estrutural.Operadores Matemáticos Básicos: O uso de % para resto (par/ímpar) e // para divisão inteira está claro e correto.🔴 Pontos de Atenção (Onde focar na próxima revisão)Esses são os detalhes sintáticos, nomenclaturas e pequenas "pegadinhas" matemáticas que precisam de reforço ativo:A Pegadinha da Atribuição com Exponente (**=): \* O erro: Achar que num**= 1 soma a base ao resultado.A correção: num \*\*= 1 é estritamente $num = num^1$. Se num é 10, o resultado permanece 10.Nomenclatura das Categorias de Operadores:O erro: Confundir os nomes dos grupos ao ser questionado.A correção: Lembrar que is/is not = Identidade (Quem você é / seu RG na memória). E que in/not in = Associação (Se você faz parte de um clube/lista).Nomenclatura de Erros Nativos do Python:O erro: Saber que o código quebra, mas não saber o nome do erro ao chamar uma variável inexistente.A correção: Variável que não existe gera um NameError.Sintaxe de Atribuição Combinada:O erro: Descrever o que o operador faz em vez de escrever a sintaxe quando o exercício pedir código.A correção: O resto da divisão atribuído à própria variável se escreve num %= 1.Sintaxe do Operador de Negação em Associações:O erro: Usar "operar in" quando se quer a negação.A correção: A sintaxe exata para verificar se algo não está na lista é not in.

last-review:: 12-04-2026 ::Operadores Lógicos
aproveitamento de 93% revisão distante

::last-review:: 26-04-2026 ::Operadores lógicos::
aproveitamento 100% - revisão distante

::to-review:: 26-05-2026 ::Operadores Lógicos+::
