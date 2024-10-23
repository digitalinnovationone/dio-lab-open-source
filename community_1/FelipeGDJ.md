## Seja muito bem-vindo(a) ao meu perfil 😁

### Conecte-se comigo!


[![Gmail](https://img.shields.io/badge/Gmail-333333?style=for-the-badge&logo=gmail&logoColor=red)](mailto:fgomesj@gmail.com)

[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/DDI+21+979014032)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/fgomesj/)

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/FelipeGDJ)

# Ferramentas 

![Vscode](https://img.shields.io/badge/Vscode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)

# Linguagens de Marcação e Estilo

![Markdown](https://img.shields.io/badge/Markdown-000?style=for-the-badge&logo=markdown)



# Aulas Resumos
-  Git e GitHub

Repositório para armazenar resumos sobre o curso Versionamento de Códigos com git e GitHub com a Elidiana.

## 📘 Documentação
- [Documentação Git](https://git-scm.com/doc)
- [Documentação GitHub](https://docs.github.com/)

## ✍️ Resumo das Aulas

| Aulas | Resumos|
|-------|--------|
| Gravando Alteraçõesno Repositório Local | [Resumos]()|

## 💻 Links Uteis

[Guia de Contribuição DIO](https://github.com/FelipeGDJ/dio-lab-open-source/tree/main)

## 🔍 Resumo do Felipe Gomes

DIO.me BootCamp Vivo Início: 09/05/2024
Aula 001 

## Vídeo 001

Venilton

Bootcamps DIO: Educação Gratuita e Empregabilidade Juntas! 

Lógica, Especialista, Aprendizado, Reconhecimento, Notoriedade

## HERO 

Comunidade, Experiências, Salas rooms e Oportunidade.

## ACT 

Aquisição, Construção e Transição

## Video 002

Guilherme Carvalho

- Ambiente de Desenvolvimento e Primeiros Passos com Python

- Introdução ao Python

- Configuração do Ambiente de Desenvolvimento

- Primeiro Programa


## Video 003 

Guilherme Carvalho

- Conhecendo a Linguagem de Programação Python

- Tipos de Dados

- Modo interativo

- Variáveis e Constantes

- Conversão de Tipos

- Funções de Entrada e Saída

## Video 004

Elidiana Andrade

## Versionamento de Código com Git e GitHub
 
O que é versionamento de código?
software que controla arquivos ao longo do tempo e gerencia quais e quem realizou as alterações. 

## Repositório Git
 
O Git é um conceito essencial no mercado de trabalho, por isso sempre reforçamos sua importância em nossa metodologia educacional. Por isso, todo código-fonte desenvolvido durante este conteúdo foi versionado no seguinte endereço para que você possa consultá-lo a qualquer momento:
 
https://github.com/digitalinnovationone/
 

- VCS DISTRIBUÍDO (DVCS)
Cada clone é um backup
Possibilita fluxo de trabalho

- Git é um sistema de controle de versão distribuído
- Gratuito e Open Source (código aberto)
- Possui ramificações (braching) e fusões (merging) eficientes
- Leve e rápido

Links
https://git-scm.com/
(scm) source code manangements

*Fluxo básico*


git clone busca verão do servidor  
git clone <--- servidor  
git commit clona o projeto no repositorio local  
git commit para criar nova versão  
atualizar o repositorio remoto  
git pull puxa as alterações do remoto  
para o local  
git commit (puxa o projeto/versão)  
git pull puxa as alterações realizadas no remoto para o local  
git push (empurra) para o remoto  


## O que é GitHub

Plataforma de hospedagem de código que utiliza a ferramenta Git


Git faz gerenciamentos de versões  
GitHub servidor de hospedagem dos códigos


https://github.com/


git version

git config permite configurar variáveis

# Configurações do git
- Criar uma pasta

Botao direito abrir com gitbashhere  
Configurar nome e email   
git config --global user.name "nomeuser"  
git config --global useremail (email)
ctrl + l (limpar terminal)  
git config init.defaulBranch (master)  
git config --global init.defaultBranch main

$ git config init.defaultBranch

$ git config --global --list
user.name=username
user.email=user@gmail.com  
init.branch=main  
init.defaultbranch=main


- Resetar configurações

rm ~/.gitconfig

User-pc MINGW64 ~/Desktop/git1  
$ git config --global --list  
user.name=user  
user.email=user@gmail.com  
init.branch=main  
init.defaultbranch=main  


- AUTENTICAÇÃO NO GIT BASH


salvar credenciais na maquina
 
git config --global credential.helper cache
git config --globalgit credential.helper store


## Criando e Clonando Repositórios


1 - Transformando um diretório local que não está sobre controle de versão, num repositorio git

2 - Clonando um repositório existente

mkdir pasta  
cd pasta  
inicia um repositorio git  
git init  
abrir diretório git  
cd .git  
mostrar configs  
cat config  
conectar a pasta com repositorio remoto  
git remote add origim URL  
clona um repositorio  
caso queira clonar em pasta com nome diferente  
git clone URL name--dir--local  
Clonar repositorios de uma brench (específica)  
git clone URL --brach feature-1 --single-branch

- Salvando alterações 

criar uma pasta para iniciar
mkdir xxx  
cd xxx  
git init  
git status  
readme.so  
git satus  

- Para inicializar um diretório qualquer em um repositório git-hub é preciso digitar o comando:

git init

verificar se o repositório foi inicializado 
cd .git
ls
cat config

3 - Criando e Clonando Repositórios

Para clonar um repositório git, copiar o URL do repositório no gitHub
e digitar:  
git clone URL  
cd DIRETÓRIO  
cd .git  
cat config  

- Comandos básicos do Git

Para vincular um repositório local com um gitHub tem que digitar

git remote add origin URL do repositório do gitHub

se observar então o cat config do .git vai mostrar que o diretório já está vinculado com o gitHub

se quiser clonar um repositório git,  
digitar: git clone URL (isso clona uma pasta do gitHub no diretório atual)

se quiser clonar um repositório git em uma pasta com nome diferente, digitar:

git clone URL [nome da pasta]


Podemos clonar somente uma branch especifica de um repositório 


git clone URL --brach [nome da branch]


4 - Salvando Alerações em Repositório Local

mkdir resumos  
cd resumos  
git init  
git status (mostra status da área de trabalho e de preparação)  
toutch README.md  
git status
(mostra arquivos não rastreados)  
markdow forma simples de escrever html  
readme.so para escrever um readme

- Editar um título
colocar uma descrição
(git /Hub )
- Inserir um link
abre colchetes [texto] + (link)

- inserir subtitulo
(##) 

btn windows + . para abrir menu


usar o traço (-) para inserir butlist
ex:
- [Documentação](https//git-scm.com/doc)

Fazer tabela
## | Aulas | Resumos|
   |-------|--------|
   | Gravando Alterações no Repositório Local | [Resumos](link para aula) |

Para inserir trecho de códigos
"""
 digitar o código aqui!

"""

Feito isso, copiar o arquivo digitado e colar o readme.md

git status

- SITUAÇÕES QUE POSSAM OCORRER


mkdir resumos  
touch resumos/aula.md  
git status  
Ignorar o arquivo  
echo resumos/ > .gitignore  
voltar

echo > .gitignore  
Obs: 
Existem ocasiões em que você encontre algum touch aulas/.gitkeep
(projetos em que git reconheça diretórios vazios)

ADICIONANDO OS ARQUIVOS NA AREA DE PREPARAÇÃO

git add .

git commit -m"breve descriao sobre o commit"

git log

- DESFAZENDO ALTERAÇÕES EM UM REPO LOCAL  
Caso tenha iniciado um repositorio git em pasta local 

remover o diretório .git  
rm -rf (recursivamente a força) .git  
rm -rf .git

- RESTAURAR ARQUIVOS EM NOSSA ARVORE
Atenção (ter certeza)
 
git restore [nome do arquivo]

ALTERAR MENSAGENS DO ULTIMO COMMIT

forma 1
git commit --amend -m"adiciona gitignore e diretóriso aulas e resumos"

forma 2
ou git commit --amend (abre o editor e altera) esq : para siar 

git log 

desfazer um commit

git reset 
  - soft git reset --soft
     git reset --soft [hash]
  
- git reset --mixed (pedrão git reset) 
  server para mixed volta os arquivos      comitados anteriormente para a area de preparaçao 

git reset --hard + [hash] 
(ignora totalmenteo os arquivos do cmmit anterior)

git reflog

para tirar arquivos da area de preparacao

git add .

(já foi para a area de preparação)

git reset nome do arquivo

ou 

git restore --staged [nome do arquivo]

- ENVIANDO ALTERAÇÕES PARA REPOSITÓRIO REMOTO

Depois de conectar a local com remoto
git remote add origin http...

Fazer:

git push -u origin master

- PARA ATUALIZAR O REPOSITÓRIO LOCAL COM ATUALIZAÇÕES REALIZADAS NO REPO REMOTO

git pull


- TRABALHANDO COM BRANCHES

É uma ramificação do projeto
um ponteiro para um commit do histórico do repositório

Para criar uma branch teste

git checkout -b teste

retornando para branch main

git checkout main

Listando último commit de cada branch

para confirmar as alterações na branch principal 

git merge teste


listando as branches existentes

git branch

para excluir uma branch   

git branch -d teste

- CONFLITOS QUE POSSAM ACONTECER
EM BRANCHES

Cenário  
git push remote origin main 
Erro!!

git pull (retorna as alterações com conflito)

decidir qual alteração e indicar para o git

altera salva 

git status

git add .
git commit -m "comita após conflito"

git push origin main

enviado


- COMANDOS UTEIS

para baixar alterações da branch remota sem mesclar com a brach local

git fetch origin main

git diff main origin/main

git merge origin/main

CLONAR REPOSITÓRIOS (BRANCHES ESPECÍFICAS)

git clone URL --branch [teste] --single-branch

IMAGINANDO "Estou trabalhando na branch teste fiz modificações"
git status 

preciso criar uma nova branch sem levar as alterações para a branch 

git stash
git stash list


voltando para a branch teste

git checkout teste
git stash list

para trazer alterações feitas na nova brech 


git stash pop 
(trezer alterações para teste e remove alterações mais recente dessa pilha)
 

ou 

git stash apply 
(mantém alterações na lista para uso posterior)

Elidiana Andrade


https://github.com/elidianaandrade/dio-curso-git-github
