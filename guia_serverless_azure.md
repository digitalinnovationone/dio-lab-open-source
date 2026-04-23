# Guia Passo a Passo: Trabalhando Aplicações Serverless na Azure (DIO)

Este guia detalhado fornece o passo a passo para a implementação do projeto Serverless na Azure, conforme o desafio do laboratório da DIO. O projeto envolve a criação de um fluxo de trabalho assíncrono utilizando **Azure Logic Apps**, **Azure Service Bus** e **Azure Functions** com integração ao **Azure SQL Database**.

## 1. Arquitetura do Projeto

O projeto Serverless consiste em dois fluxos principais:

1.  **Fluxo de Persistência (HTTP -> SQL):** Uma Azure Function (`fn-save-sql`) expõe um endpoint HTTP para receber dados e persistir um item na base de dados SQL.
2.  **Fluxo de Mensageria (Logic App -> Service Bus -> Function):** Um Azure Logic App envia uma mensagem para o Azure Service Bus, que é lida por outra Azure Function (`fn-ler-sb`).

## 2. Pré-requisitos

*   Conta ativa no **Microsoft Azure**.
*   **Azure CLI** ou **Azure PowerShell** instalados.
*   **Visual Studio Code** com as extensões **Azure Functions** e **C#** (opcional, mas recomendado para desenvolvimento local).
*   **SDK do .NET** (versão 6 ou superior, conforme o código C#).

## 3. Criação dos Recursos na Azure

### 3.1. Azure SQL Database e Tabela

Crie um Azure SQL Database e, em seguida, a tabela `ToDo` que será usada pela Azure Function.

**Esquema da Tabela `ToDo`:**

| Coluna | Tipo de Dados | Descrição |
| :--- | :--- | :--- |
| `Id` | `NVARCHAR(50)` | Identificador único do item (GUID). |
| `Description` | `NVARCHAR(MAX)` | Descrição da tarefa. |
| `IsCompleted` | `BIT` | Status da tarefa (0 ou 1). |

**Comando SQL (a ser executado no editor de consultas do Azure Portal):**

```sql
CREATE TABLE ToDo (
    Id NVARCHAR(50) PRIMARY KEY,
    Description NVARCHAR(MAX) NOT NULL,
    IsCompleted BIT NOT NULL
);
```

### 3.2. Azure Service Bus

Crie um namespace do Azure Service Bus (Tier Standard ou Premium) e um **Tópico** ou **Fila** com o nome **`logicapp`**.

### 3.3. Azure Functions App

Crie um Azure Functions App (runtime .NET) que hospedará as duas funções.

**Configurações Essenciais:**

1.  **`SqlConnectionString`:** Adicione uma **Application Setting** com a string de conexão do seu Azure SQL Database.
2.  **`ServiceBusConnection`:** Adicione uma **Application Setting** com a string de conexão do seu Azure Service Bus.

## 4. Implementação das Azure Functions

O código-fonte em C# para as funções já foi analisado. Você deve criar um projeto de Azure Functions em C# e adicionar as seguintes classes:

### 4.1. Função de Persistência (`fn-save-sql`)

Esta função é acionada por HTTP e usa o *Output Binding* SQL.

**`fn-save-sql/Model/ToDoItem.cs`**

```csharp
namespace fn_save_sql.Model
{
    public class ToDoItem
    {
        public string Id { get; set; }
        public string Description { get; set; }
        public bool IsCompleted { get; set; }
    }
}
```

**`fn-save-sql/Function1.cs`** (Código já analisado, responsável por receber HTTP e salvar no SQL)

### 4.2. Função de Leitura do Service Bus (`fn-ler-sb`)

Esta função é acionada por uma mensagem no Service Bus.

**`fn-ler-sb/Function1.cs`** (Código já analisado, responsável por ler a mensagem do Service Bus)

## 5. Criação do Azure Logic App

O Logic App será o orquestrador que envia a mensagem para o Service Bus.

1.  **Crie um Logic App** (Consumo ou Standard).
2.  **Gatilho (Trigger):** Use um gatilho **HTTP Request** (para simular uma chamada externa) ou **Recurrence** (para um agendamento simples).
3.  **Ação 1: Enviar Mensagem para o Service Bus**
    *   Adicione uma ação **Azure Service Bus**.
    *   Selecione a operação **"Send message"** (Enviar mensagem).
    *   Configure a conexão usando a string de conexão do Service Bus.
    *   Selecione o **Tópico/Fila** chamado **`logicapp`**.
    *   No campo **Content**, insira o corpo da mensagem (ex: um JSON simples ou uma string).
    *   *Exemplo de Content (JSON):*
        ```json
        {
            "timestamp": "@{utcNow()}",
            "message": "Mensagem enviada pelo Logic App para o Service Bus."
        }
        ```

##