# 📂 Seção 20 : Iteradores

## 📑 Quick section

> **Status:** 🟡 ANDAMENTO | **Data:** 27/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../Home.md) |
| :------------------- | :------------------------------- |
| &#8657; **Anterior** | [ANTERIOR](./arquivo1.md)        |
| &#8659; **Próximo**  | [PROXIMO](./arquivo2.md)         |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [x] **[Vídeo 95](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884320#overview):** iteradores — _(10min)_
- [x] **[Vídeo 96](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884330#overview):** criando — _(7min)_
- [x] **[Vídeo 97]<https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884338#overview>):** stop iteration — _(5min)_

> **Nota rápida:** [Assunto básico]

---

### 📝 Anotações e Conceitos Chave

#### 1. O que é?

- um objeto que pode ser iterado, ou percorrer seu valores.
- implementa o protocolo `iter` e `next`.
- iteradores e iteravies (⚠ Mnemonica: O vel contém a dor)
  - Iterable/Iteráveis : (list, set, dict, str, tuple), são containeres (É o objeto que contém os dados e "sabe" retornar um iterador)
  - Iterator/Iteradores: É o objeto que "anda" sobre o iterável e sabe qual é o próximo valor (é o que resulta de iter(objeto)
    - ⚠O objeto em si (value, Key) não é um iterador é um value.
    - O iterador é o que sobrevoa os objetos

- menciona o loop for para navegação que já faz o uso implicito de iter e next
- Exemplo de sintaxe ou regra:

```python
    #exemplo

    my_tuple = ("value1", "value2")
    my_iterator = iter(my_tuple) #armazena os value

    print(next(my_iterator)) #return value1
        #avança entre os iteradores
    print(next(my_iterator)) #return value2

    for iterator in my_tuple:
        print(iterator) #return value1
          #a cada next retorna um iterator

    #================================================

    string_iterable = "ABC"
    string_iterator = iter(string_iterable)

    print(next(string_iterator)) #return A
    print(next(string_iterator)) #return B
    print(next(string_iterator)) #return c


```

#### 2. Como criar um iterador? | Stop Iteration?

- usando iter e next em classes conseguimos transformar "tudo" em iter.
- informa a sintaxe `__iter__` e `__next__`, para criação dde iteraveis
- informa a sintaxe `raise StopIteration`
- Exemplo de sintaxe ou regra:

```python
    #exemplo

    class MeusNumeros:
        def __iter__(self):
            self.atual = 1
                #começa a sequencia em 1
            return self
                #retorna o proprio num

        def __next__(self):
            #adicionando o stop
            if self.atual <= 20:
                novo_valor = self.atual
                    #recebe o proprio valor antes do incremento
                    #e armazena em um var auxiliar
                self.atual += 1
                    #incrementa crescente
                return novo_valor
                    #retorna o num incrementado
            else:
                raise StopIteration
                #apos o maximo de 20 dá stop


    meu_num = MeusNumeros()
        #cria o objeto da classe

    meu_iterador = iter(meu_num)
        #cria o valor do iterador baseado na classe do objeto

    i = 0
    while i < 10:
        print(next(meu_iterador)) #returna um contador crescente
        i += 1

    #usa-se stop interation
        #para evitar uso de loops ou loop infinito na iteração em si
    for each_iterator in meu_iterador:
        print(each_iterator) #sem  a sintaxe StopIteration daria loop infinito


```

### x. 🛠️ Revisões

::to-review:: 29-04-2026 ::Iteradores Python::

💻 Notas / Código

```python
# Seu código aqui
```
