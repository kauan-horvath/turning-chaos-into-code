# 🚀 Projeto: Gestão de Clientes

## 1. Modelagem da Tabela (`Tab_clientes`)

* **1.1.** Formatar máscaras e valores padrão. [✅]

* **1.2.** Expressões e refinamento dos campos. [❌]

## 2. Interface de Usuário (`Form_clientes`)

* **2.1.** Design e formatação do formulário de entrada.

## 3. Desenvolvimento de Consultas

* **3.1. Tipos de filtros implementados:**

  * **Nome:** Aproximado e específico.
  * **Data:** Entre datas, aproximada e específica.
  * **Mês:** Específica com construtor de expressões.
  * **Idade:** Range (entre idades).
  * **DDD:** Filtro aproximado.
  
* **3.2.** Criação de subconsultas (consulta de uma consulta).

## 4. Relatórios & Automação

* **4.1.** Gerar relatórios formatados.
* **4.2.** Implementação de Macros para automação de tarefas.
  
---

## 📊 Estrutura do Modelo (Tabela)

| Campo | Tipo de Dado / Propriedade | Completado |
| :--- | :--- | :--- |
| **Código** | Numeração Automática (Chave Primária) | ✅ |
| **Data** | Data/Hora | ✅ |
| **Nome** | Texto Curto | ✅ |
| **Nascimento** | Data/Hora (Com máscara de entrada) | ✅ |
| **Idade** | Calculado (Baseado na data de nascimento) | |
| **Telefone** | Texto (Com máscara de número) | |
| **Sexo** | Caixa de Combinação (Opções) | |

---

## 💡 Sintaxes Úteis (Cheat Sheet)

### Filtros e Critérios

* **Aproximado:** `Como "*" & [Digite o valor] & "*"`
* **Exato:** `Como [Digite o valor exato]`
* **Entre:** `Entre [Início] E [Fim]`

### Cálculo de Idade

Para obter a idade exata considerando anos bissextos:

```sql
Idade = (Data() - [DataNascimento]) / 365,25
```

  [✅] **[Construtor de Expressões](https://support.microsoft.com/pt-br/topic/usar-o-construtor-de-express%C3%B5es-56214db9-8b54-44f3-bc19-2a55427b5d4c):** [Link Suporte - Construtor de Expressões]

1. [LAST-DATE: 2026-04-08] installed Office
2. [LAST-DATE: 2026-04-10] started Project

#>> enfrentei uma boa dificuldade por demorar muitos dias depois de assistir as aulas, vou finalizar o projeto do curso básico, e só depois finalizar o curso avançadoos.system('cls' if os.name == 'nt' else 'clear') 

````python
    - Problema na configuração e ajuste fino de máscaras
      - Telefone não permite inserção de número
      - FIX: Durante manipulações apague a máscara correta

    - Problema na configuração de Valor padrão
      - Data com expressão =agora(), mostrando data por extenso
      - Mexer na máscara de dados curta não resolveu
      - FIX: Mexer em "formato" dentro das propriedades

    - Pesquisar atalhos de navegação rápida:
      - Alternar em modos de exibição:
        - Design: F11 > Shift + F10 > D
        - Abrir (Dados): F11 > Shift + F10 > A
      - Abrir folha de propriedades: F4
      - Salvar antes de alternar: Ctrl + B

    - Adicionar a fórmula do campo idade
        - Falhei em lembrar de cabeça
        - Coloquei no campo valor padrão mas não acho que seja lá
        - Falhei em chamar o meu próprio campo mesmo usando nome identico e []

````
::to-review:: 13-04-2026 ::Project: Bug fix and further implements::