# 📂 Seção 25 : Serialização de Dados: Trabalhando com JSON

## 📑 WOW

> **Status:** 🟡 ANDAMENTO | **Data:** 08/05/2026

### 📺 Conteúdo em Vídeo (Udemy)

- [✅] **[Vídeo 01](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28959546#overview):** Analisar Json — _(Duração)_
- [ ] **[Vídeo 02](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28959550#overview):** Converter Json — _(Duração)_
- [ ] **[Vídeo 03](https://www.udemy.com/course/python-completo-e-profissional/learn/lecture/28959554#overview):** Formatar Json — _(Duração)_

> **Nota rápida:** [Estou muito animado para entender a importancia dessa integração]

---

### 📝 Anotações e Conceitos Chave

#### 1. Modulo Json em python

- informa que é uma ótima informa de tratar dados.
- informa sobre o metodo loads para retornar em dict.
- Exemplo de sintaxe ou regra:

```python
    #exemplo
    import json

    #abrir um string json
        #semelhante a um dict
    string_json = "{"Chave":"Valor","Nome":"Kauan"}"

    dictPy_exStringJson = json.loads(string_json)
    print(type(dictPy_exStringJson)) #return class = "dict"
    print(dictPy_exStringJson) #return em key/value {"Chave":"Valor","Nome":"Kauan"}
```

#### 2. Converter de Python para Json

- informa sobre o processo inverso.
  - metodo dumps()
- informa que a conversão pode ocorrer a partir de alguns tipos não necessáriamente dict.
- Exemplo de sintaxe ou regra:

```python
    #exemplo
    import json

    py_dict = {
        "Name":"Kauan",
        "Age":"30"
    }

    strJson_exDictPy = json.dumps(py_dict)
    print(type(strJson_exDictPy)) #return class = "str"
    print(strJson_exDictPy) #return em strValue "{"Chave":"Valor","Nome":"Kauan"}"

    #⚠  conversaão transforma os caracters de escape automaticamente

    other_types = ["Dicts", "Lists", "Tuple", "Str", "Int", "Float","Bool", "None"]

    json_dumps = json.dumps(other_types)
        #os retornos vêm em padrão JavaScript
    #⚠ O Retono de None é Null (equivalentes)
    #⚠ O retorno de Bool em java é lower_case (true/false)
```

#### 3. Formatar o Json

- informa os outros parametros de dumps().
  - informa sobre o método indent()
  - inform sobre o separators()
  - informa sobre o sort_keys()
- Exemplo de sintaxe ou regra:

```python
    #exemplos
    import json

    py_data = {
        "str": "Kauan"
        "int": 30
        "bool": True
        "false": False
        "tuple": ("Clara", "Gema", "ain")
        "null": None
        "nested_list_with_dicts": [
            {
                "mas ce filma e fala?": True,
                "ce é o bixão memo heim" : True
                }
        ]
    }

    #dumps to json
    str_json = json.dumps(py_data)
    print(str_json) #ful text "bla bla bla bla"

    #formatando a saída
    indent_json = json.dumps(py_data, indent = 4)
    print(indent_json)
        #retorna com espaços facilitando a leitura

    #alterando os separadores
    separators_json = json.dumps(py_data, indent = 4, separators = (". ", "  :: "))
    print(separators_json)
        #retorna ponto no lugar da vírgula
        # e doublos points no lugar de dois pontos

    #alterando a ordenação das chaves
    alfabetic_json = json.dumps(py_data, indent = 4, separators = (". ", "  :: "), sort_keys = True)
    print(alfabetic_json)
        #ordena as chaves alfabeticamente

    #⚠ Os parametros de dumpssão opicionais, podendo ser removidos e adicionados à necessidade
```

### x. 🛠️ Revisões

::to-review:: 08-05-2026 ::REVISAO-PADRAO::

💻 Notas / Código

```python
# Seu código aqui
```
