# 📂 Seção 12 : Dicionários: Estruturas de Chave-Valor

## 📑 Dictionaries

> **Status:** 🟡 CONCLUIDO | **Data:** 15/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../../0-organization/python-artigas-home.md) |
| :------------------- | :---------------------------------------------------------------- |
| &#8657; **Anterior** | [ANTERIOR](./colecoes-sets.md)                                    |
| &#8659; **Próximo**  | [PROXIMO](./matrizes-arrays.md)                                   |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 53](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28693042#overview):** Dictionaries — _(15min)_
- [✅] **[Vídeo 54](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28693058#overview):** Acessando Itens — _(16min)_
- [✅] **[Vídeo 55](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28693048#overview):** Alterando itens — _(05min)_
- [✅] **[Vídeo 56](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28693070#overview):** Adicionando Itens — _(05min)_
- [✅] **[Vídeo 57](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28693076#overview):** Removendo itens — _(06min)_
- [✅] **[Vídeo 58](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28693086#overview):** Loop em Dicts — _(10min)_
- [✅] **[Vídeo 59](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28693094#overview):** Copiar dicts — _(05min)_
- [✅] **[Vídeo 60](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28693098#overview):** Aninhamento de dicts — _(10min)_
- [✅] **[Teste 07](https://www.udemy.com/course/python-completo-e-profissional/learn/quiz/5346088#overview):** Teste — _(00min)_

> **Nota rápida:** [Espaço para algum insight importante do conjunto de vídeos]

---

### 📝 Anotações e Conceitos Chave

#### 1. Chave-Valor

- informa que guarda em pares.
- informa que são ORDENADAS, ALTERAVEL, NAO DUPLICA, NÃO INDEX
  - curiosidade (ordenas a partir de uma versão tardia 3.6)
- informa que a chave duplicada é sobrescrita pela nova

- Exemplo de sintaxe ou regra:

```python
    #Exemplos
    dict = {
        "chave":"valor",
        "chave2":"valor2",
        } #é padrão dividir as chaves em cada linha,

    dict[0] #return Keyerror
    dict["chave"] #return "valor"

    #===============================================

    ficha_personagem = {
        "nome":"Thanatos",
        "nome":"thathazinho da mamãe",
        "apelido":"Morte serena",
        "equivalentes": ["Mors", "Orcus"],
        "inimigos": ["sísifo", ],
        "inventário": ["Asas", "Tocha Apagada"]
    }

    ficha_personagem[1] #return Keyerror
    ficha_personagem["nome"] #return "thathazinho.." por sobrescrever

    # não perminte duplicar nem contabiliza
    print(len(ficha_personagem)) #retorna 5 (par chave:valor)
            #descartando a repetição

    type(ficha_personagem) #return <class "dict">

```

#### 2. Acessando itens

- Informa sober atribuição
- Informa sobre o método get
- informa sobre a adição de dados
- informa sobre o metodo keys
- informa sobre o metodo values
- informa sobre o metodo ITEMS (com M)
- informa sobre o uso de in

- Exemplo de sintaxe ou regra:

```python
    #Exemplos

    status = {
        "força": 0,
        "agilidade": 0,
        "vidas": 3
    }

    #Acessando valores

        #diretamente dict["chave"]
        forca = dict["força"]
            #se a chave ao for encontrada return KeyError

        #Com metodo get
       agilidade = dict.get("agilidade")
            #se chave nao encontrada return None

        #adicionando dados
            #chave existente
        status["agilidade"] = 1
            #chave nova
        status["destreza"] = 0
            #a nova chave foi adicionada
            #com valor 0 no dict original

    #Metodos de visualização
        #metodo keys() > para visualizar chaves
        show_stats = status.keys()
            #returna força. aggilidade, vidas e o novo destreza

        #metodo values() > para visualizar valores
        show_values = status.values() #retorna 0.0. 3 e 0

        #metodo items() > para visualizar chave e valor
            #retorna em tuplas ("chave", "valor")
        show_itens = status.items()
            #retorna (forca, 0), (agilidade, 1) ...

        #uso do in
        if "vidas" in status:
            print("vidas esta nesse dict")
```

#### 3. Alterando | Adicionar

- informa sobre a alteração direta.
- informa sobre a ateração com update().
- informa que adicionar é alterar pra uma key que nao existe

- Exemplo de sintaxe ou regra:

```python
    #Exemplos
    linguagens = {
        "Automação":"Java",
        "Web Stack":"Css"
    }
    #substituindo valor
        #dict["chave"] = "novo valor"
        linguagens["Automação"] = "python"
        #adicionar por não haver a chave:
            #linguagens["Low Code"] = "Vba"

    #objeto iteravel para alterar chave e valor
    linguagens.update({"Web Stack":"Html"})
        #update sem a chave tambe adiciona
            #linguagens.update({"Low Code":"Vba"})

    dba = {"Database":"Sql"}
    linguagens.update(dba)

    # Resultado final de 'linguagens':
        # {
        #   "Automação": "python",
        #   "Web Stack": "Html",
        #   "Database": "Sql"
        # }
```

#### 4. Remover | Iterar

- informa sobre o Método pop()
- informa sobre o metodo popitem()

- informa sobre a palavra chave del
- informa sobre o metodo clear()

- Informa o uso de loop for (que retorna os keys)

- Exemplo de sintaxe ou regra:

```python
    #Exemplos

    cronos = {
        "Filha 1": "Héstia",
        "Filha 2": "Deméter",
        "Filha 3": "Hera",
        "Filho 1": "Hades",
        "Filho 2": "Poseidon",
        "Filho 3": "Pedra"
    }

    salvador = {"Filho 3": "Zeus"}

    #Remover com o metodo pop()
    cronos.pop("Filha 1") #remove a chave e valor a partir da chave

    #remover com o del
    del cronos["Filha 2"] #remove a chavevalor

    #del cronos #remove tudo incusive o dict
    #remover com o popitem()
        #inicio do fim
    cronos.popitem() #remove o ultimo chavevalor ("Filho 3")

    #===================================
    #apenas com Chaves
    for ordem_nascimento in cronos:
        print(f"qual ordem do filho: {ordem_nascimento}")
            #sem index retorna key

        for ordem_nascimento in cronos.keys():
            #equivalente a interar por index,
            #mas direto pelo laço for
            print(ordem_nascimento)

    #Apenas valores
    for ordem_nascimento in cronos:
        print(f"qual o nome do filho: {cronos[ordem_nascimento]}")
            #com index retorna value

        for nome_filhos in cronos.values():
            #equivalente a interar por index,
            #mas direto pelo laço for
            print(nome_filhos)

    #com Chave e valor
    for ordem, nomes in cronos.items():
        print(f"A ordem: {ordem} e o nome: {nomes}")
        #nativamente por chave e valor

    #remover com clear()
        #Zeus derrota cronos
    cronos.clear() #esvazia mas nao deleta

```

#### 5. Copiar Dicts

- informa que referencia não copia dict1 = dict2
- informa o metodo copy() dic2 = dict1.copy() gerando o novo
- informa o construtor dict()

- Exemplo de sintaxe ou regra:

```python
    #Exemplos

    #copiar com copy
    novo_dict = dict_antigo.copy()

    #copiar com construtor
    novo_dict = dict(dict_antigo)

```

#### 6. Dicionários Aninhados

- Informa sobre a sintaxe do aninahmento literal.
- informa sobre aninhamento atraves de outro dict ja criado.
- Exemplo de sintaxe ou regra:

```python
    #Exemplos

    pergaminho_kage_bunshin = {
            "Nome": "Kage Bunshin No Jutsu",
            "Tradução":"Jutsu Clone das Sombras",
            "Criador": "Tobirama Senju",
            "Tipo": "Ninjutsu",
            "Selos": ["Selo do Clone (Cruz)"]
        },

    Jutsus_naruto = {
        "Rasengan":{
            "Tradução":"Esfera Espiral",
            "Criador": "Minato Namikaze",
            "Tipo": "Ninjutsu",
            "Selos": None
        },

        "Oiroke No Jutsu":{
            "Tradução":"Jutsu Sensual",
            "Criador": "Naruto Uzumaki",
            "Tipo": "Henge",
            "Selos": ["Carneiro"]
        },

        "Kage Bunshin No Jutsu": pergaminho_kage_bunshin
    }

    #acessando com chave e subchave
    criador_jutsu = Jutsus_naruto["Rasengan"]["Criador"]
        #["key"]["subkey"]

    #Acessando com index
    selo_jutsu = Jutsus_naruto["Oiroke No Jutsu"]["Selos"][0]
        #["key"]["subkey_list"][index]
        #retorna a partir do index da subkey list (selos)

```

#### 7. Teste

- Os itens do dicionário são apresentados em pares 'chave: valor' e podem ser referenciados usando o nome da chave. | True.
- O método pop() remove um item aleatório do dictionary. | False.
- Exemplo de sintaxe ou regra:

```python
  # titulo do código

```

### x. 🛠️ Revisões

::last-review:: 18-04-2026 ::Dictionaries::

> > > > aproveitamento: 93% - com consultas revisão intermediária

::last-review:: 23-04-2026 ::Dictionaries::

> > > > aproveitamento: 77% - sem consultas revisão próxima

Pontos fortes
Fundamentos e Estrutura Básica: Excelente compreensão da estrutura de dicionários (pares de chave-valor), como o Python lida com a ordenação a partir da versão 3.6 e o funcionamento da cópia independente de dicionários na memória.
Acesso Seguro e Navegação em Dados: Você domina a iteração com laços `for`, o desempacotamento correto de variáveis (chaves e valores) e a extração de dados em dicionários aninhados. Sabe aplicar perfeitamente o método `.get()` e o operador `in` para evitar interrupções no código por `KeyError`.
Remoção e Limpeza: Demonstrou grande clareza ao diferenciar e utilizar corretamente o método `.pop()` para chaves específicas, o comando `del` (tanto para chaves quanto para a variável em si) e o método `.clear()`.
Métodos Nativos e Operações: Você demonstrou um excelente entendimento sobre o uso de métodos embutidos do Python, como .get(), .items(), .values(), .update(), .pop() e .clear(). Sabe perfeitamente qual comando utilizar para manipular, extrair ou alterar dados com segurança.
Dicionários Aninhados e Estruturas Complexas: Você domina a manipulação de dicionários complexos, mostrando que compreende com clareza a sintaxe necessária para acessar subchaves alocadas profundamente, inclusive quando listas estão misturadas na estrutura.
Fundamentos Lógicos: O seu conhecimento base é bastante sólido. Você compreende muito bem a natureza dos pares de chave-valor, as regras que sobrescrevem chaves duplicadas e o uso de operadores como 'in' para validação de pertinência.

Áreas a melhorar
Métodos de Atualização e Mesclagem (.update): É necessário revisar como combinar dicionários. O operador de soma (`+`) não funciona para dicionários em Python; o correto é utilizar `.update()`. Além disso, o `.update()` insere ou substitui pares no nível atual, mas não cria aninhamentos automáticos ao receber um iterável.
Retorno de Visualizações e Métodos Nativos: Atenção ao que os métodos retornam: `dict.items()` retorna uma visualização contendo os pares originais encapsulados em tuplas, e não uma lista plana. Da mesma forma, nas versões modernas do Python, o método `.popitem()` remove sempre o último par inserido, e não um item aleatório.
Comportamento de Chaves Inexistentes e Duplicadas: Lembre-se de que acessar diretamente uma chave que não existe via colchetes (`dict['chave']`) retorna um erro fatal (`KeyError`) ao invés de criar a chave com `None`. Também é bom notar o impacto na função `len()` ao declarar chaves duplicadas na mesma inicialização: as duplicatas são sobrescritas, diminuindo a contagem final esperada.
Natureza da Busca por Chaves (vs. Índices): Lembre-se de que dicionários não funcionam com índices numéricos posicionais como as listas. Tentar acessar 'dict[0]' não retorna a primeira posição do dicionário; o interpretador procura por uma chave cujo nome literal seja o número inteiro '0'. Se essa chave não existir, o código resultará em um erro do tipo 'KeyError'.
Iteração Padrão em Laços 'For': Ao iterar diretamente sobre um dicionário utilizando o laço mais simples (ex: 'for variavel in dicionario:'), o comportamento padrão do Python é atribuir apenas as chaves à variável do laço a cada iteração, e não os valores. Para iterar diretamente pelos valores, lembre-se de usar explicitamente o método .values().

::to-review::07-05-2026 ::Dicts e seus detalhes::
