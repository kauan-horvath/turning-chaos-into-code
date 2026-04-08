# Aula de YAML e Automação com Python - Parte 2: Intermediário

### 1. Estruturas Complexas em YAML
No nível intermediário, começamos a lidar com objetos aninhados e múltiplos documentos no mesmo arquivo.

* **Dicionários Aninhados:** Úteis para agrupar configurações relacionadas.
* **Múltiplos Documentos:** Separados por `---`. Isso permite colocar várias configurações diferentes em um único arquivo `.yml`.

**Exemplo de `avancado.yml`:**
```yaml
banco_de-dados:
  host: "localhost"
  porta: 5432
  credenciais:
    user: "admin"
    pass: "12345"
---
servidor_web:
  porta: 8080
  debug: false
```

### 2. Manipulando Blocos de Texto
O YAML possui formas especiais de lidar com strings multilinhas (como scripts ou descrições):
* `|` (Literal): Mantém as quebras de linha exatamente como estão.
* `>` (Folded): Substitui as quebras de linha por espaços (gera um parágrafo único).

### 3. Automação com Python (Escrita e Múltiplos Documentos)
Além de ler, a automação exige que seu script Python consiga **gerar** ou **atualizar** arquivos de configuração.

**Código para escrita e leitura de múltiplos documentos:**
```python
import yaml

# Dados para salvar
config_data = {
    'projeto': 'Automacao_X',
    'ambiente': 'producao',
    'modulos': ['auth', 'api', 'db']
}

# 1. Escrevendo (Dump) em um arquivo
with open('new_config.yml', 'w') as file:
    yaml.dump(config_data, file, default_flow_style=False)

# 2. Lendo múltiplos documentos de um arquivo
with open('multiplo.yml', 'r') as file:
    # safe_load_all retorna um gerador
    documentos = yaml.safe_load_all(file)
    for doc in documentos:
        print(f"Documento encontrado: {doc}")
```

### 4. O Parâmetro `default_flow_style`
Ao usar `yaml.dump()`, se você definir `default_flow_style=False`, o Python gerará um YAML "limpo" (com quebras de linha). Se for `True`, ele gerará algo parecido com JSON (entre chaves `{}`), o que é menos legível.

### 5. Desafio Intermediário
Tente criar um script Python que lê um dicionário de usuários e gera um arquivo YAML onde cada usuário tem sua própria lista de permissões e um status de "último login".

---