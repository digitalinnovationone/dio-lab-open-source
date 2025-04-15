
# Hello World GitHub

Aqui irei pontuar e exemplificar comandos que podem ser usados no Github usando o Git.


## Comandos Basicos

Para exibir log(histórico) das atividades.

```bash
  git log
```

Para exibir o estado atual da branch.

```bash
  git status
```

Para exibir a versão da branch.

```bash
  git branch -v
```
Para mostrar as configurações do repositório git
  (lembrando que antes tem de localizar o .git usando "cd .git" dentro do diretório).

```bash
  cat config
```

## Comandos de configuração

Comando para configurar o nome de usuário do github.

```bash
  git config --global user.name "USERNAME"
```
Comando para configurar o email do github.

```bash
  git config --global user.email "email"
```
Comando para indicar que aquela branch é a main no github.

```bash
  git config --global user.defaultBranch
```
Comando para adicionar o link em que o diretório será clonado.

```bash
  git remote add origin URL
```

## Comandos de criação de git e branch

Inicia uma instância Git no diretório, criando os arquivos necessários para manipulação do mesmo.

```bash
  git init
```

Cria uma branch(vertente) do projeto dentro do diretório.

```bash
  git checkout -b NAMEBRANCH
```

## Comandos para manipulação do github e branch

Comando usado para copiar um repositório do servidor github.

```bash
  git clone
```

Comando usado para copiar ultima versão	do diretório do servidor github.

```bash
  git pull
```
Comando usado para enviar ultima versão	do diretório do servidor github.

```bash
  git push
```
Comando usado para copiar adicionar arquivos a atual versão do diretório do servidor github.

```bash
  git add
```
Comando usado para enviar sua versão do diretório ao servidor github.

```bash
  git commit
```
Comando usado para restaurar ultima versão do diretório do servidor github.

```bash
  git restore
```
Comando usado para resetar niveladamente informações do diretório do servidor github.

  * elimina apenas a existência do commit
```bash
  git reset --soft HASHDOCOMMIT
```
  * elimina a existência do commit e as alterações feitas
```bash
  git reset --mixed HASHDOCOMMIT
```
  * elimina a existência do commit, as alterações e elimina os arquivos
```bash
  git reset --hard HASHDOCOMMIT
```

Comando usado para selecionar a branch

```bash
  git checkout BRANCH
```

Comando usado para atualizar arquivos deletados da branch

```bash
  git stash
```

Comando usado para mesclar arquivos e alterações com a atual branch

```bash
  git merge BRANCH
```
