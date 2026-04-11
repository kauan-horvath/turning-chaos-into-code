
# 🛠️ Os Tipos Mais Comuns

| Prefixo | Quando usar? | Exemplo |
| :--- | :--- | :--- |
| **`feat:`** | Uma **nova funcionalidade** (Feature). | `feat: add navigation table to modules` |
| **`fix:`** | Correção de um **bug** ou erro. | `fix: repair broken relative link in Home` |
| **`docs:`** | Mudanças apenas na **documentação** (README, .md). | `docs: add study notes about variables` |
| **`style:`** | Mudanças de **formatação** (espaços, vírgulas) que não afetam o código. | `style: fix indentation in main.py` |
| **`refactor:`** | Mudança no código que nem corrige bug nem adiciona feature. | `refactor: simplify variable assignment logic` |
| **`chore:`** | Tarefas de "limpeza" ou ferramentas (atualizar .gitignore, etc). | `chore: update folder structure` |

---

## 📝 A Regra de Ouro (Estrutura)

A estrutura ideal é:
`<tipo>: <descrição curta em letras minúsculas>`

1. **Use o imperativo:** Em inglês, escreva como se estivesse dando uma ordem ao código (Ex: `add` em vez de `added`, `fix` em vez de `fixed`).
2. **Seja direto:** O commit deve responder à pergunta: *"Se eu aplicar este commit, o que ele fará no projeto?"*.
    * *Resposta:* "Adicionará (add) navegação rápida".

## 💡 Por que usar isso agora?

Como você está organizando sua **Wiki de estudos**, usar `docs:` para seus arquivos Markdown e `feat:` quando criar um script Python novo vai deixar seu GitHub com uma cara de **perfil profissional**. Recrutadores amam ver um repositório que segue o padrão *Conventional Commits*.

