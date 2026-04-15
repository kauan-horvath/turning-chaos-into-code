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

### Passos para um Relacionamento Seguro

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

::last-review:: 2026-04-08 :: Only formatted the mkd ::
::last-review:: 15-04-2026 :: Revise Access information ::
Aproveitamento 87% - revisão distante
Pontos fortes
Estrutura de Tabelas e Tipos de Dados: Você demonstra domínio sólido sobre a criação de tabelas, uso de Chaves Primárias, comportamento do campo 'Requerido' e a importância de limitar o tamanho de campos de texto para otimização.
Interface e Atalhos: Excelente conhecimento dos atalhos de produtividade (F4, Shift+Setas) e na navegação pelos menus de design do Access.
Consultas e Lógica de Filtros: Você entende bem o uso de caracteres curinga para buscas aproximadas e a aplicação de critérios de data complexos entre períodos.
Manutenção e Boas Práticas: Mostrou clareza sobre a necessidade de compactar o banco de dados, o gerenciamento de arquivos de bloqueio (.laccdb) em ambientes de versão como Git e padronização de nomenclatura.
Áreas a melhorar
Precisão em Tipos Numéricos e Financeiros: Lembre-se que para valores monetários, o tipo 'Moeda' é superior ao 'Número (Duplo)' porque evita erros de arredondamento em cálculos matemáticos complexos.
Macros vs. Construtor de Expressões: O 'Construtor de Expressões' serve para criar fórmulas, enquanto as 'Macros' são a ferramenta correta para automatizar sequências de ações (como abrir formulários ou imprimir) sem usar código VBA.
Documentação e Validação: O 'Texto de Validação' é focado na experiência do usuário final (a mensagem que ele lê), enquanto o comentário interno geralmente fica na 'Descrição' do campo no modo design da tabela.
Lógica Booleana em Consultas: Revise os operadores lógicos: critérios na mesma linha funcionam como o operador 'E' (ambas as condições devem ser verdadeiras), enquanto critérios em linhas diferentes funcionam como 'OU'.

::to-review:: 22-04-2026 ::Refazer Questionário - Access Fundamentals ::
