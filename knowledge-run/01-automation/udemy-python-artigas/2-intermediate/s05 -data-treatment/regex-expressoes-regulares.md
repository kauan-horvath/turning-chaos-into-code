# 📂 Seção 26 : RegEx: Busca e Validação com Expressões Regulares

## 📑 REGE

> **Status:** 🟡 ANDAMENTO | **Data:** 09/05/2026

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 112](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29002524#overview)>):** RegEx — _(11min)_
- [✅] **[Vídeo 113](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29002512#overview)>):** Função Search() — _(9min)_
- [✅] **[Vídeo 114](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29002522#overview)>):** Findall() — _(7min)_
- [✅] **[Vídeo 115](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29002522#overview)>):** split() — _(min)_
- [✅] **[Vídeo 116](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29002530#overview)>):** sub() — _(4min)_
- [✅] **[Vídeo 117](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29002530#overview)>):** Objeto de Correspondencia — _(8min)_
- [✅] **[Vídeo 118](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29047336#overview)>):** Metacaracteres 1 — _(1min)_
- [✅] **[Vídeo 119](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29047338#overview)>):** Metacaracteres 2 — _(12min)_
- [✅] **[Vídeo 120](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29047342#overview)>):** Metacaracteres 3 — _(14min)_
- [✅] **[Vídeo 121](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29047366#overview)>):** Sequencias especiais 1 — _(11min)_
- [✅] **[Vídeo 122](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109224#overview)>):** Sequencias especiais 2 — _(5min)_
- [✅] **[Vídeo 123](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109236#overview)>):** Sequencias especiais 3 — _(3min)_
- [✅] **[Vídeo 124](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109250#overview)>):** Sequencias especiais 4— _(11min)_
- [✅] **[Vídeo 125](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109274#overview)>):** Conjuntos 1 — _(09min)_
- [✅] **[Vídeo 126](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109286#overview)>):** Conjuntos 2 — _(7min)_
- [✅] **[Vídeo 127](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109292#overview)>):** Conjuntos 3 — _(8min)_
- [✅] **[Vídeo 128](<[LINKDOVIDEO](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109294#overview)>):** Conjuntos 4 — _(11min)_

> **Nota rápida:** [mds senta que la vem historia, nao faço ideia do que seja mas bora pra cima]

---

### 📝 Anotações e Conceitos Chave

### Noção Geral

#### 1. O que é Regex (Expressões regulares)

- uma expressão regular que forma um padrão de pesquisa .
- usado para verificar se uma string possui o padrao de pesquisa.
- informa sobre o pacote re (regular expressions)
- Expressões regulares são uma matéria indivual (pesquisar mais)

- Exemplo de sintaxe ou regra:

```python
    #exemplos
    import re

    string = "O Gato come sua língua?"

    #verificar se a string começa com "O
        # E se termina em língua

   pesquisa_regex = re.search("^O.*Língua$", string) #ambas precisam ser True para return True
        #caracteres especiais
            # ^ (se começa com)
            # . (qualquer carac menos quebralinha)
            # * (0 ou mais occorencias)
            # $ (se termina com)
    print(pesquisa_regex) #return true

    if pesquisa_regex:
        #retorna se correspondente
        print("sim o gato comeu minha língua")
    else:
        print("Não, Não comeu)
```

#### 2. Função Search()

- informa sobre a função search().
  - faz uma pesquisa de regex em uma string, e retorna True/False
  - informa que se fizer mais de uma apenas a primeira é retornada
  - iunforma sobre o objeto start()
    - que faz um retorno da posição da correspondencia

- EXPLICAÇÃO.
- Exemplo de sintaxe ou regra:

```python
    #Exemplos
    import re

    string = "O amor é o calor, que aquece a minha alma"
    string_sem_espaco = "Brasil"

    search_regex = re.search("\s", string)
        # \s (onde a string tiver um espaço em branco)

    new_search_regex = re.search("Brazil", string_sem_espaco)

    #retornar se teve
    print(search_regex)
        #return <re.Match object; span=(1,2), match=' '>

    #retornar posição
    search_regex = sr
    print(f"O primeiro espao esta na posição {sr.start()}")
    new_search_regex = nsr
    print(f"O retorno sem correspondia é {nsr)}")
        #return None
```

#### 3. Função Findall()

- informa que ela retorna todas as correspondencias encontradas.
- informa que o retorno é list, com os values ou vazia

- Exemplo de sintaxe ou regra:

```python
    #Exemplos
    import re

    string = "O amor é o calor, que aquece a minha alma"

    regex_findall = re.findall("or", string)
    regex_not_find = re.findall("er", string)
    print(regex_findall)
        #return list ["or", "or"]

        #retorna na ordem que encontra 1 - amor 2 - calor
    print(regex_not_find)
        #return []
        #⚠ sempre retorna um list, se sem corresp return []

    if regex_findall:
        #qtd = 0
        #for n in regex_findall:
        #    #n = "or" (value in list)
        #    qtd += 1
            #gambiarra desnecessaria por ser list pode-se usar len()

        print(f"Há {len(regex_findall)} correspondencias!")
    else:
        print("Não há correspondencias")
```

#### 4. Função Split()

- informa que ela retorna uma string para cada divisão onde ocorrecu correspond.
- informa sobre o param maxsplit.
- Exemplo de sintaxe ou regra:

```python
    #Exemplos
    import re

    string = "O amor é o calor, que aquece a minha alma"

    split_regex = re.split(",", string)
    print(split_regex)
        #return uma list ["O amor é o calor","que aquece a minha alma"]
        #⚠ Note que ele exclue da str o separador
            #ou seja split("or", string)
            #return ["O am", "é o cal", ...]

    #controlar o max de ocorrencias
    maxs_plit_regex = re.split("\s", string, 2)
    print(max_split_regex)
        #return uma list ["O", "amor", "é o calor, que aquece a minha alma"]
        # \s a cada espaço split no max 2 vezes
        #⚠Note que a porção final vem identica sem split
```

#### 5. função sub()

- informa que substitui as ocorrecias pelo valor inforado.
- informa sobre o parametro count pára a qtd de subst.
- Exemplo de sintaxe ou regra:

```python
    #Exemplos
    import re

    string = "O amor é o calor, que aquece a minha alma"

    sub_var = "ódio"

    sub_regex = re.sub("amor", sub_var, string)
    print(sub_regex)
        #return "o ódio é o calor...."

    #controlando a qtd de subst
    count_sub_regex = re.sub("a", "A", string, 2)
    print(count_sub_regex)
        #return "o Amor é o cAlor, que aquece..."
        #substitui só a qtd informada de ocorrencias
```

### Objetos de Correspondência

### Sequencias Especiais

### Conjuntos

#### N. TOPICO

- EXPLICAÇÃO.
- EXPLICAÇÃO.
- Exemplo de sintaxe ou regra:

### x. 🛠️ Revisões

::to-review:: 09-05-2026 ::REVISAO-PADRAO::

💻 Notas / Código

```python
# Seu código aqui
```
