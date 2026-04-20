# 🚀 Projeto: Gestão de Clientes

## 1. Modelagem da Tabela (`tbl_clientes`)

- [x] **1.1.** Formatar máscaras e valores padrão.
- [x] **1.2.** Expressões e refinamento dos campos.

## 2. Interface de Usuário (`frm_clientes`)

- [x] **2.1.** Design e formatação do formulário de entrada.

## 3. Desenvolvimento de Consultas

- [x] **3.1. Tipos de filtros implementados:**
  - **Nome:** Aproximado e específico.
  - **Data:** Entre datas, aproximada e específica.
  - **Mês:** Específica com construtor de expressões.
  - **Idade:** Range (entre idades).
  - **DDD:** Filtro aproximado.

---

## 📊 Estrutura do Modelo (Tabela)

| Campo          | Tipo de Dado / Propriedade                | Status |
| :------------- | :---------------------------------------- | :----- |
| **Código**     | Numeração Automática (Chave Primária)     | ✅     |
| **Data**       | Data/Hora                                 | ✅     |
| **Nome**       | Texto Curto                               | ✅     |
| **Nascimento** | Data/Hora (Com máscara de entrada)        | ✅     |
| **Idade**      | Calculado (Baseado na data de nascimento) | ✅     |
| **Telefone**   | Texto (Com máscara de número)             | ✅     |
| **Sexo**       | Caixa de Combinação (Opções)              | ✅     |

---

## 💡 Sintaxes Úteis (Cheat Sheet)

### Filtros e Critérios

- **Aproximado:** `Como "*" & [Digite o valor] & "*"`
- **Exato:** `Como [Digite o valor exato]`
- **Entre:** `Entre [Início] E [Fim]`

### Cálculo de Idade

Para obter a idade exata considerando anos bissextos (forçando o número inteiro para evitar arredondamento antes do aniversário):

```sql
Idade = Int((Data() - [DataNascimento]) / 365,25)
```

- [x] **[Construtor de Expressões](https://support.microsoft.com/pt-br/topic/usar-o-construtor-de-express%C3%B5es-56214db9-8b54-44f3-bc19-2a55427b5d4c):** Link de Suporte

---

## 🛠️ Troubleshooting (Problemas e Soluções)

### ⚠️ Problemas

- **Configuração e ajuste fino de máscaras:**
  - _Comportamento:_ Telefone não permite inserção de número.
  - _FIX:_ Durante manipulações, apague a máscara, insira o dado e recrie a máscara correta.
- **Configuração de Valor Padrão:**
  - _Comportamento:_ Data com expressão `=Agora()` mostrando data por extenso. Mexer na máscara de dados curta não resolveu.
  - _FIX:_ Mexer na propriedade "Formato" dentro da Folha de Propriedades, e não na máscara.
- **Fórmula do campo Idade:**
  - _Comportamento:_ Falhei em lembrar de cabeça. Coloquei no campo "Valor Padrão" (local incorreto). Falhei em chamar o próprio campo mesmo usando nome idêntico e `[]`.
  - _FIX:_ Implementado no campo correto (tipo Calculado) com a formatação exata após revisar a aula.
- **Atalhos e Navegação:**
  - _Nota:_ É impossível trabalhar com agilidade no Access sem o mouse (mouse configurado).
  - _Alternar modos de exibição:_
    - Design: `F11` > `Shift + F10` > `D`
    - Abrir (Dados): `F11` > `Shift + F10` > `A`
  - _Abrir Folha de Propriedades:_ `F4`
  - _Salvar antes de alternar:_ `Ctrl + B` (ou `Ctrl + S`).

### ✅ Soluções Aplicadas

- **Tabelas:**
  - Implementação do Sexo: `Pesquisa` > `Caixa de Combinação` > `Origem da linha: "Masculino";"Feminino"`.
- **Formulários:**
  - Mudar para formato PopUp (`Folha de Propriedades` > `Outro`).
  - Remover seletor de registro (`Folha de Propriedades` > `Formato`).
  - Remover parada de tabulação (`Folha de Propriedades` > `Outro`).
  - _Dica:_ Mudar o tamanho dos botões de forma padronizada.
- **Relatórios:**
  - Criados utilizando o Assistente.
  - Agrupamentos definidos para separar (Sexo).
  - Ordenação: Crescente por Nome.
  - Fórmula replicada no campo Idade.
- **Consultas:**
  - Origem: Podem ser criadas a partir de Tabelas ou outras Consultas (usado o assistente).
  - Campo Critérios:
    - `Entre [] E []` > Cria um filtro entre valores.
    - `Como []` > Retorna a partir do valor exato.
    - `Como "*" & [] & "*"` > Retorna a partir do valor parcial.
  - Excepcional (Cálculo em Consulta):
    - `Expr1: Mes([Nascimento])`

---

## 📅 Log de Atividades e Revisão

- `::last-review:: 2026-04-08` :: Installed Office
- `::last-review:: 2026-04-10` :: Started Project
- `::last-review:: 2026-04-13` :: Finalizado e commitado

> Enfrentei uma boa dificuldade por demorar muitos dias depois de assistir às aulas. Finalizei este módulo e vou revisar para manter o fundamento fresco.

::Last-review:: 20-04-2026 :: Refazer as tabelas para fixação ::
::to-review:: 20-05-2026 ::Criar um projeto a partir de uma tabela::
