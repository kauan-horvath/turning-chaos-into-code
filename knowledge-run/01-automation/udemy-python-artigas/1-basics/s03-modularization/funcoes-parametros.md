# 📂 Seção 16 : Funções e Parâmetros

## 📑 fUNÇÕES

> **Status:** 🟡 ANDAMENTO | **Data:** 20/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../../0-organization/python-artigas-home.md) |
| :------------------- | :---------------------------------------------------------------- |
| &#8657; **Anterior** | [ANTERIOR](./loops-repeticao.md)                                  |
| &#8659; **Próximo**  | [PROXIMO](./arquivo2.md)                                          |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 75](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794068#overview):** Funções — _(10min)_
- [✅] **[Vídeo 76](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794072#overview):** Parâmetros — _(10min)_
- [✅] **[Vídeo 77](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794078#overview):** Argumentos — _(10min)_
- [✅] **[Vídeo 78](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794080#overview):** Valor Padrão — _(10min)_
- [✅] **[Vídeo 79](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794090#overview):** Lista como Argumento — _(10min)_
- [✅] **[Vídeo 80](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794096#overview):** Declaração de passagem — _(3min)_
- [✅] **[Vídeo 81](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794092#overview):** Recursividade — _(10min)_
- [✅] **[Vídeo 82](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28794104#overview):** Lambda — _(10min)_

> **Nota rápida:** [Animado para aprender lambda e lista como argumento]

---

### 📝 Anotações e Conceitos Chave

#### 1. Funções | Parâmetros | Param como Palavra-chave | valor padrão

- informa que são agrupamentos de tarefas.
- informa que podem receber argumentos e parametros.

- Exemplo de sintaxe ou regra:

```python
    #Função básica e seus nomes, e chamando a função
        def uma_funct(um_parametro):
            print("essa é uma função")

        uma_funct("um_argumento")
            #chamando a função para usar quantas vezes quiser

    #função com Argumentos e parâmetro com lista
        darths = ["Anakin Skywalker", "Darth Vader"]

        def cumprimento(nomes_input):
            # Verifica se o que chegou é uma lista
            if isinstance(nomes_input, list):
                for nome in nomes_input:
                    print(f"Saudações {nome}")
            else:
                # Se não for lista (for só um nome solto), imprime direto
                print(f"Saudações {nomes_input}")

        #fornecendo parametro literal
        cumprimento("Darth Maul")

        #fornecendo parametro em list
        for nome in darths:
            cumprimento(nome)

        #forncendo a lista como parametro
        cumprimento(darths)

        #fornecendo a lista literal
        cumprimento(["nome1", "nome2"])

    #função com retorno | Parametros e Argumentos
        def force_detection(sensitives):
            malignos = ["Darth Vader", "Anakin"]
            bondosos = ["Mestre Yoda", "Obiwan"]

            if sensitives in malignos:
                print("⭕ Este sensitivo é um Sith!")
                return False

            if sensitives in bondosos:
                print("⭕ Este sensitivo é um Jedi!")
                return True

        mestre_yoda = force_detection("Mestre Yoda")
        darth_vader = force_detection("Darth Vader")

        #uma funct pode ter quantos parametros forem necessários
            #necessário fornecer os argumentos para os parametros

        #receber paramentros com *todos
            def muitos_parametros(param_1, param_2, param_3, param_4):
                pass
            muitos_parametros(1, 2, 3, 4)

            def multi_parametros(*param_1234):
                pass
            multi_parametros(1, 2, 3, 4, 5, 6)
            #necessários para quando não se sabe a quantidade de param

        #função com parametro como palavra chave (para ordem diversa)
            def parentesco(primeiro, segundo, terceiro):
                print(primeiro)
                print(segundo)
                print(terceiro)

            parentesco(terceiro="josé", segundo="kauan", primeiro="maria")

            #utilizando **parametro (Param como DICT)

            def ninjas(**jutsu):
                print(jutsu)

                for ninja, poder in jutsu.items():
                    print(f"{ninja},{poder}")

            ninjas(naruto="rasengan", sasuke="sou eu bola de fogo")

            #usar como dicionário faz com que eu forneça argumentos a partir de chaves escolhidas ou forneça um dict como argumento
            #posso manipular o parametro na função como um dict

        #função com valor padrão
            def meu_pais(pais="Brasil"):
                print(pais)

            meu_pais("tatooine")
            meu_pais() #sem nada daria erro mas como coloquei padrao nao

```

#### 2. Função Recursiva

- Informa que é uma função que chama a si mesma.
- EXPLICAÇÃO.
- Exemplo de sintaxe ou regra:

```python
    #Exemplos

    def repetir(n):
        for x in range(n):
            print(f"repetição {n}")

    repetir(10)

    #função recursiva
    def repetir_recursivo(n):
        if n > 0:
            print("fiz o recurso")
            repetir_recursivo(n-1)

    repetir_recursivo(5)

```

#### 3. Função Lambda

- função anonima que recebe n argumentos mas só da um return

- Exemplo de sintaxe ou regra:

```python
    #Exemplo

    func = lambda arg : arg + 10
    resultado = func(5) #return 15

    nova_func = lambda arg1, arg2 : arg1 * arg2
    resultado = nova_func(2, 5)

    #função com lambda interno
    def multiplica(n):
        return lambda arg : arg * n

    var_duplicadora = multiplica(2)
    var_triplicadora = multiplica(3)

```

### x. 🛠️ Revisões

::last-review:: 22-04-2026 :: Funções e Param/Args::

> > > > aproveitamento 90% - revisao longa

::to-review:: 29-04-2026 ::Funções e Param/Args::
