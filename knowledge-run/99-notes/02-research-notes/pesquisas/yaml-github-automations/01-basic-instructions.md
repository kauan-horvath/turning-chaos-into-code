# Aula de YAML e Automação com Python - Parte 1: O Básico

## 1. O que é YAML?

YAML (YAML Ain't Markup Language) é um formato de serialização de dados legível por humanos. É amplamente utilizado para arquivos de configuração devido à sua sintaxe limpa, que utiliza espaços e quebras de linha em vez de parênteses ou chaves complexas.

## 2. Estrutura e Sintaxe

Diferente do JSON, o YAML depende da **indentação** para definir a hierarquia.

- **Chave e Valor:** Definidos por `:`. Note o espaço obrigatório após os dois pontos.
- **Tipos de Dados:** Suporta strings (sem necessidade de aspas, a menos que contenham caracteres especiais), números e booleanos (`true`/`false`).
- **Listas:** Definidas por um hífen `-`.

**Exemplo de arquivo `config.yml`:**

```yaml
usuario: "Horvath"
versao: 1.0
ativo: true
pastas:
  - scripts
  - logs
  - credentials
```

## 3. Automação com Python (Leitura)

Para manipular arquivos YAML no Python, utilizamos a biblioteca `PyYAML`.

**Instalação:**

```bash
pip install pyyaml
```

**Código para leitura básica:**

```python
import yaml

# Abrindo e carregando o arquivo
with open('config.yml', 'r') as file:
    dados = yaml.safe_load(file)

# Acessando as informações como um dicionário Python
print(f"Usuário: {dados['usuario']}")
print(f"Primeira pasta: {dados['pastas'][0]}")
```

## 4. Boas Práticas

- Sempre use **espaços** para indentação, nunca o caractere TAB, pois isso quebra o interpretador YAML.

- Utilize o `yaml.safe_load()` em vez de `yaml.load()` para evitar a execução de código arbitrário e garantir a segurança do seu script.

---
