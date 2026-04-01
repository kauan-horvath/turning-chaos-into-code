### 🛡️ Lint Showcase: Automação de Qualidade (CI)
Implementei um fluxo de **Integração Contínua (CI)** utilizando **GitHub Actions** para garantir a integridade do código Python.

* **O que faz:** Toda vez que um novo código é enviado (`push`), um robô (ambiente Ubuntu) é acionado para verificar erros de sintaxe e padrões de escrita.
* **Ferramenta:** `Flake8` (Linter).
* **Objetivo:** Manter o repositório livre de erros básicos e garantir que o projeto siga boas práticas de desenvolvimento moderno, sem esforço manual.

---

**Dica rápida:** Se quiser deixar o seu `README.md` com cara de projeto profissional de verdade, você pode adicionar este "badge" (selo) no topo do arquivo. Ele atualiza sozinho para **"passing"** (verde) sempre que o teste passar:

```markdown
![Lint Status](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO/actions/workflows/lint.yml/badge.svg)
```