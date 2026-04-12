# 📑 Notas de Estudo: Microsoft Access

**Instrutor:** Ricardo Ortega
**Contato:** (11) 98027-3769
**Projeto Prático:** Sistema de Fluxo de Caixa (Receita vs. Despesa)

---

## 🏗️ Aula 01 - Objetos do Access

### 📊 Tabelas

São os "containers" de dados onde armazenamos os registros. Ao criar uma tabela, definimos:

- **Nome do Campo:** Identificação da coluna.
- **Tipo de Dados:** \* **Chave Primária:** Identificador único para evitar duplicidade.
- **Máscara de Entrada:** Formatação prévia (ex: CPF, CEP) para facilitar a inserção. _Dica: Salve antes de manipular._
- **Valor Padrão:** Valor automático (ex: `=Agora()` para data/hora atual).
- **Comentários:** Documentação interna sobre a finalidade de cada campo.

### 🔍 Consultas

Processamento de dados a partir de tabelas ou outras consultas para gerar visualizações filtradas.

- **Sintaxe de Filtro:** Uso de operadores como `Como`, `E`, `Entre`, além de caracteres curinga (`*`) e concatenação (`&`).

### 📝 Formulários

Interfaces amigáveis para preenchimento e navegação de dados.

- **Tabulação:** Ordem lógica de preenchimento ao usar a tecla TAB.
- **Expressões:** Uso do **Construtor de Expressões** na guia de dados para cálculos em tempo real.
- **Controles:** Botões de ação (Deletar, Copiar, Colar) e seletores de registro.

### 📈 Relatórios

Documentos estáticos para apresentação e impressão de resultados.

- **Agrupamento:** Organização de dados por categorias e ordem crescente/decrescente.
- **Finalidade:** Demonstração de valores úteis e métricas de desempenho.

### 🤖 Macros (Low-Code)

Ferramenta de automação para executar ações sequenciais.

- **Aplicação:** Programação de botões e eventos em campos específicos sem necessidade de VBA complexo.

---

## 🛠️ Boas Práticas & Design

### Organização

- **Nomenclatura:** Use prefixos (ex: `tbl_`, `qry_`, `frm_`, `rpt_`) para identificar objetos em projetos grandes.

### Folha de Propriedades

- **Formato:** Ajustes de interface como Pop-up, barras de rolagem, parada de tabulação e seletores.
- **Dados:** Utilizar o construtor de expressões para gerar dados derivados.

### Modo Design (Dicas de Produtividade)

- **Alinhamento:** Utilizar ferramentas de distribuição equidistante para um layout limpo.
- **Atalhos:**
  - `Shift` + `Setas`: Redimensiona o tamanho do campo selecionado.
- **Estrutura:** Atenção à diferença entre **Cabeçalho** (fixo) e **Detalhe** (repete para cada registro).

---

### 🚀 Project Development

See the advancements through:
`care-projects/access-table-development/creating-a-database.md`

::last-review:: 08-04-2026 ::Only formated the mkd.::

::to-review:: 15-04-2026 ::Access Basic Model.::
