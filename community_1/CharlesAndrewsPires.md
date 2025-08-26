<h1 align="center"> Saudações, tech. </h1>

> :construction: Profile em construção :construction:

1.Meu nome é Charles e tenho interesse no mundo da inteligência artificial, blockchain e afins...

2.Espero obter bons conhecimentos com a ajuda do time da DIO.
![OIG o_](https://github.com/CharlesAndrewsPires/Projetos-DIO/assets/153829352/04f7fb44-d746-41f4-8774-47f4fbf7092a)

## Alguns comandos importantes no Git
_config --global user.name (ou user.email)_
>Altera o nome/email do usuario

_mkdir (nome do diretorio)_
>cria uma pasta, um diretorio

_cd (nome do diretorio)_
>entra na pasta indicada

_git init_
>torna a pasta um diretorio Git

_git clone URL (repositorio remoto do GitHub)_
>importa um diretorio do GitHub

_git remote -v_
>mostra o repositorio GitHub ao qual esta vinculado o Git (local)

_git remote add origin URL_
>associa o seu diretorio local (Git) ao GitHub
>nesse caso e melhor seguir as orientacoes para a criacao/importacao de diretorio no GitHub

_git status_
>indica como esta a sua arvore de trabalho no Git (a situacao do trabalho atual): se houve alguma alteracao nos arquivos, etc...

_git add (nome do arquivo)_
>adiciona/vincula o arquivo para a sua arvore de trabalho

_git add ._
>adiciona/vincula todos os arquivos que sofreram alteracao

_git commit -m"(nome da sua nova versao)"_
>vincula as alteracoes que voce realizou gerando uma nova versao

_git log_
>elenca todas as alteracoes/versoes (commit) realizadas

_git reflog_
>elenca todas as alteracoes/versoes (commit) realizadas de forma detalhada

_(pasta)/ > .gitignore_
>identifica uma pasta que voce nao quer que faca parte do seu trabalho
>como o Git nao identifica pastas vazias, pode ser que encontremos arquivos com o nome *(arquivo).gitkeep*. Isso serve para identificar que a pasta e que ela esta vazia.

_rm -rf .git_
>exclui o repositorio (retira da arvore de trabalho)

_git restore + (nome do arquivo)_
>descarta a ultima alteracao (retoma a ultima versao do arquivo que foi modificado)

_git comit --amend -m"(novo nome do commit)_
>altera o nome do ultimo commit

_git reset --soft (ou --mixed ou --hard)_
>retoma um commit anterior
>a depender do tipo utilizado (soft, mixed ou hard), o Git podera disponibilizar ou nao os arquivos que foram criados apos o commit

_git push_
>envia as alteracoes do repositorio local para o GitHub

_git pull_
>puxa as alteracoes realizadas do GitHub para o local (Git)

_git checkout -b (nome do novo branch)_
>o branch representa uma nova ramificacao do seu projeto, para nao interferir no seu projeto principal
>utilizado para que varias pessoas trabalhem em diferentes aspectos no projeto: correcao de bugs, nova funcionalidade, etc...

_git checkout (nome da branch)_
>alterna para o branch indicado

_git branch_
>elenca todas as branch

_git branch -v_
>mostra todas as branch e quais os commit de cada branch

_git merge (nome da branch)_
>mescla as branch (as commit de cada branch serao igualadas)

_git branch -d (nome da branch)
>exclui a branch indicada

## Autenticacao por Token
Apos gerado o Token (GitHub), inserir o codigo *git clone + URL (o codigo gerado na criacao do Token)*

## Criar ou vincular um repositorio no GitHub
Utilizando o GitHub fica mais facil: ele traz instrucoes para criar ou importar um repositorio do zero

### Create a new repository on the command line:
echo "# meu-projeto" >> README.md
git init
git add README.md
git comit -m "first comit"
git branch -M main
git remote add origin https://github.com/... (diretorio criado no GitHub)
git push -u origin main

### Push an existing repository from the command line
git remote add origin https://github.com/... (diretorio criado no GitHub)
git branch -M main
git push -u origin main