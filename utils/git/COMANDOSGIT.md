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
  - [Stashing Changes](#stashing-changes)
  - [Reescrevendo o Histórico](#reescrevendo-o-historico)
  - [Repositórios Remotos](#repositorios-remotos)
  - [Inspecionando Mudanças](#inspecionando-mudancas)
- [🧠 Comandos Avançados do Git](#comandos-avancados-do-git)
  - [Refs e Reflog](#refs-e-reflog)
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

<a id="intermediate-git-commands"></a>
## 📈 Intermediate Git Commands

### Branching and Merging

- **Listing all local branches in the current repository**:
  ```bash
  $ git branch
  ```

- **Switching to a branch**:
  ```bash
  $ git checkout [branch_name]
  ```

- **Creating and switching to a new branch**:
  ```bash
  $ git checkout -b [branch_name]
  ```

- **Merging a branch into the active branch**:
  ```bash
  $ git merge [branch_name]
  ```

- **Deleting a branch**:
  ```bash
  $ git branch -d [branch_name]
  ```

### Stashing Changes

- **Stashing current changes**:
  ```bash
  $ git stash
  ```
  Temporarily saves changes that are not yet committed.

####
####

- **Stashing current changes with a message**:
  ```bash
  $ git stash save "Your message here"
  ```
  Temporarily saves changes that are not yet committed with a descriptive message.

####
####

- **Listing all stashed changes**:
  ```bash
  $ git stash list
  ```
  Shows a list of all the stashed changes.

####
####

- **Applying a specific stash**:
  ```bash
  $ git stash apply stash@{n}
  ```
  Restores the stashed changes from a specific stash, where `n` is the stash number (e.g., `stash@{0}`, `stash@{1}`).

####
####

- **Applying most recent stash**:
  ```bash
  $ git stash apply
  ```

- **Dropping a stash**:
  ```bash
  $ git stash drop
  ```
  Removes the latest stash.

####
####

- **Dropping a specific stash**:
  ```bash
  $ git stash drop stash@{n}
  ```
  Removes a specific stash based on the number `n`.

####
####

- **Applying and dropping the latest stash**:
  ```bash
  $ git stash pop
  ```
  Applies the latest stash and then removes it from the stash list.

####
####

### Rewriting History

- **Rebasing your branch**:
  ```bash
  $ git rebase [base_branch]
  ```
Reapplies your branch's commits onto the base branch. Useful for ensuring a linear history.

####
####

- **Interactive rebasing**:
  ```bash
  $ git rebase -i [base_commit]
  ```
  Allows you to edit commits in the process.

####
####

- **Continue rebasing after resolving conflicts**:
  ```bash
  $ git rebase --continue
  ```

####
####

- **Abort the current rebase**:
  ```bash
  $ git rebase --abort
  ```

####
####

- **Amending the latest commit (without changing commit message)
  ```bash
  $ git commit --amend --no-edit
  ```
  Allows you to add new changes to the previous commit without changing its commit message.

####
####

### Remote Repositories

- **Fetching changes from remote without merging**:
  ```bash
  $ git fetch [remote_name]
  ```
  This command retrieves updates from a remote repository but doesn't merge these changes with your local branch. It's useful to see updates before deciding whether you want to integrate them.

####
####

- **Pulling changes from a remote repository**:
  ```bash
  $ git pull [remote_name] [branch_name]
  ```
  This command fetches and automatically tries to merge changes from the specified remote branch with your current local branch.

####
####

- **Pushing a branch to remote**:
  ```bash
  $ git push [remote_name] [branch_name]
  ```
  Pushes your local changes to the remote repository. This updates the remote branch with your recent commits.

####
####

- **Configurando uma conexão de rastreamento entre um branch local e um branch remoto / Setting up a tracking connection between a local and remote branch**:
  ```bash
  $ git branch --u [remote_name]/[branch_name]
  ```
  Establishes a tracking connection between the local branch and the specified remote branch. This is handy as it allows `git pull` and `git push` to automatically know which remote branch to pull from or push to.

####
####

- **Pulling changes and rebasing (instead of merging)**:
  ```bash
  $ git pull --rebase
  ```
  Instead of merging commits, this command reapplies your local commits on top of the fetched changes. It helps to maintain a clean, linear commit history.

####
####

### Inspecting Changes

- **View commit history**:
  ```bash
  $ git log
  ```

- **Viewing the diff for the staged changes**:
  ```bash
  $ git diff --staged
  ```
  Displays the difference between the staged changes and the latest commit.

- **View difference between the current branch and another branch**:
  ```bash
  $ git diff [other_branch_name]
  ```

- **Viewing the log in a graphical interface**:
  ```bash
  $ gitk
  ```
  Opens a graphical interface to navigate and inspect the commit history (Availability of `gitk` may vary based on installation and OS).

####

- **Logging in a pretty format with one line per commit**:
  ```bash
  $ git log --oneline --graph --all --decorate
  ```
  Displays the commit history in a concise format with branches and tags, making it easier to understand the repository's history.

<a id="advanced-git-commands"></a>
## 🧠 Advanced Git Commands

### Refs and the Reflog

- **Viewing the reflog**:
  ```bash
  $ git reflog
  ```
  Shows a log of where your HEAD and branch references have been. This can be used to recover lost commits or branches.

- **Reapply a lost commit:**:
  ```bash
  $ git cherry-pick [commit_hash]
  ```
  This can be used after consulting the reflog to apply a commit that was lost (due to reset, rebase, etc.)

- **Recover a state after a hard reset**:
  ```bash
  $ git reset 'HEAD@{1}'
  ```
This command lets you go back to the previous state before the hard reset.

### Bisecting

- **Start the bisect process**:
  ```bash
  $ git bisect start
  ```

- **Mark a commit as good**:
  ```bash
  $ git bisect good
  ```

- **Mark a commit as bad**:
  ```bash
  $ git bisect bad
  ```

- **End the bisect process**:
  ```bash
  $ git bisect reset
  ```

- **Using bisect to find a bad commit**:
  ```bash
  $ git bisect start
  $ git bisect bad
  $ git bisect good [last_known_good_commit_hash]
  ```
  Git will then check out a commit halfway between the last known good commit and the end of your branch. Test the commit, then tell Git whether it's good or bad. Git will continue narrowing down until it identifies the exact commit that introduced an issue.

### Filter-branch

- **Replacing all email addresses in history**:
  ```bash
  $ git filter-branch --commit-filter 'if [ "$GIT_AUTHOR_EMAIL" = "old_email@example.com" ]; then
       export GIT_AUTHOR_EMAIL=new_email@example.com;
       export GIT_COMMITTER_EMAIL=new_email@example.com;
     fi;
     git commit-tree "$@"'
  ```
  ⚠️ **Warning**: This command rewrites the history to completely replace email addresses throughout the repository. Proceed with extreme caution!

####
####

- **Removing a file from the entire Git history**:
  ```bash
  $ git filter-branch --force --index-filter "git rm --cached --ignore-unmatch path_to_file" --prune-empty --tag-name-filter cat -- --all
  ```
  ⚠️ **Warning**: This command rewrites the history to completely remove a file from the repository. Proceed with extreme caution!

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