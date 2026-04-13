# 📑 Fundamentos e Notas de Estudo: Microsoft Access

**Instrutor:** Ricardo Ortega
**Contato:** (11) 98027-3769
**Projeto Prático:** Sistema de Fluxo de Caixa (Receita vs. Despesa)

---

## 1. Tabelas: Criação e Estruturação

As tabelas são os "containers" base de qualquer banco de dados relacional. Ao criar uma tabela, definimos os campos, tipos de dados e comentários (documentação interna sobre a finalidade de cada campo).

**Caminho para criar:** `Guia Criar` > `Grupo Tabelas` > `Design da Tabela`

### Definindo Campos e Tipos de Dados

| Tipo de Dado             | Uso Recomendado               | Configuração Especial                                                  |
| :----------------------- | :---------------------------- | :--------------------------------------------------------------------- |
| **Texto Curto**          | Nomes, Sobrenomes, Categorias | Limitar o `Tamanho do Campo` (ex: 50 caracteres) para otimizar espaço. |
| **Número**               | Quantidades, Idades           | Ajustar o `Tamanho do Campo` (ex: Inteiro Longo, Duplo).               |
| **Moeda**                | Valores financeiros           | Formato monetário automático; previne erros de arredondamento.         |
| **Data/Hora**            | Datas de registro, nascimento | Usar máscaras de entrada (ex: `00/00/0000;0;_`).                       |
| **Numeração Automática** | Chaves Primárias (IDs)        | Incremento automático, ideal para garantir unicidade sem intervenção.  |

- **Chave Primária:** Identificador único obrigatório para evitar duplicidade de registros.
- **Valor Padrão:** Valor inserido automaticamente (ex: `=Agora()` para registrar a data/hora atual da criação do registro).

---

## 2. A Folha de Propriedades e Boas Práticas (Design)

A Folha de Propriedades (`F4`) é onde você aplica validações na raiz do banco e ajusta o comportamento das interfaces.

**Caminho para acessar:** `Aba Design` > `Grupo Mostrar/Ocultar` > `Folha de Propriedades`

### Propriedades de Dados (Tabelas)

- **Máscara de Entrada:** Formatação prévia que facilita a inserção (ex: CPF, CEP). _Dica: Salve antes de manipular._ Ex: `\(00\) 00000\-0000;0;_`
- **Regra de Validação:** Impede dados que violem regras lógicas (ex: `>=18`).
- **Texto de Validação:** Mensagem de erro amigável exibida ao usuário.
- **Requerido:** Se marcado como **Sim**, impede campos vazios (comportamento NOT NULL).

### Boas Práticas de Organização e Interface

- **Nomenclatura:** Use prefixos (`tbl_`, `qry_`, `frm_`, `rpt_`) para identificar objetos rapidamente no painel.
- **Formato de Formulários:** Ajustes como Pop-up, remoção de barras de rolagem, parada de tabulação e ocultação de seletores de registro deixam o sistema com cara de software.
- **Produtividade no Modo Design:**
  - Utilize as ferramentas de alinhamento e distribuição equidistante.
  - Atalho útil: `Shift` + `Setas` redimensiona o tamanho do campo/botão selecionado.
  - Entenda a hierarquia visual: **Cabeçalho** (fica fixo no topo) vs. **Detalhe** (repete para cada registro exibido).

---

## 3. Relacionamentos e Integridade Referencial

Para que o banco seja relacional, as tabelas não devem existir isoladas. Elas se conectam através de Chaves Primárias e Chaves Estrangeiras.

**Caminho para configurar:** `Guia Ferramentas de Banco de Dados` > `Grupo Relações` > `Relações`

### Passos para um Relacionamento Seguro:

1. Adicione as tabelas desejadas via `Adicionar Tabelas`.
2. Arraste a **Chave Primária** da tabela de origem (lado "1") para a **Chave Estrangeira** da tabela relacionada (lado "Muitos").
3. Na janela _Editar Relações_, marque obrigatoriamente:
   - `[X] Impor Integridade Referencial` (Impede a criação de registros órfãos).
   - _(Opcional)_ `Propagar Atualização/Exclusão` para manter a consistência em cascata.

---

## 4. Consultas (Queries)

Processamento de dados a partir de tabelas ou outras consultas para gerar visualizações filtradas. São os motores que alimentam formulários e relatórios.

**Caminho para criar:** `Guia Criar` > `Grupo Consultas` > `Design da Consulta`

### Sintaxe e Critérios de Filtro

A linha **Critério** funciona como a cláusula `WHERE` do SQL. É possível usar caracteres curinga (`*`) e concatenação (`&`).

- **Texto Exato:** `"Ativo"`
- **Aproximado:** `Como "*" & [Digite o valor] & "*"`
- **Intervalo (Datas/Números):** `Entre #01/01/2026# E #31/12/2026#`
- **Múltiplas condições:** Uso lógico de `E` / `Ou` nas linhas de critério.

---

## 5. Formulários e Relatórios

### 📝 Formulários (Interfaces de Entrada)

Interfaces amigáveis para preenchimento, navegação e manipulação de dados.

- **Tabulação:** Organize a ordem lógica de preenchimento ao usar a tecla `TAB`.
- **Expressões:** Use o **Construtor de Expressões** na aba _Dados_ para realizar cálculos em tempo real na tela.
- **Controles:** Adicione botões de ação (Salvar, Deletar, Novo) para facilitar a usabilidade.

### 📈 Relatórios (Saída e Impressão)

Documentos estáticos projetados para apresentação, análise e impressão.

- **Finalidade:** Demonstração de métricas de desempenho e resumos.
- **Agrupamento:** Permite organizar os dados visualmente por categorias (ex: separar despesas por mês) e definir ordem crescente/decrescente.

---

## 6. Macros (Automação Low-Code)

Ferramenta nativa de automação para executar ações sequenciais sem precisar escrever código.

- **Aplicação:** Programação de eventos em botões (ex: "Ao Clicar") ou validações complexas em campos específicos, substituindo a necessidade de usar VBA em operações rotineiras.

---

## 7. Integração e Versionamento (Git x Access)

Como o projeto faz parte do repositório `turning-chaos-into-code`, e arquivos `.accdb` são binários proprietários, os seguintes cuidados são essenciais:

- **Compactação Frequente:** O Access "incha" o arquivo com lixo de memória. Reduza o tamanho antes de fazer o commit.
  - **Caminho:** `Guia Arquivo` > `Informações` > `Compactar e Reparar Banco de Dados`
- **Atenção ao Lock:** Nunca faça um `git commit` com o Access aberto. Feche o programa para que o arquivo temporário de bloqueio (`.laccdb`) desapareça.
- **Configuração do `.gitignore`:** Mantenha a regra abaixo no repositório:

  ```gitignore
  # Ignorar arquivos de bloqueio de registro temporário do Access
  *.laccdb
  ```

---

## 🚀 Status e Logs do Projeto

Acompanhe os avanços práticos através do arquivo:
`care-projects/access-table-development/creating-a-database.md`

- `::last-review:: 2026-04-08` :: Only formatted the mkd.
  ::to-review:: 2026-04-15` :: Revise Access information
