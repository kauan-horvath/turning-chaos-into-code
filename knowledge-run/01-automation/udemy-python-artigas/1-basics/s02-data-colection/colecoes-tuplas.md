# 📂 **Seção 10:** Tuplas: Imutabilidade e Performance

## 📑 Tuplas

> **Status:** 🟡 CONCLUIDO | **Data:** 13/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../../0-organization/python-artigas-home.md) |
| :------------------- | :---------------------------------------------------------------- |
| &#8657; **Anterior** | [ANTERIOR](./colecoes-listas.md)                                  |
| &#8659; **Próximo**  | [PROXIMO](./colecoes-sets.md)                                     |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 41](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28528767#overview):** Tuplas Python — _(13min)_
- [✅] **[Vídeo 42](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28528777#overview):** Acessando Itens — _(13min)_
- [✅] **[Vídeo 43](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28528785#overview):** Atualizar Tuplas — _(12min)_
- [✅] **[Vídeo 44](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28528791#overview):** Descompactando Tuplas — _(10min)_
- [✅] **[Vídeo 45](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28528793#overview):** Loops — _(11min)_
- [✅] **[Vídeo 46](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28528803#overview):** Juntas Tuplas — _(3min)_
- [✅] **[Teste 05](https://www.udemy.com/course/python-completo-e-profissional/learn/quiz/5346084#overview):** Teste — _(00min)_

> **Nota rápida:** [Espaço para algum insight importante do conjunto de vídeos]

---

### 📝 Anotações e Conceitos Chave

#### 1. Tuplas

- Sintaxe entre parentes =(" ",)
- Informa que são ORDENADAS E IMUTAVEIS.
- gemini informa:

💡 Por que usar Tuplas em vez de Listas?

**Performance**: Tuplas são processadas mais rápido que listas.
**Segurança**: Garante que dados sensíveis (como configurações ou coordenadas GPS) não sejam alterados por erro humano ou bugs.
**Dicionários**: Tuplas podem ser usadas como chaves de dicionários; listas não.

- Exemplo de sintaxe ou regra:

```python
    # Exemplos
genius = ("Azul","Vermelho","Amarelo","Azul", "Verde")
    # Azul pode ser valor igual
    # porque o index e posição é unico e diferente
    #a ordem nao mudará após a criação

genius_1item = ("Amarelo", ) #uma virgula após o 1 item
genius_string = ("Amarelo")

    type(genius_1item) #<class "tuple">
    type(genius_string) #<class "Str">

genius_Tdah = ("Azul", True, "Vermelho", 2, "Amarelo")
    #aceita tipos variados

#metodo construtor (casting)
resposta = "Azul","Vermelho","Amarelo","Azul", "Verde"
resposta_tupla = tuple(resposta)

```

#### 2. Acessando Itens

- Informa que acessa através do Index.
- Informa o método .count()
- informa o metodo .index("value')
- Exemplo de sintaxe ou regra:

```python
  # Exemplos
    genius = ("Azul","Vermelho","Amarelo","Azul", "Verde")

    #Acesso por index
    primeira_cor = genius[0]
    ultima_cor = genius[-1]

    #Usando os metodos
    quantas_cores = len(genius) #retorna 5
    onde_verde = genius.index("Verde") #retorna 5

    quantos_azuis = genius.count("Azul") #retorna 2
    onde_azul_repetido = genius.index("Azul")
        #retorna APENAS 0 (a primeira ocorrencia)
        #para localizar repetidos necessario loop
```

#### 3. Atualizando Tuplas

- Informa que sendo imutável o truque é transformar em listas, alterar e voltar a Tupla.
- informa que é possível adicionar tuplas de tuplas.
- Exemplo de sintaxe ou regra:

```python

    #BURLANDO COM CONVERSÂO
    genius = ("Azul","Vermelho","Amarelo","Azul", "Verde")

    #genius.remove("Verde") #retorna erro
    list_genius = list(genius)
    list_genius.append("Toranja")
    list_genius.remove("Toranja")
        #todos os modificadores de lista
    genius = tuple(list_genius) #volta a ser tupla

    #============================

    #BURLANDO COM CONCATENAÇÃO
    #adicionar tuplas com tuplas
    cor = ("Azul",) ⚠️ Virgula para formar Tuple
    genius += cor
    #retorna "Azul","Vermelho","Amarelo","Azul", "Verde", "Azul"

    #============================
    #Não é possível remover itens, mas é possível deletar a lista
    del genius

```

#### 4. Descompactação

- Informa que.descompactar os dados facilita algumas alterações
- informa sobre a sintaxe do asterisco na descompactação.
  - ⚠️ A descompactação sempre retorna LIST
- Exemplo de sintaxe ou regra:

```python
    #Exemplos
    genius = ("Azul","Vermelho","Amarelo","Azul", "Verde")

    (cor_azul, cor_vermelha,, cor_amarelo, *resto_cores) = genius
        #para tamanhos desproporcional usa-se astericos
        resto_cores.append("Laranja")
        #retorna "Azul", "Verde","Laranja" POIS É UMA LIST*

    #se o asterico estiver no meio, ele pega o intervalor do meio
    (cor_azul, *cores_do_meio, cor_verde) = genius
        #manipular valores individuais em list
        #ja que nao é possível alterar a tupla geral

```

#### 5. Loops em tuplas

- Informa que é o padrão para exrtação de valores individuais.
- Relata como.
- Exemplo de sintaxe ou regra:

```python
    #Exemplos
    genius = ("Azul","Vermelho","Amarelo","Azul", "Verde")

    #loop por valor
    for cor in genius:
        print(cor)

    #loop por index
    for index_cor in range(len(genius)): #⚠️ Necessario usar RANGE()
        print(index_cor)
        print(genius[index_cor]) #retorna cor a partir do index

    #loop while
    i = 0
    while i < len(genius):
        print(genius[i])
        i += 1 #incrementa senão repete o mesmo index

```

#### 6. Juntar Tuplas

- Informa que é possível juntar através da Concatenação.
- Informa qu também é possível juntar através da multiplicação.
- Exemplo de sintaxe ou regra:

```python
  # Exemplos
    genius = ("Azul","Vermelho","Amarelo","Azul", "Verde")
    cesta_frutas = ("Blueberry", "Morango", "Banana", "Blueberry", "limão")

    minstura = genius + cesta_frutas
    dobra_tupla = genius * 2 #multiplica a mesma tupla
    #retorna ("Azul","Vermelho",.. "Azul","Vermelho",..)

```

#### 7. Teste

1. Os itens de tupla NÃO são ordenados, imutáveis ​​e NÃO permitem valores duplicados | False
2. Em Python, podemos extrair os valores de uma tupla para variáveis individuais. Isso é chamado de "desempacotamento" | True

### x. 🛠️ Revisões

::last-review:: 15-04-2026 :: Tuplas::
aproveitamento 80% - Revisão proxima: [revisão gemini](https://gemini.google.com/share/54c461b4a8d5)

Pontos fortes
Operações Básicas e Sintaxe: Você demonstra excelente domínio sobre a criação de tuplas, incluindo o caso especial de itens únicos (uso da vírgula) e o uso da função construtora tuple().
Imutabilidade e Segurança: Você compreende perfeitamente que tuplas não podem ser alteradas diretamente e entende as vantagens de performance e segurança que isso traz para o código.
Manipulação de Coleções: Mandou muito bem em conceitos de concatenação, repetição de elementos e na lógica de conversão entre listas e tuplas para contornar restrições de alteração.
Iteração: Mostrou conhecimento sólido sobre como percorrer tuplas usando loops for e while, incluindo o controle de índices e a lógica de evitar loops infinitos.
Áreas a melhorar
Ordenação vs. Mutabilidade: Cuidado para não confundir 'Ordenado' com 'Mutável'. Tuplas são ordenadas (mantêm a ordem de inserção), mas são imutáveis (não podem ser alteradas). Uma das questões foi respondida incorretamente por essa confusão.
Unpacking (Descompactação): Ao usar o asterisco (\*) na descompactação, o Python sempre agrupa os valores restantes em uma LISTA, mesmo que a origem seja uma tupla. Revise também o acesso a variáveis específicas durante o unpacking para não pular índices.
Métodos de Sequência: Lembre-se que tuplas em Python não possuem o método .find() (comum em strings); para localizar índices em tuplas, utilizamos exclusivamente o .index().
Identificação de Tipos: Fique atento aos parênteses: em Python, apenas colocar algo entre parênteses como ("Azul") não cria uma tupla, mas sim uma String. A presença da vírgula é o que define a estrutura de tupla.

::Last-review:: 19-04-2026 ::Tuplas e seus detalhes::

> > > > Aproveitamento 80% - revisão próxima

Entender melhor o Range(len()):

Pontos fortes
Conceitos Fundamentais e Imutabilidade: Você demonstrou domínio total sobre a natureza imutável das tuplas e a importância dessa característica para a integridade dos dados e performance de memória.
Métodos e Acesso a Dados: Sua compreensão sobre como acessar itens (incluindo indexação negativa), usar o método .count() e identificar índices de ocorrência está excelente.
Iteração e Controle: Você entende bem como percorrer tuplas usando loops for e while, além de dominar a lógica de descompactação (unpacking) básica.
Áreas a melhorar
Operações de Repetição e Concatenação: Atenção ao operador de multiplicação (\*). Ele repete os elementos individualmente dentro da mesma estrutura, em vez de criar tuplas aninhadas.
Sintaxe de Criação e Conversão: Lembre-se de que a função tuple() em uma string cria uma tupla de caracteres individuais, e que uma tupla pode ser criada apenas separando valores por vírgulas, mesmo sem parênteses.
Manipulação Indireta: Embora entenda a teoria da imutabilidade, você se confundiu ao achar que métodos de lista (como .append()) funcionariam em tuplas. Tuplas não possuem métodos de alteração in-place.
