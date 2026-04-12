# Aula de YAML e Automação com Python - Parte 3: Avançado

## 1. Âncoras (`&`) e Aliases (`*`)

O YAML permite que você defina um bloco de dados uma única vez e o reutilize em outros lugares. Isso evita repetição (princípio DRY - *Don't Repeat Yourself*).

* **`&` (Anchor):** Marca um bloco de dados com um nome.
* **`*` (Alias):** Referencia o bloco marcado anteriormente.
* **`<<:` (Merge Key):** Permite "copiar" o conteúdo de uma âncora e adicionar ou sobrescrever campos específicos.

**Exemplo de `setup.yml`:**

```yaml
# Definição padrão de um servidor
padrao_server: &config_base
  cpu: 2
  memoria: 4GB
  os: "Ubuntu 22.04"

servidor_web:
  <<: *config_base
  porta: 80

servidor_db:
  <<: *config_base
  memoria: 16GB  # Sobrescrevendo a memória padrão
```

## 2. Tratando Variáveis de Ambiente no YAML

Na automação real, nunca deixamos senhas ou tokens expostos no arquivo. Usamos "placeholders" que o Python substitui em tempo de execução.

**Exemplo de integração Python + Env:**

```python
import yaml
import os

# Simulando uma variável de ambiente (geralmente vinda do SO)
os.environ['DB_PASSWORD'] = 'minha_senha_secreta'

def carregar_config_com_env(path):
    with open(path, 'r') as f:
        # Carrega o conteúdo como string primeiro
        conteudo = f.read()
        
    # Substitui marcadores no formato ${VAR}
    # (Em projetos reais, costuma-se usar bibliotecas como 'python-dotenv')
    for key, value in os.environ.items():
        conteudo = conteudo.replace(f'${{{key}}}', value)
        
    return yaml.safe_load(conteudo)

# Exemplo de uso
# Se no YAML houver: senha: ${DB_PASSWORD}
# O Python carregará o valor real da variável de ambiente.
```

## 3. Criando Custom Tags (`!tag`)

Você pode ensinar o `PyYAML` a reconhecer tipos de dados personalizados. Isso é muito usado em frameworks como o **Ansible** ou **Home Assistant**.

> **Exemplo: Construtor customizado**

```python
import yaml

def join_constructor(loader, node):
    seq = loader.construct_sequence(node)
    return ''.join([str(i) for i in seq])

# Registrando a tag !unir
yaml.add_constructor('!unir', join_constructor)

documento = """
caminho: !unir [/home/, usuario, /scripts]
"""
dados = yaml.load(documento, Loader=yaml.FullLoader)
print(dados['caminho'])  # Saída: /home/usuario/scripts
```

## 4. Boas Práticas Avançadas

* **Validação de Esquema:** Utilize bibliotecas como `Cerberus` ou `Pydantic` para validar se o YAML que o usuário enviou contém todos os campos obrigatórios e tipos corretos.
* **Ordenação:** Se a ordem das chaves for importante para você ao salvar o arquivo, utilize `sort_keys=False` no `yaml.dump()`.

---
