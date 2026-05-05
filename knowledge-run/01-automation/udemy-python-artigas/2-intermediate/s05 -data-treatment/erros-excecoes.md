# 📂 Seção 28 : Tratamento de Exceções e Debugging (Try/Except)

## 📑 Try Except Finally

> **Status:** 🟡 ANDAMENTO | **Data:** 05/05/2026

### 📺 Conteúdo em Vídeo (Udemy)

- [x] **[Vídeo 132](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109354#overview):** Manipulação de Exceção — _(06min)_
- [x] **[Vídeo 133](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109362#overview):** Muitas excecções — _(07min)_
- [x] **[Vídeo 134](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109368#overview):** Bloco Finally — _(05min)_
- [x] **[Vídeo 135](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109382#overview):** lançar exception — _(10min)_

> **Nota rápida:** [Ja usei mas quero aprender com detalhes]

---

### 📝 Anotações e Conceitos Chave

#### 1. Manipulação de Exceção

- informa sobre o tratamento de erros.
- gemini informa: é uma convenção colocar no try, apenas a área passível de erro, e não todo o script, para faciliar identificar erros locais.
- Exemplo de sintaxe ou regra:

```python
    #Exemplos
    #x = "teste"
    print(x) #return erro por NameError

    #corrigindo
    try:
        #try só roda se não encontrar erro
        print(x) #vai retornar NameError
        #mas o try jogará para o except
    except:
        print("Deu erro em algo")

```

#### 2. Exceções específicas / Bloco Finally

- informa que é possível nomear qual erro.
- informa sobre o else no try.
- Exemplo de sintaxe ou regra:

```python
    #exemplos

    #x = "teste"

    try:
        print(x) #return NameError
    except NameError:
        print("A var não foi definida e retornou NameError")
    except:
        print("Houve algum problema inespecífico")
    else:
        print("Rodo esse bloco apenas se rodar o Try")
    finally:
        print("Rodo esse bloco, independente do successo ou falha do try")
        #serve para fechar objetos de arquivos com erro ou não, e evitar overload de memória
```

#### 3. Raise/Lançar uma exceção

- informa que podemos lançar um erro em alguma condição.
- forçar um erro próprio e não de estrutura padrão.
- informa que podemos usar erros-chave
- Exemplo de sintaxe ou regra:

```python
    #exemplos

    x = 5

    if x < 0:
        raise Exception("Não é permitido número negativo")

    y = "cinco"

    if not type(y) is int:
        raise TypeError("São permitidos apenas números")

```

### x. 🛠️ Revisões

::to-review:: 07-05-2026 ::Try Except::
