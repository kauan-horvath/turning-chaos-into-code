# 📂 Seção 01: [Manipulação de Dados]

## 📑 [Tipos primitivos 1]

> **Status:** 🟢 Concluido | **Data:** 09/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../../0-organization/python-artigas-home.md)      |
| :------------------- | :--------------------------------------------------------------------- |
| &#8657; **Anterior** | [Primeiros Passos](../s00-intro-config\02-sintaxe-primeiros-passos.md) |
| &#8659; **Próximo**  | [Operadores](./05-operadores-logicos.md)                               |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 13](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408604#content):** [Todos os tipos primitivos] — _(10min)_
- [✅] **[Vídeo 14](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408616#content):** [Inteiros] — _(17min)_
- [✅] **[Vídeo 15](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408622#content):** [Casting] — _(10min)_
- [✅] **[Vídeo 16](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408636#content):** [Strings] — _(11min)_
- [✅] **[Vídeo 17](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408654#content):** [Fatiar Strings] — _(11min)_
- [✅] **[Vídeo 18](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408852#content):** [Modificar Strings] — _(14min)_
- [✅] **[Vídeo 19](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408892#content):** [Concatenação de Strings] — _(5min)_
- [✅] **[Vídeo 20](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408908#content):** [Formatação de Strings] — _(11min)_
- [✅] **[Vídeo 21](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408938#content):** [Caracteres de Escape] — _(21min)_
- [✅] **[Vídeo 22](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28408956#content):** [Valores Booleanos] — _(17min)_
- [✅] **[Teste](https://www.udemy.com/course/python-completo-e-profissional/learn/quiz/5346072#content):** [Teste] — _(0min)_
- [✅] **[Exercicio1](https://www.udemy.com/course/python-completo-e-profissional/learn/quiz/5346072#content):** [Exercicio1] — _(10min)_
- [✅] **[Exercicio2](https://www.udemy.com/course/python-completo-e-profissional/learn/quiz/5346072#content):** [Exercicio2] — _(10min)_

> **Nota rápida:** [Uma aula extensa sobre as delicadezas dos tipos primitivos de Str e Int, ver restante na seção tipo primitivos 2]

---

### 📝 Anotações e Conceitos Chave

#### 1. [Overview dos tipos]

- O professor passa brevemente por cada tipo:
  **[str] String:** Texto e caracteres
  **[int] [float] [complex] Numéricos:** Números e matemática
  **[bool] Booleanos:** Valores de True or False
  **[list] [tuple] [range] Sequência:** listas e armazenamento
  **[dict] Mapeamento:** orgnização e chaves
  **[set] [frozenset] Conjuntos:** não faço ideia
  **[bytes] [bytearray] [memoryview] Binários:** não faço ideia

- Exemplo de sintaxe ou regra:

```python
  #Output de cada tipo
  string_var = "um texto" #incluindo o espaço
 
  int_var = 20 #apenas inteiros
  float_var = 20.5 #apenas numeros reais
  complex_var = 1j #apenas a letra j
 
  bool_var = True #or False

  list_var = ["str_data1","str_data2"]
  tuple_var = ("str_data1","str_data2")
  range_var = range(num) #using the function

  dict_var = {"str_key1":"str_value1", "str_key2":10}
  set_var = {"str_data1", "str_data2"} # maybe a dict without key?
  fronzenset_var = ({"str_data1", "str_data1"}) # a tuple with a set inside?

  bytes_var = b"str_data" #have no ideia why
  bytearray_var = bytearray(num) #using a function
  memoview_var = memoryview(bytes(num)) #wtf

  #Explica denovo sobre casting (Definir vs Configurar)
  casting_list = [
    str(), int(), float(), complex(), bool(), list(), tuple(), range(), dict(), set(), frozenset(), bytes(), bytearray(), memoryview(bytes())]
    #note nem todos os valores são intercambiáveis, transformar um [int em bool] = [5 != True]
```

#### 2. [Números]

- informa sobre a existência de **numeros negativos**.
- informa sobre a **sintaxe de "."** para float.
- informa sobre a **notação científica** [35e3].
- informa sobre a **letra j** do complex [5j].
- informa a conversão **[Casting]** entre tipos numéricos:
    - pesquisar onde exatamente é util um int(2.8) Ex-tipo como novo tipo? exceto str <> int não conheco nenhum outro uso
    - **funções de construtor:** int(), float() etc
    - menciona um pouco sobre os **erros de casting**, pois input incorretos geram ValueError
- informa sobre a geração de **random numbers**.
- Exemplo de sintaxe ou regra:

```python
  #usando random
  import random
  min = 0
  max = 7

  #randrange é Offbyone, só atinge max-1
  media_boletim = random.randrange(min, max) #reprovado safado
 
  float(media_boletim) #6.0
  #str("seis") erro ausencia de num literal
```

#### 3. [Strings]

- informa sobre o **uso de aspas:**
    - **'** simples
    - **"** duplas
    - **'''** multiline
- informa que strings são **MATRIZES** de caracteres:
    - acessar esses caracteres atraves do **index[num]**.
- informa que strings são **ARRAYS**, ou seja, podem ser percorridas por um loop for:
    - em cada value usando um **index[]** da string.
- informa sobre a medição de string com **len()**.
- **UTIL:** cheCa se uma frase esta presente dentro do string com o **metodo in**.

- Exemplo de sintaxe ou regra:

```python

  #acessando a matriz da string
  abcdario = "ABCDE"
 
  tamanho_abc = len(abcdario) #comprimento

  letra_1 = abcdario[0] #index offbyone #A
  letra_1a3 = abcdario[0:3] #aula de index
  letra_final = abcdario[-1] #acho que é isso

 
  #sintaxe literal: for letra in "LMFAO"
  for letra in abcdario:
    #soletra as letras
    print(letra)
    #1 loop A
    #2 loop B ...

  #====================================
  kauan = "Eu programo em Python a " #2 anos

  is_programer = "PROGRAM" in kauan.upper() #retorna True
  is_java = "JAVA" in kauan.upper() #retorna False
  is_not_dated = "ANO" not in kauan.upper() #retorna True if its not dates

  if is_programer == True:
      print("Você programa! passou para a proxima fase!")
      if is_not_dated == True:
          print("please provide us the time")
      else:
          print("Você programa há algum tempo! passou para a proxima fase!")

          if is_java == True:
              print("Procuramos um programador de JAVA, você foi Arovado")
          else:
              print("Infelizmente você não programa em java - Reprovado")
  else:
      print("você não é programador reprovado")
```

##### 3.1 [Fatiar Strings]

- informa sobre o uso de **index** para fatiar strings.
- Exemplo de sintaxe ou regra:

```python
  #acessando pedaços de strings
  abcdario = "ABCDEFGHIJK"
  texto_2a6 = texto[2:6] # retorna "CDEFG"
  texto_inicio_ate6 = texto[:6] #retorna "ABCDEFG"
  texto_de6_final = texto[6:] #retorna "GHIJK"
  indexnegativo_invertido = texto[-5:-3] #retorna "GH"
```

##### 3.2 [Modificar Strings]

- **Concatenação (+):** informa que não podemos concatenar string + num.
- **Imutabilidade:** informa que os metodos criam cópia e não modificam o original.

**Principais Metodos:**

- **.upper():** reorna tudo maiusculo.
- **.lower():** retorn minusculo.
- **.strip():** remove espaços do começo e final.
- **.replace():** "subsituir", "substituto".
- **.split():** o texto entre o separador fornecido se torna uma lista.

- Exemplo de sintaxe ou regra:

```python
  #acessando pedaços de strings
  sussuro = "me vê um tadalafila.."
  tamanho_da_sala = "         [eu]          "

  atendente_pro_estoque = sussuro.upper() #retorna um berro ME VE UM TADALAFILA!
  depois_do_vexame = tamanho_da_sala.strip() #retorna "[eu]" com vergonha kk
  panico_mode = sussuro.replace("..", " pro meu pai rsrsrs") #retorna me ve um tadalafila pro meu pai rsrsrs

  cerebro_atendente = "Um tadalafila!, pro pai dele"
  lista_cliente = cerebro_atendente.split(",")
  lista_cliente_atualizada = lista_cliente[0] #excluiu a informação adicionada kk

  atendente_pro_estoque = sussuro.upper() #retorna um berro UM TADALAFILA!
```

##### 3.3 [Formato de Strings]

- informa sobre o **método format():** semelhante ao fstring mas é metodo .format().
- informa sobre o **index** das entradas de dados no format:
  - **CUIDADO COM OFFBYONE:** {0},{1}

  - Exemplo de Sintaxe ou regra:

```python
      #exemplo de uso do ponto format
      qtd_beijos = 2
      beijos_morena = "Tudo que eu preciso são {} beijos da morena"

      tiros_marido = qtd_beijos * 10
      facadas_marido = qtd_beijos * 1
      marido_rampage = "Salafrário, vou te dar {1} facadas e {0} tiros, pra você aprender a não pegar mulher casada"

      #isso para adicionar int a str sem concatenar
      print(beijos_morena.format(qtd_beijos)) #retorna ..10 beijos da morena
      print(marido_rampage.format(facadas_marido, tiros_marido)) #retorna .. vou te dar 20 facadas e 2 tiros kk
```

##### 3.4 [Caracteres Especiais]

- informa que usar alguns simbolos dao erro na string:
    - **\\"**: retorna as aspas literais.
    - **\\\\**: retorna uma barra invertida literal.
    - **\\'**: retorna uma aspas simples literal.
    - **\\n**: retorna uma quebra de linha.
    - **\\r**: retorna uma carriage return, nova linha de baixo.
    - **\\t**: retorna tabulação com tab.
    - **\\b**: retorna um bascskpace e apaga o anterior.
    - **\\x**: retorna um caractere literal a partir de um código hexadecimal \x48 = H.
    - **\\123**: retorna um caractere literal a partir de um código Otal \x110 = H.

- Exemplo de Sintaxe ou regra:

```python
    #uso do caractere especial

    é_bilada_cino = "eu disse que era \"SABOR\" Mulher"
    print("Toguro diz: " + é_bilada_cino) #retorna "Toguro diz: eu disse que era SABOR Mulher"
```

#### 4. [Booleanos]

- informa que são valores de resultados de **expressões lógicas** e servem para inúmeras funcções e cenários.
- informa como funciona o **casting de bool():**
    - só retorna **False** se:
      - string, list, etc = "" Vazios
      - int, floar, etc = 0
- informa sobre o **retorno bool** de funções.
- informa sobre a funct **isinstance()**.

- Exemplo de sintaxe ou regra:

```python
  #obtendo valor bool
  meu_carro = 10
  seu_carro = 9

  feministas = 1
 
  falocentrismo = meu_carro > seu_carro #retorna True
  isinstance(falocentrismo, bool) #retorna true se for do tipo fornecido

  def prolifer():
      if falocentrismo == True:
        feminista += 1000
        return True
      else:
        print("o mundo reside em paz por mais tempo")
        return False

  if prolifer() == True:
    print("explodir o mundo")
```

#### 5. Teste e Exercícios

1. Em Python, o tipo de dados é definido quando você atribui um valor a uma variável. = **True**
2. Em Python int, float e complex são variáveis de tipo númerico. = **True**

- Exemplo de sintaxe ou regra:

```python
  #EXERCICIO 1 - Calcula Triplo
  braco = 1
  perna = 2

  def malhando(parte_corpo):
      print("fibrando esse corpinho")
      triplo = int(parte_corpo) * 3
      return triplo

  print(malhando(braco))
  print(malhando(perna))

  #EXERCICIO 2 - Calcula Produto de 2 numeros O.O
  tamanho_sua_mãe = input("Digite um numero entre 100 e 1000: ")
  tamanho_da_lua = input("Digite um umero entre 1 e 10: ")
  #input retorna string é necessário casting

  massa_buraco_negro = int(tamanho_sua_mãe) * int(tamanho_da_lua)
  print(f"A multiplicação é: {massa_buraco_negro}")
```

[LAST-DATE: 2026-04-11] Revisão de tipos

[Questionário](https://gemini.google.com/share/089bc530f8bd)

> > > > Aproveitamento de 81% - revisão média

```python
    '''
      - Pontos fortes
        - Manipulação e Métodos de Strings: Você demonstrou domínio excelente sobre métodos como `.strip()`, `.upper()`, `.replace()` e fatiamento negativo, além de compreender a imutabilidade das strings e o uso de caracteres de escape.
        - Tipagem e Conversão Numérica: Excelente compreensão sobre tipos numéricos complexos, erros de tipo em concatenações sem casting e o comportamento da função `int()` ao truncar números decimais.
        - Operadores Lógicos e Formatação: Identificou corretamente o uso de operadores de associação (`not in`) e a indexação de argumentos no método `.format()`.
      - Áreas a melhorar
        - Lógica de Booleanos em Coleções: Lembre-se que em Python, coleções (listas, tuplas, etc.) são consideradas `True` se não estiverem vazias. No caso de `bool([0])`, o resultado é `True` porque a lista contém um elemento, mesmo que o elemento seja zero.
        - Sintaxe de Fatiamento (Slicing): Ao omitir o valor antes dos dois pontos em `[:6]`, o Python sempre inicia o fatiamento a partir do índice 0, e não do índice 1.
        - Estruturas de Dados (Sets vs Dicts): Ambos utilizam chaves `{}` na sintaxe, mas a diferença fundamental é estrutural: dicionários exigem pares `chave: valor`, enquanto sets contêm apenas valores únicos.
      '''
```

::to-review:: 18-04-2026 ::Tipos Primitivos::
