### Olá, eu sou Leandro Antônio Fortunato (lefortunato)

✨ **Engenheiro de sistemas** na FinanceIT.

🏢 **Atuação Profissional**
- 🚀 Engenheiro de sistemas Sr na empresa FinanceIT

# 🚀 Guia Prático de Git para Iniciantes

Bem-vindo(a) ao guia essencial de **Git**!  Se você tem pouco ou nenhum conhecimento sobre controle de versão, este manual foi feito especialmente para você. Aqui você aprenderá os comandos mais utilizados no dia a dia, explicados de forma simples, com descrições objetivas e exemplos práticos de uso.

---

## 📌 Sumário
1. [Conceitos Básicos](#-conceitos-básicos)
2. [Configuração Inicial](#1-configuração-inicial)
3. [Criando ou Obtendo Repositórios](#2-criando-ou-obtendo-repositórios)
4. [O Fluxo do Dia a Dia (Salvar Alterações)](#3-o-fluxo-do-dia-a-dia-salvar-alterações)
5. [Trabalhando com Ramificações (Branches)](#4-trabalhando-com-ramificações-branches)
6. [Sincronizando com o GitHub](#5-sincronizando-com-o-github)
7. [Desfazendo Erros](#6-desfazendo-erros)
8. [Resumo Rápido dos Comandos](#-resumo-rápido)

---

## 💡 Conceitos Básicos

Antes de ir para os comandos, pense no **Git** como uma **máquina do tempo para o seu código**:
- **Repositório (Repo):** É a pasta do seu projeto monitorada pelo Git.
- **Commit:** É como um "checkpoint" ou foto do seu código naquele exato momento.
- **Branch (Ramo):** Uma linha de desenvolvimento paralela (ideal para testar novidades sem quebrar o código principal).
- **Remote:** O servidor onde seu código fica salvo na nuvem (por exemplo, no GitHub).

---

## 1. Configuração Inicial

Antes de usar o Git pela primeira vez no seu computador, você precisa se identificar.

### `git config`
- **Descrição:** Define seu nome de usuário e e-mail. Essas informações ficarão registradas em todos os seus *commits*.
- **Caso de Uso:** Configurando o Git logo após instalá-lo no computador.

```bash
# Definir seu nome
git config --global user.name "Seu Nome"

# Definir seu e-mail (use o mesmo do GitHub)
git config --global user.email "seu.email@exemplo.com"
```

---

## 2. Criando ou Obtendo Repositórios

### `git init`
- **Descrição:** Transforma a pasta atual em um repositório Git zerado.
- **Caso de Uso:** Você iniciou um projeto novo na sua máquina e quer começar a controlar as versões dele com o Git.

```bash
git init
```

### `git clone`
- **Descrição:** Baixa uma cópia completa de um repositório existente (por exemplo, no GitHub) para a sua máquina.
- **Caso de Uso:** Baixar um projeto de outra pessoa ou um projeto seu que já está hospedado no GitHub.

```bash
git clone https://github.com/usuario/nome-do-repositorio.git
```

---

## 3. O Fluxo do Dia a Dia (Salvar Alterações)

Este é o ciclo que você mais repetirá: **Modificar código ➔ Checar status ➔ Preparar ➔ Salvar (Commit)**.

### `git status`
- **Descrição:** Mostra o estado atual das suas alterações. Diz quais arquivos foram modificados, adicionados ou removidos.
- **Caso de Uso:** Usado a todo momento para saber "o que está acontecendo" antes de salvar suas mudanças.

```bash
git status
```

### `git add`
- **Descrição:** Adiciona os arquivos modificados para a *Staging Area* (área de preparação antes do commit).
- **Caso de Uso:** Preparar arquivos específicos ou todos os arquivos para serem salvos no próximo checkpoint.

```bash
# Preparar um arquivo específico
git add index.html

# Preparar TODOS os arquivos modificados de uma vez
git add .
```

### `git commit`
- **Descrição:** Salva as alterações preparadas no histórico do repositório com uma mensagem explicativa.
- **Caso de Uso:** Registrar oficialmente uma conquista ou mudança relevante no código (ex.: criar uma tela de login).

```bash
git commit -m "Adiciona tela de login do usuário"
```

### `git log`
- **Descrição:** Exibe o histórico de todos os *commits* (checkpoints) feitos no projeto.
- **Caso de Uso:** Consultar quem alterou o quê e quando, ou ver mensagens de commits antigos.

```bash
# Exibe o histórico detalhado
git log

# Exibe o histórico de forma resumida e em uma linha por commit
git log --oneline
```

---

## 4. Trabalhando com Ramificações (Branches)

Branches permitem que você trabalhe em recursos novos sem mexer no código principal (*main* ou *master*) que já está funcionando.

### `git branch`
- **Descrição:** Lista, cria ou deleta ramificações.
- **Caso de Uso:** Ver em qual branch você está no momento ou criar uma nova branch.

```bash
# Listar todas as branches
git branch

# Criar uma nova branch chamada 'nova-funcionalidade'
git branch nova-funcionalidade
```

### `git checkout` / `git switch`
- **Descrição:** Alterna entre diferentes branches do projeto.
- **Caso de Uso:** Mudar para a branch de desenvolvimento para trabalhar em uma nova tarefa.

```bash
# Mudando para uma branch existente
git checkout nova-funcionalidade

# Atalho: Cria E já muda para a nova branch de uma só vez
git checkout -b nova-funcionalidade

# Nota: Em versões mais recentes do Git, você também pode usar:
git switch nova-funcionalidade
```

### `git merge`
- **Descrição:** Junta as alterações de uma branch dentro da branch atual.
- **Caso de Uso:** Você terminou de desenvolver uma funcionalidade na branch `nova-funcionalidade` e quer juntá-la na branch principal `main`.

```bash
# 1. Volte para a branch principal
git checkout main

# 2. Incorpore as mudanças da outra branch
git merge nova-funcionalidade
```

---

## 5. Sincronizando com o GitHub

Comandos para enviar suas alterações para a nuvem ou baixar as atualizações da sua equipe.

### `git remote`
- **Descrição:** Conecta seu repositório local a um repositório remoto (hospedado no GitHub, GitLab, etc.).
- **Caso de Uso:** Vincular uma pasta local recém-criada a um repositório do GitHub.

```bash
git remote add origin https://github.com/usuario/nome-do-repositorio.git
```

### `git push`
- **Descrição:** Envia seus commits locais para o repositório remoto na nuvem.
- **Caso de Uso:** Atualizar o GitHub com o código que você acabou de salvar na sua máquina.

```bash
# Envia os commits para a branch 'main' no GitHub
git push origin main
```

### `git pull`
- **Descrição:** Baixa as novidades do repositório remoto e atualiza seu código local de forma automática.
- **Caso de Uso:** Quando outra pessoa da equipe enviou alterações para o GitHub e você precisa atualizar a sua máquina antes de começar a trabalhar.

```bash
git pull origin main
```

---

## 6. Desfazendo Erros

Todos cometemos erros! O Git tem ferramentas incríveis para nos salvar.

### `git restore`
- **Descrição:** Descarta as alterações feitas em um arquivo que ainda **não foram salvas** com `git add` ou `git commit`.
- **Caso de Uso:** Você fez um teste no código, deu tudo errado e quer voltar para como o arquivo estava antes de você mexer.

```bash
# Restaura o arquivo para o estado original
git restore script.js
```

### `git reset`
- **Descrição:** Remove arquivos da área de preparação (*Staging Area*) ou desfaz commits.
- **Caso de Uso:** Você deu `git add .` por engano em um arquivo que não queria incluir.

```bash
# Retira um arquivo da área de preparação (sem apagar as alterações dele)
git restore --staged arquivo.txt
```

---

## 📑 Resumo Rápido

| Comando | Para que serve? |
| :--- | :--- |
| `git init` | Cria um novo repositório local |
| `git clone <url>` | Baixa um repositório da nuvem |
| `git status` | Mostra o estado dos seus arquivos |
| `git add .` | Prepara todas as alterações para o commit |
| `git commit -m "mensagem"` | Salva um histórico/checkpoint das alterações |
| `git push origin <branch>` | Envia suas alterações para o GitHub |
| `git pull origin <branch>` | Baixa e junta as alterações do GitHub na sua máquina |
| `git checkout -b <nome>` | Cria e entra em uma nova branch |

---

💡 **Dica de Ouro:** Não se preocupe em memorizar todos os comandos de primeira! Guarde este guia nos seus favoritos ou no seu perfil do GitHub para consultar sempre que tiver dúvidas.
