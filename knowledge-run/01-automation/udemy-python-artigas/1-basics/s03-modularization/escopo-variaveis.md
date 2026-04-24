# 📂 Seção 21 : Escopo Global vs Local

## 📑 ESCOPO DE VARIÁVEIS

> **Status:** 🟡 CONCLUIDO | **Data:** 23/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../../0-organization/python-artigas-home.md)          |
| :------------------- | :------------------------------------------------------------------------- |
| &#8657; **Anterior** | [ANTERIOR](./funcoes-parametros.md)                                        |
| &#8659; **Próximo**  | [PROXIMO](../../2-intermediate/s04-advanced-structures/poo-fundamentos.md) |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [x] **[Vídeo 01](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884366#overview):** Escopo Global — _(06min)_
- [x] **[Vídeo 02](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884370#overview):** Escopo Local — _(09min)_

> **Nota rápida:** [Assunto simples apenas para registro]

---

### 📝 Anotações e Conceitos Chave

#### 1. Acesso ao escopo

- informa que o aninhamento de funções permite o acesso do escopo.
- relata onde é o ambito local e global.
- informa sobre a palavra chave global

- Exemplo de sintaxe ou regra:

```python
    #EXEMPLOS

    def my_func():
        x = 300
        def my_inner_func():
            print(x) #faz parte do escopo da my_func (local)
        my_inner_func() #acessa o escopo com sucesso
    my_func()

    y = 300
    def my_func_2():
        print(y) #acessa o global com sucesso
    my_func_2()

    def my_func_3():
        y = 150
        print(y) #acessa o local 150 mas nao altera
    my_func_3()

    def my_func_4():
        global y
        y = 150
        print(y) #acessa o global
        #com global y, sobrescreve 300 por 150
    my_func_4()
```

### x. 🛠️ Revisões

::to-review:: 25-04-2026 :: Escopo de Variável ::
