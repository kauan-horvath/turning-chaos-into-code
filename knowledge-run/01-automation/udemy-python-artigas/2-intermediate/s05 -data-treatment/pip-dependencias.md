# 📂 Seção 27 : Gerenciamento de Dependências com PIP

## 📑 Instalador de pacotes

> **Status:** 🟡 CONCLUIDO | **Data:** 04/05/2026

---

### 📺 Conteúdo em Vídeo (Udemy)

- [x] **[Vídeo 129](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109312#overview):** Instalador de pacotes — _(05min)_
- [x] **[Vídeo 130](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109320#overview):** Baixe um pacote Py — _(07min)_
- [x] **[Vídeo 131](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/29109328#overview):** Remover um pacote — _(03min)_

> **Nota rápida:** [uso muito e não sei tanto os detalhes]

---

### 📝 Anotações e Conceitos Chave

#### 1. instalando o pip

- verificar se esta instalado.
- verificar a presença na pasta de python
- instalar atraves do site sses necessario

- Exemplo de sintaxe ou regra:

```cmd
    #quickway para checar se instalado
        #CMD > pip --version

    #identificando na pasta
        #%appdata% > appdata > local > programs > python > scripts > pip

    #instalando pelo site
        #https://pypi.org/project/pip/
```

#### 2. Adicionando pacotes

- ensina o pip instal.
- como instalar uma atuualização.
- Exemplo de sintaxe ou regra:

```cmd
#usando o pip
    pip install camelcase

#instalando um upgrade
    python -m pip install --upgrade pip

```

Exemplo de uso de bibliotea instalada:

```python
    #apos instalado o camelcase (usando)

    import camelcase

    txt = "kauan horvath"

    txt_formated = camelcase.CamelCase().hump(txt)
    print(txt_formated) #return Kauan Horvath
        #semelhante a um .upper()
```

#### 3. Remover pacotes

- usando o terminnal do windows ou do vscode.
- EXPLICAÇÃO.
- Exemplo de sintaxe ou regra:

```cmd
    #exemplos
    pip uninstall camelcase

    y/n: y

    #usando o list pip para identificar os pacotes
    pip list

    package    | version
    pip        | 21.3
    setuptolls | 56.0.0
```

### x. 🛠️ Revisões

::to-review:: 06-05-2026 ::Pip install::

💻 Notas / Código

```python
# Seu código aqui
```
