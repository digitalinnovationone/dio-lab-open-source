[![Leia em Português](https://img.shields.io/badge/%F0%9F%87%A7%F0%9F%87%B7%20Portugu%C3%AAs-F0FFFF.svg)](COMANDOSGIT.md)
[![Leia em Inglês](https://img.shields.io/badge/%F0%9F%87%BA%F0%9F%87%B8%20English-gray.svg)](GITCOMMANDS.md)

# Comandos do Git

Este documento fornece uma visão geral dos comandos essenciais do Git.

😁 Sinta-se à vontade para contribuir e melhorar este guia!

## Índice
- [⚙️ Configurando o Git](#configurando-o-git)
- [📚 Comandos Básicos](#comandos-basicos)
  - [Operações de Repositório](#operacoes-de-repositorio)
  - [Conexões Remotas](#conexoes-remotas)
  - [Operações de Commit](#operacoes-de-commit)
- [📈 Comandos Intermediários do Git](#comandos-intermediarios-do-git)
  - [Criação de Branches e Merging](#criacao-de-branches-e-merging)
  - [Stashes (Guardando Mudanças Temporariamente)](#stashes)
  - [Reescrevendo o Histórico](#reescrevendo-o-historico)
  - [Repositórios Remotos](#repositorios-remotos)
  - [Inspecionando Mudanças](#inspecionando-mudancas)
- [🧠 Comandos Avançados do Git](#comandos-avancados-do-git)
  - [Refs e Reflog](#refs-e-o-reflog)
  - [Bisecting](#bisecting)
  - [Filter-branch](#filter-branch)
  - [Submódulos](#submodulos)
  - [Worktrees](#worktrees)
  - [Rebase Avançado](#rebase-avancado)
  - [Limpeza](#limpeza)
  - [Cherry-picking](#cherry-picking)
  - [Merge Avançado](#merge-avancado)

<a id="configurando-o-git"></a>
## ⚙️ Configurando o Git

- **Configurando seu e-mail**:
  ```bash
  $ git config user.email [seu_email_aqui]
  ```

- **Configurando seu nome de usuário**:
  ```bash
  $ git config user.name [seu_usuario_aqui]
  ```

Se você precisar especificar o escopo para sua configuração, use as tags abaixo:

- **Escopo local** (específico para o repositório atual):
  ```bash
  $ git config --local user.email [seu_email_aqui]
  ```

- **Escopo global** (aplica-se a todos os repositórios em seu sistema):
  ```bash
  $ git config --global user.email [seu_email_aqui]
  ```

- **Escopo do sistema** (aplica-se a todo o sistema, afetando todos os usuários):
  ```bash
  $ git config --system user.email [seu_email_aqui]
  ```

<a id="comandos-basicos"></a>
## 📚 Comandos Básicos

### Operações de Repositório

- **Inicializando um novo repositório local**:
  ```bash
  $ git init
  ```

- **Clonando um repositório remoto existente**:
  ```bash
  $ git clone [url_origem_remota]
  ```

- **Clonando um branch específico**:
  ```bash
  $ git clone --branch [nome_do_branch] [url_origem_remota]
  ```

- **Clonando para um diretório especificado**:
  ```bash
  $ git clone [url_origem_remota] [nome_do_diretorio]
  ```
### Conexões Remotas

- **Listando repositórios remotos conectados**:
  ```bash
  $ git remote
  ```

- **Adicionando uma nova conexão remota**:
  ```bash
  $ git remote add [nome_remoto] [url_para_remoto]
  ```

- **Removendo uma conexão remota existente**:
  ```bash
  $ git remote rm [nome_remoto]
  ```

- **Renomeando uma conexão remota**:
  ```bash
  $ git remote rename [nome_antigo_remoto] [nome_novo_remoto]
  ```

### Operações de Commit

- **Preparando todas as mudanças para commit**:
  ```bash
  $ git add --all
  ```
  ou
  ```bash
  $ git add -a
  ```
  ou simplesmente
  ```bash
  $ git add .
  ```

- **Commitando mudanças preparadas com uma mensagem**:
  ```bash
  $ git commit -m "sua mensagem aqui"
  ```

- **Preparando e commitando todas as mudanças em uma etapa**:
  ```bash
  $ git commit -a -m "sua mensagem aqui"
  ```

- **Modificando a mensagem do commit mais recente**:
  ```bash
  $ git commit --amend -m "nova mensagem aqui"
  ```

<a id="comandos-intermediarios-do-git"></a>
## 📈 Comandos Intermediários do Git

<a id="criacao-de-branches-e-merging"></a>
### Criação de Branches e Merging

- **Listando todos os branches locais no repositório atual**:
  ```bash
  $ git branch
  ```

- **Mudando para um branch**:
  ```bash
  $ git checkout [nome_do_branch]
  ```

- **Criando e mudando para um novo branch**:
  ```bash
  $ git checkout -b [nome_do_branch]
  ```

- **Fazer merge de um branch no branch ativo**:
  ```bash
  $ git merge [nome_do_branch]
  ```

- **Deletando um branch**:
  ```bash
  $ git branch -d [nome_do_branch]
  ```

<a id="stashes"></a>
### Stashes (Guardando Mudanças Temporariamente)

- **Criando um stash das mudanças atuais**:
  ```bash
  $ git stash
  ```
  Salva temporariamente mudanças que ainda não foram commitadas.

####
####

- **Criando um stash das mudanças atuais com uma mensagem**:
  ```bash
  $ git stash save "Sua mensagem aqui"
  ```
  Salva temporariamente mudanças que ainda não foram commitadas com uma mensagem descritiva.

####
####

- **Listando todos os stashes**:
  ```bash
  $ git stash list
  ```
  Mostra uma lista de todos os stashes criados.

####
####

- **Aplicando um stash específico**:
  ```bash
  $ git stash apply stash@{n}
  ```
  Restaura as mudanças de um stash específico, onde `n` é o número do stash (por exemplo, `stash@{0}`, `stash@{1}`).

####
####

- **Aplicando o stash mais recente**:
  ```bash
  $ git stash apply
  ```

- **Descartando um stash**:
  ```bash
  $ git stash drop
  ```
  Remove o stash mais recente.

####
####

- **Descartando um stash específico**:
  ```bash
  $ git stash drop stash@{n}
  ```
  Remove um stash específico baseado no número `n`.

####
####

- **Aplicando e descartando o stash mais recente**:
  ```bash
  $ git stash pop
  ```
  Aplica o stash mais recente e, em seguida, o remove da lista de stashes.

####
####

<a id="reescrevendo-o-historico"></a>
### Reescrevendo o Histórico

- **Rebase de sua branch**:
  ```bash
  $ git rebase [branch_base]
  ```
  Reaplica os commits de sua branch sobre a branch base. Útil para garantir um histórico linear.

####
####

- **Rebase interativo**:
  ```bash
  $ git rebase -i [commit_base]
  ```
  Permite editar commits no processo.

####
####

- **Continuar o rebase após resolver conflitos**:
  ```bash
  $ git rebase --continue
  ```

####
####

- **Abortar o rebase atual**:
  ```bash
  $ git rebase --abort
  ```

####
####

- **Alterar o último commit (sem mudar a mensagem do commit)**:
  ```bash
  $ git commit --amend --no-edit
  ```
  Permite adicionar novas mudanças ao commit anterior sem alterar sua mensagem.

####
####

<a id="repositorios-remotos"></a>
### Repositórios Remotos

- **Buscar alterações do remoto sem merge**:
  ```bash
  $ git fetch [nome_remoto]
  ```
  Este comando recupera atualizações de um repositório remoto, mas não faz o merge dessas alterações com sua branch local. É útil para ver atualizações antes de decidir se deseja integrá-las.

####
####

- **Puxar alterações de um repositório remoto**:
  ```bash
  $ git pull [nome_remoto] [nome_branch]
  ```
  Este comando busca e tenta automaticamente fazer o merge das alterações da branch remota especificada com sua branch local atual.

####
####

- **Enviando uma branch para o remoto**:
  ```bash
  $ git push [nome_remoto] [nome_branch]
  ```
  Envia suas alterações locais para o repositório remoto. Isso atualiza a branch remota com seus commits recentes.

####
####

- **Configurando uma conexão de rastreamento entre uma branch local e uma branch remota**:
  ```bash
  $ git branch --u [nome_remoto]/[nome_branch]
  ```
  Estabelece uma conexão de rastreamento entre a branch local e a branch remota especificada. Isso é útil porque permite que `git pull` e `git push` saibam automaticamente de qual branch remota puxar ou para qual enviar.

####
####

- **Puxar alterações e fazer rebase (em vez de merge)**:
  ```bash
  $ git pull --rebase
  ```
  Em vez de fazer o merge dos commits, este comando reaplica seus commits locais sobre as alterações buscadas. Ajuda a manter um histórico de commits limpo e linear.

####
####

<a id=inspecionando-mudancas></a>
### Inspecionando Mudanças

- **Visualizar histórico de commits**:
  ```bash
  $ git log
  ```

- **Visualizar o diff para as mudanças staged**:
  ```bash
  $ git diff --staged
  ```
  Mostra a diferença entre as mudanças staged e o último commit.

- **Ver a diferença entre a branch atual e outra branch**:
  ```bash
  $ git diff [nome_outra_branch]
  ```

- **Visualizar o log em uma interface gráfica**:
  ```bash
  $ gitk
  ```
  Abre uma interface gráfica para navegar e inspecionar o histórico de commits (A disponibilidade de `gitk` pode variar com base na instalação e no sistema operacional).

####

- **Exibindo log em um formato bonito com uma linha por commit**:
  ```bash
  $ git log --oneline --graph --all --decorate
  ```
  Exibe o histórico de commits em um formato conciso com branches e tags, facilitando o entendimento do histórico do repositório.

<a id="comandos-avancados-do-git"></a>
## 🧠 Comandos Avançados do Git

### Refs e o Reflog

- **Visualizar o reflog**:
  ```bash
  $ git reflog
  ```
  Mostra um registro de onde seu HEAD e as referências de branch estiveram. Pode ser usado para recuperar commits ou branches perdidos.

- **Reaplicar um commit perdido**:
  ```bash
  $ git cherry-pick [hash_do_commit]
  ```
  Este comando pode ser usado após consultar o reflog para aplicar um commit que foi perdido (devido a reset, rebase, etc.)

- **Recuperar um estado após um hard reset**:
  ```bash
  $ git reset 'HEAD@{1}'
  ```
  Este comando permite voltar ao estado anterior antes do hard reset.

### Bisecting

- **Iniciar o processo de bisect**:
  ```bash
  $ git bisect start
  ```

- **Marcar um commit como bom**:
  ```bash
  $ git bisect good
  ```

- **Marcar um commit como ruim**:
  ```bash
  $ git bisect bad
  ```

- **Encerrar o processo de bisect**:
  ```bash
  $ git bisect reset
  ```

- **Usando bisect para encontrar um commit problemático**:
  ```bash
  $ git bisect start
  $ git bisect bad
  $ git bisect good [hash_ultimo_commit_bom_conhecido]
  ```
  O Git verificará um commit no meio entre o último commit bom conhecido e o final de sua branch. Teste o commit, depois informe ao Git se ele é bom ou ruim. O Git continuará refinando até identificar o commit exato que introduziu um problema.

### Filter-branch

- **Substituindo todos os endereços de email no histórico**:
  ```bash
  $ git filter-branch --commit-filter 'if [ "$GIT_AUTHOR_EMAIL" = "old_email@example.com" ]; then
       export GIT_AUTHOR_EMAIL=new_email@example.com;
       export GIT_COMMITTER_EMAIL=new_email@example.com;
     fi;
     git commit-tree "$@"'
  ```
  ⚠️ **Aviso**: Este comando reescreve o histórico para substituir completamente os endereços de email em todo o repositório. Proceda com extrema cautela!

####
####

- **Removendo um arquivo de todo o histórico do Git**:
  ```bash
  $ git filter-branch --force --index-filter "git rm --cached --ignore-unmatch caminho_para_o_arquivo" --prune-empty --tag-name-filter cat -- --all
  ```
  ⚠️ **Aviso**: Este comando reescreve o histórico para remover completamente um arquivo do repositório. Proceda com extrema cautela!

####
####

### Submodules

- **Adding a submodule**:
  ```bash
  $ git submodule add [repository_url] [path_to_place_submodule]
  ```
  Adds another repository as a submodule in your current repo. This allows you to include and track another project within your own project.

####
####

- **Updating all submodules**:
  ```bash
  $ git submodule update --recursive --remote
  ```

### Worktrees

- **Creating a new worktree**:
  ```bash
  $ git worktree add [path] [branch]
  ```
  This allows you to check out multiple branches simultaneously in different directories.

####
####

### Advanced Rebase

- **Starting an Interactive Rebase**:
  ```bash
  $ git rebase -i [base_branch_name]
  ```

- **Squashing the last *n* commits into a single one**:
  ```bash
  $ git rebase -i HEAD~[n]
  ```
  In the text editor that pops up, replace "pick" with "squash" or "s" for the commits you want to squash into the previous one (the one above them).

####
####

### Cleanup

- **Cleaning untracked files**:
  ```bash
  $ git clean -f
  ```
  ⚠️ **Warning**: Permanently deletes untracked files from the working directory. Always double-check before executing.

####

- **Cleaning Untracked Files and Directories**:
  ```bash
  $ git clean -f -d
  ```
  ⚠️ **Warning**: Permanently removes untracked files and directories. Check carefully before executing.

####

- **Removing remote branches that no longer exist**:
  ```bash
  $ git fetch -p
  ```

- **Cleaning up local branches that have been merged**:
  ```bash
  $ git branch --merged | xargs git branch -d
  ```
  ⚠️ **Warning**: Ensure you no longer need the branches before removing them.

####

### Cherry-picking

- **Applying changes from specific commits**:
  ```bash
  $ git cherry-pick [commit_hash1] [commit_hash2]
  ```

- **Aborting cherry-pick**:
  ```bash
  $ git cherry-pick --abort
  ```
  ⚠️ **Warning**: Aborting the operation will revert any changes applied during the cherry-pick.

####


### Advanced Merge

- **Merging without an automatic commit**:
  ```bash
  $ git merge [branch_name] --no-commit
  ```

- **Merging and squashing all commits**:
  ```bash
  $ git merge --squash [branch_name]
  ```

  This takes all the commits from another branch and squashes them into a single commit on the current branch.

####

- **Previewing merge conflicts before merging**:
  ```bash
  $ git diff --name-only --diff-filter=U
  ```

- **Aborting a merge operation**:
  ```bash
  $ git merge --abort
  ```
  ⚠️ **Warning**: Aborting the merge will revert any changes made during the merge operation.

###

#### 😄 We hope that this guide has been helpful for you. If you have any feedback or would like to contribute with more information, please make a pull request or open an issue!