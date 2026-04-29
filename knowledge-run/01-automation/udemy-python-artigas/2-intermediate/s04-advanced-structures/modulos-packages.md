# 📂 Seção 22 : Organização de Código: Módulos e Packages

## 📑 Módulos

> **Status:** 🟡 ANDAMENTO | **Data:** 29/04/2026

### 🌐 Navegação rápida

| **🏠 HOME**          | [Retornar ao Início](../Home.md) |
| :------------------- | :------------------------------- |
| &#8657; **Anterior** | [ANTERIOR](./arquivo1.md)        |
| &#8659; **Próximo**  | [PROXIMO](./arquivo2.md)         |

---

### 📺 Conteúdo em Vídeo (Udemy)

- [x] **[Vídeo 100](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28884390#overview):** Módulos — _(10min)_
- [ ] **[Vídeo 02](LINKDOVIDEO):** NomeVídeo — _(Duração)_
- [ ] **[Vídeo 03](LINKDOVIDEO):** NomeVídeo — _(Duração)_

> **Nota rápida:** [descobri esse tema atraves do jogo thhe farmer was replaced super interessante]

---

### 📝 Anotações e Conceitos Chave

#### 1. Módulos

- informa que são um arquivo com um conjunto de funções que podem ser importados, em outros
- informa que são como as bibliotecas mas a partir do seu próprio diretório.
- informa que pode contar variaves, arrays e etc
- (aliasing) - informa sobre a palavra chave import e abreviar com as
- informa que ao importar criar cache do uso
- Exemplo de sintaxe ou regra:

```python
    #Exemplos

    #Arquivo 1 (MeuModulo.py)
        def boas_vindas(nome):
            print(f"Datebayo {nome} sensei")

        ninja = {
            "nome":"Naruto",
            "jutsu":"Rasengan",
        }
    #Arquivo 2
        #import MeuModulo
        import MeuModulo as mm

        #chamar
        #MeuModulo.boas_vindas("Kauan")
            #depois de abreviar a versão completa do nome dá erro
        mm.boas_vindas("Kauan")

        qual_jutsu = mm.ninja["jutsu"]
        print(qual_jutsu)
            #return "Rasengan"
```

#### 2. Modulos Intregados

- informa que existem varios e cita alguns.
- platform, dir

- informa como acessar os recursos e funções dos módulos usando o dir

- Exemplo de sintaxe ou regra:

```python
    #exemplo
    import platform as plat

    x = plat.system()
    print(x) #return windows

    lista_dir = dir(plat) #⚠ o alias persiste até aqui

    for i in lista_dir:
        print(i) # return um a um do list de métodos
```

#### 3. Importar parte do módulo

- informa que o uso do from importa só uma parte.
- professor nao explica mas é importante esse uso pois o import roda o arquivo uma vez ao chhamar, e dependendo da construção, ausencia de `if __name__ == "__main__":`, o arquivo pode acabar rodando coisas indesejadas e bugando.

- Exemplo de sintaxe ou regra:

```python
    #Exemplos

    #Arquivo 1 (MeuModulo.py)
        def boas_vindas(nome):
            print(f"Datebayo {nome} sensei")

        ninja = {
            "nome":"Naruto",
            "jutsu":"Rasengan",
        }

        if __name__ == "__main__":
            print("Executando testes locais do módulo...")
            boas_vinda("teste")
            #area dedicada a testar o módulo sem chamar pelo arquivo original que usará este, evita funções abertas por acidente e só execcuta ao se rodar diretamente por aqui

    #Arquivo 2
        from MeuModulo import ninja, boas_vindas

        nome = ninja["nome"]
            #nao precisa de meumodulo.ninja pois agora é parte desse arquivo

        boas_vindas(nome) #return Naruto

```

### x. 🛠️ Revisões

::to-review:: 01-05-2026 ::Módulos::
