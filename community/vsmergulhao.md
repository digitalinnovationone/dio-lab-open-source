# Repositório de teste para comandos do Git - GitHub

Comandos básicos do git para versionamento e criação de repositório
## Autor

- [@vsmergulhao](https://www.github.com/vsmergulhao)


## Documentação

[Documentação Git](https://git-scm.com/docs)


## 🚀 Sobre mim
Gerente de projetos, desenvolvedor, analista de dados, engenheiro de software, analista de requisitos, tester, sempre a procura de mais conhecimento...

## Exemplos de comando Git

### Cria um diretório local e abre o diretório
```bash
mkdir teste-git_local
cd teste-git_local
```

### Inicializa o versionamento no diretório criado
```bash
git init
```

### Visualiza o config local e volta para o diretório anterior
```bash
cat config
```
### Clona o projeto git
```bash
git clone <URL>
```

### Clona o projeto git passando o nome do diretório
```bash
git clone git@github.com:<USER_NAME>/teste-git.git  <nome do diretório>
```

### Mostra a diferença de um diretório clonado   Possui os dados do remote
```bash
cd teste-git
```
```bash
cd .git/
```
```bash
cat config
```
```console
			[core]
					repositoryformatversion = 0
					filemode = true
					bare = false
					logallrefupdates = true
		👉  [remote "origin"]
					url = git@github.com:<USER_NAME>/teste-git.git
					fetch = +refs/heads/*:refs/remotes/origin/*
			[branch "main"]
					remote = origin
					merge = refs/heads/main
```

```bash
git remote -v
```
```
origin  git@github.com:<USER_NAME>/teste-git.git (fetch)
origin  git@github.com:<USER_NAME>/teste-git.git (push)
```

### Quando o diretório criado pelo git init não possuir as configurações do remote

```bash
 cat .git/config
```
```console
        [core]
                repositoryformatversion = 0
                filemode = true
                bare = false
                logallrefupdates = true
```
```bash
git remote add origin https://github.com/<USER_NAME>/teste-git.git
```
```bash
cat .git/config
```
```console
        [core]
                repositoryformatversion = 0
                filemode = true
                bare = false
                logallrefupdates = true
        👉[remote "origin"]
                url = https://github.com/<USER_NAME>/teste-git.git
                fetch = +refs/heads/*:refs/remotes/origin/*

```
### Quando fizer o clone irá trazer apenas a branch selecionada
```bash
git clone URL --branch <nome da branch> --single-branch
```

### Mostra o status da branch atual
```bash
git status
```
```console
			On branch main

			No commits yet

			nothing to commit (create/copy files and use "git add" to track)
```
```bash
 touch README.md 👉Cria um arquivo README.md com o camando touch
```
```bash
 vi README.md 👀Visualiza o arquivo README.md 👀 📤<Ctrl+:>q <enter>
```
```bash
 git status
```
```console
    On branch main
    No commits yet
    Untracked files:
    (use "git add <file>..." to include in what will be committed)
            README.md

    nothing added to commit but untracked files present (use "git add" to track)
```

### Adiciona um arquivo específico na área de preparação
```bash
git add README.md
```
```bash
git status
```
```console
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

### Adiciona todos os arquvivos e diretórios alterados na área de preparação
```bash
git add .
```
```bash
git status
```

```console
    On branch main
    Changes to be committed:
    (use "git restore --staged <file>..." to unstage)
            new file:   .gitignore
            new file:   alunos/.gitkeep

```

### Commita o(s) arquivo(s) que estão na área de preparação com uma mensagem
```bash
git commit -m"Commit inicial"
```
```console
		[main (root-commit) 3ca7f27] Commit inicial
		 1 file changed, 140 insertions(+)
		 create mode 100644 README.md

```

### Git log -> Exibe o log de atividades
```bash
git log
```
```
		commit 3ca7f271f2274c2d6408c4c42d53399b9c4c385e (HEAD -> main)
		Author: <Nome do usuário> <email>
		Date:   Thu Oct 16 15:06:56 2025 -0300

			Commit inicial
```
### Git status sem nenhuma alteração
```bash
git status
```
```
	On branch main
	nothing to commit, working tree clean
```

### O Git não reconhece diretórios vazios

```bash
mkdir resumo
```
```bash
mkdir alunos
```
```bash
git status
```

```
    On branch main
    nothing to commit, working tree clean
```

```bash
ls
```
```
README.md  alunos  resumo
```

### Git ignore no exemplo irá ignorar o diretório resumo
```bash
echo resumos/ > .gitignore
```
```bash
git status
```
```
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

nothing added to commit but untracked files present (use "git add" to track)
```

### Arquivo .gitkeep -> Arquivo nome do arquivo convencionado para que o git reconheca direórios vazios
```bash
touch alunos/.gitkeep
```
```bash
git status
```
```
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        alunos/

nothing added to commit but untracked files present (use "git add" to track)
```


### Git Restore -> Restaura o arquivo com o conteúdo anterior a modificação
```bash
git status
```
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```
```bash
git restore README.md
```
```bash
git status
```
```
On branch main
nothing to commit, working tree clean
```

### Modifica o comentário do último commit
```bash
git commit --amend -m"Criando o gitignore e o .gitkeep no diretório alunos"
```
```
[main 9cd02fe] Criado o gitignore e o .gitkeep no diretório alunos
 Date: Thu Oct 16 15:29:36 2025 -0300
 3 files changed, 98 insertions(+), 16 deletions(-)
 create mode 100644 .gitignore
 create mode 100644 alunos/.gitkeep
```
```bash
git log
```
```
commit 9cd02fec80831150658837b65f591de285cc5074 (HEAD -> main)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 15:29:36 2025 -0300

    Criado o gitignore e o .gitkeep no diretório alunos

commit 3ca7f271f2274c2d6408c4c42d53399b9c4c385e
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 15:06:56 2025 -0300

    Commit inicial
```

## Abre o editor para modificar o texto do commit
```bash
git commit --amend
```

### Volta para o commit anterior especificado pelo hash
```bash
git log
```
```
commit 9cd02fec80831150658837b65f591de285cc5074 (HEAD -> main)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 15:29:36 2025 -0300

    Criado o gitignore e o .gitkeep no diretório alunos

commit 3ca7f271f2274c2d6408c4c42d53399b9c4c385e
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 15:06:56 2025 -0300

    Commit inicial
```
```bash
git reset --soft 3ca7f271f2274c2d6408c4c42d53399b9c4c385e
```
```bash
git status
```
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        modified:   README.md
        new file:   alunos/.gitkeep

```
```bash
git log
```
```
commit 3ca7f271f2274c2d6408c4c42d53399b9c4c385e (HEAD -> main)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 15:06:56 2025 -0300

    Commit inicial
```
### Git reset -mixed (comportamento padrão) recupera os arquivos anteriores e coloca em nossa árvore de trabalho
```bash
git log
```
```
commit bf0753d9107b340d198acafddbf296c46d76179c (HEAD -> main)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 16:54:04 2025 -0300

    Commit de teste reset -soft

commit 3ca7f271f2274c2d6408c4c42d53399b9c4c385e
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 15:06:56 2025 -0300

    Commit inicial
```
```bash
git reset --mixed 3ca7f271f2274c2d6408c4c42d53399b9c4c385e
```
```
Unstaged changes after reset:
       README.md
```
```bash
git log
```
```
commit 3ca7f271f2274c2d6408c4c42d53399b9c4c385e (HEAD -> main)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 15:06:56 2025 -0300

    Commit inicial
```
```bash
git status
```
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        alunos/

```

### Git reset --hard retorna ao ponto da brach marcada e ignora inclusive os arquivos modificados
```bash
git add .
```
```bash
git commit -m"Commit de teste reset -mixed"
```
```
[main be1b5d6] Commit de teste reset -mixed
 3 files changed, 98 insertions(+), 16 deletions(-)
 create mode 100644 .gitignore
 create mode 100644 alunos/.gitkeep
```
```bash
git log
```
```
commit be1b5d63a9b85f8a1cd264b51350711b375e6a3d (HEAD -> main)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 16:58:15 2025 -0300

    Commit de teste reset -mixed

commit 3ca7f271f2274c2d6408c4c42d53399b9c4c385e
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 15:06:56 2025 -0300

    Commit inicial
```
```bash
git reset --hard 3ca7f271f2274c2d6408c4c42d53399b9c4c385e
```
```
HEAD is now at 3ca7f27 Commit inicial
```
```bash
git status
```
```
On branch main
nothing to commit, working tree clean
```
```bash
git log
```
```
commit 3ca7f271f2274c2d6408c4c42d53399b9c4c385e (HEAD -> main)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 15:06:56 2025 -0300

    Commit inicial
```

### Mostra todo o histórico de alterações ```git reflog```
```bash
 git reflog
```
```bash
3ca7f27 (HEAD -> main) HEAD@{0}: reset: moving to 3ca7f271f2274c2d6408c4c42d53399b9c4c385e
be1b5d6 HEAD@{1}: commit: Commit de teste reset -mixed
3ca7f27 (HEAD -> main) HEAD@{2}: reset: moving to 3ca7f271f2274c2d6408c4c42d53399b9c4c385e
bf0753d HEAD@{3}: commit: Commit de teste reset -soft
3ca7f27 (HEAD -> main) HEAD@{4}: reset: moving to 3ca7f271f2274c2d6408c4c42d53399b9c4c385e
9cd02fe HEAD@{5}: commit (amend): Criado o gitignore e o .gitkeep no diretório alunos
de3d221 HEAD@{6}: commit: Teste de commit
3ca7f27 (HEAD -> main) HEAD@{7}: commit (initial): Commit inicial
```

### git reset <nome_arquivo> retira o arquivo da área de preparação antes do commit
```bash
git status
```
```
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        aula1.md
        aulas/

nothing added to commit but untracked files present (use "git add" to track)
```
```bash
git add .
```
```bash
git status
```
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   aula1.md
        new file:   aulas/aula2.md

```
```bash
git reset aula1.md
```
```bash
git status
```
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   aulas/aula2.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        aula1.md
```

### Restaura o arquivo para versão anterior  ```git restore --staged <nome do arquivo>``` da área de preparaçao antes do commit
```bash
git restore --staged aulas/aula2.md
```
```bash
git status
```
```
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        aula1.md
        aulas/

nothing added to commit but untracked files present (use "git add" to track)
```

### Cria um vínculo da origin no servidor remoto ```git remote add```
```bash
git remote add origin https://github.com/<USER_NAME>/teste-git_local.git
```

### Realiza o envio do Repositório local para o repositório remoto
```bash
git push -u origin main
```

### Atualiza os arquivos remoto para o local
```bash
git pull
```

### Cria e muda de branch ```git checkout -b <nome da branch>```
```bash
git checkout -b teste
```
```
local:~/test_git_branch$ git checkout -b teste
Switched to a new branch 'teste'
local:~/test_git_branch$ git log
commit 1d0d26cd24e8e488773541d9e204e4d202b7ddae (HEAD -> teste, main)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 20:29:12 2025 -0300

    Commit 2

commit 99cea63c6413e9ffdf93e07c91ce6a00e426851b
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 20:26:26 2025 -0300

    Commit 1
```

### Listando branch ```git branch -v```
```bash
git branch -v
```
```
local:~/test_git_branch$ echo "Teste de branch3" > commit_branch3.txt
local:~/test_git_branch$ git add .
local:~/test_git_branch$ git commit -m"Commit 3"
[teste 99d3df9] Commit 3
 1 file changed, 1 insertion(+)
 create mode 100644 commit_branch3.txt
local:~/test_git_branch$ git log
commit 99d3df9db9763e578f6d20350e538005d457cb6e (HEAD -> teste)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 20:33:04 2025 -0300

    Commit 3

commit 1d0d26cd24e8e488773541d9e204e4d202b7ddae (main)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 20:29:12 2025 -0300

    Commit 2

commit 99cea63c6413e9ffdf93e07c91ce6a00e426851b
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 20:26:26 2025 -0300

    Commit 1
local:~/test_git_branch$ git checkout main
Switched to branch 'main'
local:~/test_git_branch$ git log
commit 1d0d26cd24e8e488773541d9e204e4d202b7ddae (HEAD -> main)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 20:29:12 2025 -0300

    Commit 2

commit 99cea63c6413e9ffdf93e07c91ce6a00e426851b
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 20:26:26 2025 -0300

    Commit 1

local:~/test_git_branch$ git branch -v
* main  1d0d26c Commit 2
  teste 99d3df9 Commit 3
```

### Para mesclar a branch atual com a branch selecionada ```git merge <nome da branch>```
```bash
git merge teste
```

```
Updating 1d0d26c..99d3df9
Fast-forward
 commit_branch3.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 commit_branch3.txt
local:~/test_git_branch$ git log
commit 99d3df9db9763e578f6d20350e538005d457cb6e (HEAD -> main, teste)
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 20:33:04 2025 -0300

    Commit 3

commit 1d0d26cd24e8e488773541d9e204e4d202b7ddae
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 20:29:12 2025 -0300

    Commit 2

commit 99cea63c6413e9ffdf93e07c91ce6a00e426851b
Author: <Nome do usuário> <email>
Date:   Thu Oct 16 20:26:26 2025 -0300

    Commit 1
local:~/test_git_branch$ git branch -v
* main  99d3df9 Commit 3
  teste 99d3df9 Commit 3
```

### Exclui a branch ```git branch -d <nome da branch>```
```bash
git branch -d teste
```
```
Deleted branch teste (was 99d3df9).
```
### Atualiza sem mesclar a branch com o diretório local ```git fetch origin main```
```bach
git fetch origin main
```
```
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 961 bytes | 961.00 KiB/s, done.
From https://github.com/<USER_NAME>/teste-git_local
 * branch            main       -> FETCH_HEAD
   0484148..da3c33f  main       -> origin/main
```

### Exibe a diferença entre branchs ```git diff <branch_origem> <branch_de_comparação>```
```bach
git diff main origin/main
```
```
diff --git a/aula1.md b/aula1.md
index e69de29..209ddb9 100644
--- a/aula1.md
+++ b/aula1.md
@@ -0,0 +1 @@
+teste commitado^M
```

### Mescla a branch atual com a especificada ```git merge  <nome_branch>```
```bach
git merge origin/main
```
```
Updating 0484148..da3c33f
Fast-forward
 aula1.md | 1 +
 1 file changed, 1 insertion(+)
```

### Clone de uma branch específica
```bach
git clone https://github.com/<USER_NAME>/teste-git_local.git --branch Teste-de-branch-criada-no-remoto --single-branch
```
## Gerando SSH

### Gerando chave SSH no linux
```bash
ls -al ~/.ssh    👉 Veriofica se existe o diretório SSH
```

### Se não existir
```bash
ssh-keygen -t ed25519 -C "email"
```

### Inicializa o SSH agent em background
```bash
eval "$(ssh-agent -s)"
    Agent pid 77602
```

### Adiciona a chave no SSH-agent
```bash
ssh-add ~/.ssh/id_ed25519
```

### Ir para diretório  SSH e listar as chaves
```bash
cd ~/.ssh
ls
```
```console
		id_ed25519     👉Chave privada
		id_ed25519.pub 👉Chave pública
```

### Exibe o conteúdo da chave
```bash
cat id_ed25519.pub
		ssh-ed25519 <chave> <email>  👉Retorno do arquivo
```
