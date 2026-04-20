# 📂 Seção 18 : Matrizes e Coleções Multidimensionais

## 📑 Matrizes

> **Status:** 🟡 CONCLUIDO | **Data:** 17/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../../0-organization/python-artigas-home.md) |
| :------------------- | :---------------------------------------------------------------- |
| &#8657; **Anterior** | [ANTERIOR](./colecoes-dicts.md)                                   |
| &#8659; **Próximo**  | [PROXIMO](../s03-modularization/condicionais-if-else.md)          |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [x] **[Vídeo 84](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884124#overview):** Arrays — _(10min)_
- [x] **[Vídeo 85](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884134#overview):** Listas como Arrays — _(5min)_

> **Nota rápida:** [Devido à fraqueza do material fiz uma pesquisa mais densa com IA]

---

### 📝 Anotações e Conceitos Chave

#### 1. A incrivel semelhança de arrays com listas

- informa que não há suporte para Arrays e que num improviso pode-se usar lists ⚠️ Em outras linguagens uma array não pode aumentar de tamanho

- Para usar como Array propriamente dito é necessário uma biblioteca
  - import array as arr
  - ⚠️porque usar o import? EFICIENCIA DE MEMORIA.
    - uma lista aceita todos os tipos de dados, a array exige que todos sejam do mesmo tipo, tornando mais leve e facilitando lidar com muitos dados.
- Tipagem de dados (Type codes)
  - informa sobre os 4 tipos i, f, d, u
    - i - inteiro assinado (pos negativo)
    - f - float
    - d - float duplo (como decimal)
    - u - unicode (entrando em desuso)

- Exemplo de sintaxe ou regra:

```python
    #Exemplos

    import array as arr

    #criando um array de inteiros
    megasena = arr.array("i", [14, 20, 32, 37, 39, 42])

        #acesso por index
        megasena[0] #return 14

        #alterando como lista
        megasena[1] = 25 #altera 20 por 25
        #megasena[1] = "vinte e cinco" #return error

    #metodos de lista funcionam normalmente (se respeitando o tipo da array)
    #loops for e while funcionam normalmente (se nao alterar o tipo)

    #metodos exclusivos para array

    #salvar todo o array em um binário (ultra rápido)
        #usa-se o with para não precisar de f.open() e f.close()
            #e ficar preso em caso de erro
    with open("arquivo.bin", "wb") as f: #f é convenção para a var do file
        #wb (write binary)
        megasena.tofile(f)

    #desconverter de binário para array devolta
    minha_megasena = arr.array("i")
    with open("megasena.bin", "rb") as f:
        minha_megasena.fromfile(f, 3)
        #rb (read binary)
        #3 é a qtd de arquivos que serao puxados do binario
            #se pedir a mais vai retornar EOFError (End of file)

    #como solicitar all inves de por numero, só deixar sem número?
    import os

        # 1. Descobrir o tamanho total do arquivo em bytes
        tamanho_bytes = os.path.getsize("megasena.bin")

        # 2. Descobrir quantos bytes cada item do seu tipo ocupa (itemsize)
        # Para o tipo 'i', geralmente é 4.
        tamanho_do_item = minha_megasena.itemsize

        # 3. Calcular a quantidade total
        quantidade = tamanho_bytes // tamanho_do_item

        # 4. Ler tudo de uma vez
        with open("megasena.bin", "rb") as f:
            minha_megasena.fromfile(f, quantidade)
```

#### 2. Refinado pela IA

Guia de Arrays em Python (Módulo `array`)

### 1. Arrays vs. Listas

- **Nativo vs. Biblioteca:** O Python não possui suporte a arrays "puros" de forma global; por padrão, usamos **lists**. Para arrays reais, é necessário importar a biblioteca `array`.

- **Eficiência de Memória:** Diferente das listas (que guardam objetos e ocupam muito espaço), o array guarda valores brutos.
  - **Lista:** Aceita dados mistos (string, int, float).
  - **Array:** Exige **tipo único**. É mais leve e ideal para lidar com grandes volumes de dados numéricos.
- **Limitação de Tamanho:** ⚠️ Em linguagens de baixo nível (C/Java), arrays têm tamanho fixo. No Python, o módulo `array` permite `.append()`, mas internamente ele precisa realocar memória, o que pode ser lento em escalas massivas.

---

### 2. Tipagem de Dados (Type Codes)

Ao criar um array, você define o tipo de dado que ele aceitará usando um caractere:

| Código    | Descrição        | Nota Técnica                                     |
| :-------- | :--------------- | :----------------------------------------------- |
| **`'i'`** | Inteiro assinado | Aceita valores positivos e negativos.            |
| **`'f'`** | Float            | Ponto flutuante de precisão simples.             |
| **`'d'`** | Float duplo      | Ponto flutuante de alta precisão (como decimal). |
| **`'u'`** | Unicode          | Caractere (em desuso em versões recentes).       |

---

### 3. Implementação e Regras

```python
import array as arr

# Criando um array de inteiros ('i')
megasena = arr.array("i", [14, 20, 32, 37, 39, 42])

# ACESSO: Por índice (igual à lista)
# megasena[0] -> retorna 14

# ALTERAÇÃO: Deve respeitar o tipo definido
megasena[1] = 25              # OK: altera 20 por 25
# megasena[1] = "texto"       # ERRO: TypeError

# COMPATIBILIDADE:
# Métodos (append, pop, remove) e Loops (for, while) funcionam
# exatamente como nas listas, desde que o tipo seja respeitado.
```

---

### 4. Métodos Exclusivos e Manipulação de Arquivos

Arrays possuem métodos nativos para lidar com dados binários de forma ultra rápida.

#### Salvando em Binário (`tofile`)

Usamos o bloco `with` para garantir que o arquivo seja fechado corretamente, mesmo se houver erro.

```python
# 'wb' = Write Binary (Escrita Binária)
# 'f' = Convenção de variável para o arquivo (file)
with open("arquivo.bin", "wb") as f:
    megasena.tofile(f)
```

#### Lendo de Binário (`fromfile`)

Para ler, precisamos saber a quantidade de itens. Se pedir mais do que existe no arquivo, o Python retorna `EOFError`.

```python
minha_megasena = arr.array("i")

# 'rb' = Read Binary (Leitura Binária)
with open("arquivo.bin", "rb") as f:
    # Lê exatamente 3 itens do tipo 'i'
    minha_megasena.fromfile(f, 3)
```

#### Como ler o arquivo INTEIRO (Dinâmico)

Para não chutar um número e causar erro, calculamos o tamanho total:

```python
import os

# 1. Pega o tamanho total do arquivo em bytes
tamanho_bytes = os.path.getsize("arquivo.bin")

# 2. Verifica quantos bytes cada item do seu tipo ocupa (itemsize)
# No tipo 'i', geralmente ocupa 4 bytes por número
tamanho_do_item = minha_megasena.itemsize

# 3. Calcula a quantidade real de itens (Divisão inteira //)
quantidade = tamanho_bytes // tamanho_do_item

# 4. Lê tudo dinamicamente
with open("arquivo.bin", "rb") as f:
    minha_megasena.fromfile(f, quantidade)
```

> **Dica Extra:** Se não quiser calcular, você pode usar `minha_megasena.frombytes(f.read())`, que lê o arquivo todo e converte automaticamente.

### x. 🛠️ Revisões

::last-review:: 19-04-2026 ::Arrays e métodos exclusivos::

> > > > aprovetiamento 100% (sem testes)

::to-review:: 26-04-2026 :: Arrays ::
