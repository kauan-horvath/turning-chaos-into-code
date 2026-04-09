# 🚀 Projeto: Gestão de Clientes

### 1. Modelagem da Tabela (`Tab_clientes`)
* **1.1.** Criação de máscaras e valores padrão. [✅]
    - adicionado mascara de telefone em tab_clientes
    - valor padrão em sexo como "sexo"
* **1.2.** Formatação e refinamento dos campos.

### 2. Interface de Usuário (`Form_clientes`)
* **2.1.** Design e formatação do formulário de entrada.

### 3. Desenvolvimento de Consultas
* **3.1. Tipos de filtros implementados:**
    * **Nome:** Aproximado e específico.
    * **Data:** Entre datas, aproximada e específica.
    * **Mês:** Específica com construtor de expressões.
    * **Idade:** Range (entre idades).
    * **DDD:** Filtro aproximado.
* **3.2.** Criação de subconsultas (consulta de uma consulta).

### 4. Relatórios & Automação
* **4.1.** Gerar relatórios formatados.
* **4.2.** Implementação de Macros para automação de tarefas.

---

## 📊 Estrutura do Modelo (Tabela)

| Campo | Tipo de Dado / Propriedade |
| :--- | :--- |
| **Código** | Numeração Automática (Chave Primária) |
| **Data** | Data/Hora |
| **Nome** | Texto Curto |
| **Nascimento** | Data/Hora (Com máscara de entrada) |
| **Idade** | Calculado (Baseado na data de nascimento) |
| **Telefone** | Texto (Com máscara de número) |
| **Sexo** | Caixa de Combinação (Opções) |

---

## 💡 Sintaxes Úteis (Cheat Sheet)

### Filtros e Critérios
* **Aproximado:** `Como "*" & [Digite o valor] & "*"`
* **Exato:** `Como [Digite o valor exato]`
* **Entre:** `Entre [Início] E [Fim]`

### Cálculo de Idade
Para obter a idade exata considerando anos bissextos:
```sql
Idade = (Data() - [DataNascimento]) / 365.25
```


[!construtor de expresões](Link do Suporte de Construtor de Expressões):(https://support.microsoft.com/pt-br/topic/usar-o-construtor-de-express%C3%B5es-56214db9-8b54-44f3-bc19-2a55427b5d4c)

TODO: [REVIEW-DATE: 2026-04-08] installed Office
# TODO: [REVIEW-DATE: 2026-04-10] Start Access Project