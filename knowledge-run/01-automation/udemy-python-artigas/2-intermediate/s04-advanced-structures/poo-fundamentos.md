# 📂 Seção 19 : POO: Classes, Objetos e Pilares

## 📑 Programação Orientada a Objetos

> **Status:** 🟡 CONCLUIDO | **Data:** 24/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../../0-organization/python-artigas-home.md) |
| :------------------- | :---------------------------------------------------------------- |
| &#8657; **Anterior** | [ANTERIOR](../../1-basics/s03-modularization/escopo-variaveis.md) |
| &#8659; **Próximo**  | [PROXIMO](./arquivo2.md)                                          |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 86](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884180#overview):** Classes e Objetos — _(07min)_
- [✅] **[Vídeo 87](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884194#overview):** Função **init** — _(15min)_
- [✅] **[Vídeo 88](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884208#overview):** Métodos de Objeto — _(07min)_
- [✅] **[Vídeo 89](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884220#overview):** Parâmetros Self — _(05min)_
- [✅] **[Vídeo 90](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884226#overview):** Modificar Propriedades — _(06min)_
- [✅] **[Vídeo 91](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884236#overview):** Excluir Objetos — _(07min)_
- [✅] **[Vídeo 92](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884252#overview):** Herança POO — _(10min)_
- [✅] **[Vídeo 93](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884252#overview):** Classe derivada — _(10min)_
- [✅] **[Vídeo 94](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884280#overview):** Adicionar Prop e Métodos — _(11min)_

> **Nota rápida:** [Assunto novo e interessante to animado para descobrir do que se trata]

---

### 📝 Anotações e Conceitos Chave

#### 1. definições e criação

- informa que um classe irá manter as propriedades para os demais objetos.
- iforma que uma classe é um construtor com plantas e que reproduz para os demais objetos.

- Exemplo de sintaxe ou regra:

```python
    #Exemplos

    class ClasseNova: #classe
        x = 5 #propriedade (Uma var interna da classe)


    print(ClasseNova) #return <class "__main__.ClasseNova">
    objeto1 = ClasseNova() #objeto a partir da classe

    print(objeto1.x) #return 5

```

#### 2. Função init / Parametro Self

- informa que a funçção init serve para definiçç~çao de propriedades do objeto.
  - informa que é possível aloccar valores previos ou definir parametros para o ato da criação do objeto
- informa que self é a nomenclatura para acessar as propriedades em init
  - informa a nomenclatura -> para definir como vaslor padrao

- informa que é um referencia a instancia atual, para ser referenciado
  - nao precisa ser chamado de self, mas precisa ser o primeiro
  - (NAO RECOMENDADO) usei meu_self no exemplo,
    - mas posso criar meu_self_2 para o proximo método por exemplo

- gemini adiciona

1. Explique o self com mais ênfase:
   Muitos iniciantes se confundem com o self. Uma frase que ajuda muito é: "O self é como o dedo da classe apontando para si mesma. Ele garante que o nome do Goku seja do Goku, e não do Vegeta."

2. O método `__str__`:
   Para uma próxima aula, seria legal mostrar o método `__str__`. Sem ele, se você der um print(goku), o Python retorna algo feio como <`__main__`.sayajin object at 0x... >. Com o `__str__`, você personaliza o que aparece no print.

- Exemplo de sintaxe ou regra:

```python
    #exeplos

    #⚠ Classes devem ser criadas com PascalCase
    class NovaPessoa:
        def __init__(meu_self, nome, idade) -> None:
            #self.nome = "Kauan" #pré determinado
            meu_self.name = nome
            meu_self.age = idade #campo para preenchimento do usuário
            #self.age/self.name é a propriedade do objeto
            #nome/idade é o parametro para a propriedade

    objeto_pessoa1 = NovaPessoa("Kauan", 29)
    print(objeto_pessoa1.name) #return Kauan
    print(objeto_pessoa1.age) #return 29

    objeto_pessoa2 = NovaPessoa("João", 20)
    print(objeto_pessoa2.name) #return João
    print(objeto_pessoa2.age) #return 20

    class CriarSayajin:
        def __init__(self, name, power_qtd) -> None:
            self.name = name
            self.power = power_qtd

        def __str__(self) -> str:
            return f"Nome do Sayajin:: {self.name} | Poder: {self.power}"

    goku = CriarSayajin("Goku", "+ de 8000")
    print(goku) # Saída: Sayajin: Goku | Poder: + de 8000

    vegeta = CriarSayajin("Vegeta", "7999")
    print(goku) # Saída: Sayajin: Vegeta | Poder: 7999

```

#### 3. Métodos

- informa que funções dentro da classe, são chamadas de métodos.
  - pois eles podem desempenhar papeis atribuidos direto ao objeto

- gemini adciona:

  | Termo            | O que o aluno deve entender                      |
  | ---------------- | ------------------------------------------------ |
  | Classe           | "O projeto ou a ""Fábrica"" (ex: CriarSayajin)." |
  | Objeto/Instância | O produto saído da fábrica (ex: goku)            |
  | Atributo         | O que o objeto tem (ex: self.name).              |
  | Método           | O que o objeto faz (ex: farmando_ki()).          |
  | `__str__`        | Como o objeto se apresenta para humanos.         |

- Exemplo de sintaxe ou regra:

```python
    #exemplos:

    class NovaPessoa:
        def __init__(self, nome, idade) -> None:
            self.name = nome
            self.age = idade

        def myfunc_metodo(self): #isso é um método
            print(f"olá meu nome é {self.name}")

    pessoa1 = NovaPessoa("kauan", 29)
    pessoa1.myfunc_metodo() # return olá meu nome é Kauan

    class CriarSayajin:
        def __init__(self, name, power_qtd) -> None:
            self.name = name
            self.power = power_qtd

        def __str__(self) -> str: #metodo que altera a saída da classe
            return f"Nome do Sayajin:: {self.name} | Poder: {self.power}"

        def farmando_ki(self, turnos):
            while turnos > 0:
                self.power += 100
                turnos -= 1

    goku = CriarSayajin("Goku", 8000)
        #sem a piada do + de 8000 porque deve ser int ou float para o cálculo
    goku.farmando_ki(10)
    print(goku.power) #return more power than 8000
```

#### 4. Modificar / Excluir Propriedades

- começa pelo pass para não dar erro.
- informa que uma simples atribuição pode alterar as popriedades dos objetos.
- informa que del exclue uma propriedade
-

- Exemplo de sintaxe ou regra:

```python
    #exemplo
    class NovaPessoaTeste:
        pass

    teste_pessoa1 = NovaPessoaTeste() #não tem função mas não da erro

    class NovaPessoa:
        def __init__(self, nome, idade) -> None:
            self.name = nome
            self.age = idade

        def todos_dados(self):
            print(self.name, self.age)

    #alterando uma propriedade
    pessoa1 = NovaPessoa("Kauan", 29)
    pessoa1.name = "João" #sobrescreve o valor da propriedade name, no objeto pessoa1

    del pessoa1.age #aqui o objeto perde essa propriedade


```

#### 5. Herança (Base/Derivada) / init em derivadas / Adicionar prop/metod

- informa que qualquer classe por ser base.
- informa que a palavra super() pode recuperar as propriedades
- Exemplo de sintaxe ou regra:

```python
    #exemplo

    class NovaPessoa:
        def __init__(self, nome, sobrenome) -> None:
            self.name = nome
            self.surname = sobrenome

        def nome_completo(self):
            print(self.name, self.surname)

    pessoa1 = NovaPessoa("Kauan", "Horvath")
    pessoa1.nome_completo() #return Kauan Horvath

    class ClasseHerdeira(NovaPessoa):
            #sintaxe para puxar todas as propriedadeds de outra classe
        pass

    pessoa2 = ClasseHerdeira("João", "Silveira")
    pessoa2.nome_completo() #return João Silveira
        #apesar de utilizar a classe dervada as propriedades são identicas as da classe base

    class NovoEstudante(NovaPessoa):
      #def __init__(self, materia):
            #aqui ela sobrescreve o init da lasse base

        def __init__(self, materia, nome, sobrenome):
            #aqui ele referencia como a base, mesmo com parametro a mais

            #NovaPessoa.__init__(self, nome, sobrenome)
            self.materia = materia #cria um propriedade nova
            super().__init__(nome, sobrenome) #mantem a propriedade de NovaPessoa

        def amor_materia(self, qtd_amor):
            self.qtd_amor = qtd_amor
            print(f"eu amo {self.qtd_amor}, da matéria {self.materia}")


    estudante1 = NovoEstudante("Química", "Kauan", "Horvath")
    estudante1.nome_completo() #return Kauan horvath
        #acessa a propriedade base, mesmo com a nova propriedade do derivado
    print(estudante1.materia)

    estudante1.amor_materia("100%")
    print(estudante1.qtd_amor) #returna ama 100% de quimica
```

#### z. Exercício Gemini

- REgras:

🏆 Sugestão de Exercício Prático (Desafio do Aluno)
Para encerrar o material, peça para eles criarem uma classe Carro:

Atributos: marca, modelo, combustivel (nível de 0 a 100).

Método `__str__`: Exibir "Carro: [Modelo] | Tanque: [Nível]%".

Método dirigir(distancia): Cada 1km rodado consome 1 de combustível. Se o combustível chegar a 0, printar "Sem combustível!".

```python

    class Carro:
        def __init__(self, marca, modelo, combustivel) -> None:
            self.marca = marca
            self.modelo = modelo
            self.combustivel = combustivel

        def __str__(self):
            return (f"Carro: {self.marca, self.modelo} | Tanque: {self.combustivel}.") #⚠lembrar que o metodo self requer return

        def dirigir(self, distancia):
            #self.distancia = distancia
                #distancia nao é uma propriedade do objeto carro
                #nao há necessidade de guardar

            if self.combustivel >= distancia:
                self.combustivel -= distancia
                print(f"voce rodou {distancia} e sobrou {self.combustivel}")
            else:
                faltou = distancia - self.combustivel
                self.combustivel = 0 #resetar o tanque sem negativo

                print(f"Sem Combustível, faltaram {faltou}km")


    carro1 = Carro("Volkswagen", "Fusca", 80)
    print(carro1) # return Carro: Volkswagen Fusca | Tanque: 80%

    carro1.dirigir(90) # return Sem Combustível, Faltaram 10km
    print(carro1.combustivel) #return 0

```

### x. 🛠️ Revisões

::to-review:: 27-04-2026 ::Classes, Objetos, Param/Metodos::
