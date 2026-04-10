# 1. O Propósito Principal

O objetivo de um `spec.md` é eliminar a ambiguidade. Em vez de começar a programar imediatamente (o que pode gerar retrabalho), o desenvolvedor ou o arquiteto de software define o plano de ação em Markdown.

## Benefícios

* **Alinhamento:** Garante que todos os envolvidos (desenvolvedores, designers e clientes) entendam o que será construído.
* **Documentação Viva:** Como está no formato `.md`, ele vive dentro do repositório de código (Git), sendo versionado junto com o software.
* **Eficiência para IAs:** Atualmente, o `spec.md` é a ferramenta favorita para quem usa IAs como **Cursor, Windsurf ou Devin**. A IA lê o arquivo e segue as instruções à risca, evitando alucinações.

---

## 2. Estrutura Comum de um spec.md

Um bom arquivo de especificação geralmente segue esta estrutura:

### A. Visão Geral (Overview)

Um resumo de alto nível sobre o que é o projeto e qual problema ele resolve.

### B. Funcionalidades (Features)

Lista detalhada do que o software deve fazer.

* *Exemplo:* "O sistema deve permitir login via Google."
* *Exemplo:* "O usuário deve conseguir exportar relatórios em PDF."

### C. Requisitos Técnicos (Tech Stack)

Define quais tecnologias serão usadas.

* Linguagem: TypeScript
* Framework: Next.js
* Banco de Dados: PostgreSQL

### D. Regras de Negócio

Lógica específica que o código deve respeitar.

* *Exemplo:* "Um usuário só pode deletar um comentário se ele for o autor ou for um administrador."

### E. Critérios de Aceitação

Uma lista de verificação (checklist) para determinar se a tarefa foi concluída com sucesso.

---

## 3. Exemplo Prático de um spec.md

Abaixo, um exemplo de como seria o conteúdo de um arquivo para um sistema de "Lista de Tarefas":

```markdown
# Spec: Sistema de To-Do List

## Visão Geral
Um aplicativo web simples para gerenciar tarefas diárias, focado em produtividade pessoal.

## Funcionalidades
- [ ] Criar tarefas com título e descrição.
- [ ] Marcar tarefas como concluídas.
- [ ] Filtrar tarefas por (Todas / Pendentes / Concluídas).
- [ ] Persistência de dados no navegador (LocalStorage).

## Requisitos Técnicos
- Frontend: React com Tailwind CSS.
- Gerenciamento de Estado: Context API.

## Regras de Negócio
- O título da tarefa não pode estar vazio.
- O limite máximo de caracteres no título é 50.

## Design
- Cores: Fundo escuro (#121212), Texto branco, Destaque em roxo.
- Layout: Lista centralizada em uma coluna.
