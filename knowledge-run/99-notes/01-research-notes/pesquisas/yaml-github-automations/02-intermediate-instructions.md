# Aula de YAML e Automação com Python - Parte 2: Intermediário

No nível intermediário, o foco é a **bidirecionalidade** e a **segurança**. Você aprenderá a modificar arquivos programaticamente e a proteger dados sensíveis.

## 1. Escrevendo YAML com Python

Muitas vezes, sua automação precisará atualizar um arquivo de configuração (como adicionar uma nova data de revisão no seu `revisions.yml`).

Para isso, usamos o `yaml.dump()`.

```python
import yaml

novo_projeto = {
    'projeto': 'Access Modulo 2',
    'revisar_em': '2026-04-15',
    'status': 'pendente'
}

# Lendo o arquivo existente
with open('revisions.yml', 'r') as f:
    dados = yaml.safe_load(f) or []

# Adicionando o novo item à lista
dados.append(novo_projeto)

# Salvando de volta (dump)
with open('revisions.yml', 'w') as f:
    yaml.dump(dados, f, sort_keys=False, default_flow_style=False)
```

> **Nota:** `sort_keys=False` mantém a ordem que você definiu, e `default_flow_style=False` garante que o arquivo fique bonito e legível (em blocos), em vez de uma linha única.

---

## 2. O Uso de Variáveis de Ambiente (Environment Variables)

Em automações profissionais (como a que acabamos de fazer no GitHub Actions), o arquivo YAML serve como uma ponte para passar segredos (Secrets).

No YAML do GitHub Actions, você define a variável:

```yaml
env:
  MINHA_CHAVE: ${{ secrets.CHAVE_SEC_RET }}
```

E no Python, você a captura de forma segura:

```python
import os

# O Python "escuta" o que o YAML injetou no sistema
chave = os.environ.get('MINHA_CHAVE')

if chave:
    print("Conexão segura estabelecida.")
```

## 3. Tratamento de Dados "Seguro" (Dicionários)

Arquivos YAML podem vir incompletos. Se você tentar acessar uma chave que não existe (`dados['detalhes']`), seu código vai quebrar com um `KeyError`.

**A técnica intermediária é usar o `.get()`:**

```python
# Se 'detalhes' não existir, ele retorna 'Sem descrição' em vez de quebrar
descricao = t.get('detalhes', 'Sem descrição')
```

---

## 4. Âncoras e Aliases (Otimização de YAML)

Se você tem dados repetidos no YAML, pode usar âncoras (`&`) e aliases (`*`) para evitar redundância. Isso é muito usado em configurações complexas de Docker ou CI/CD.

```yaml
config_padrao: &base
  idioma: pt-br
  timezone: America/Sao_Paulo

projeto_1:
  <<: *base
  nome: "Access"

projeto_2:
  <<: *base
  nome: "Python"
```

*O `<<: *base` diz ao YAML: "copie tudo o que está em 'base' para cá".\*

---

## Resumo da Parte 2

- **Python -> YAML:** Aprendemos a salvar dados.
- **YAML -> Sistema:** Aprendemos sobre `os.environ`.
- **Robustez:** Uso de `.get()` para evitar falhas em dados ausentes.
