# Comandos Mais Utilizados no Git

Git é uma ferramenta essencial para desenvolvedores, permitindo controle de versão e colaboração eficiente.
Aqui estão alguns dos comandos mais utilizados no Git, explicados de forma amigável e simplista:

## `git init`
Inicializa um novo repositório Git no diretório atual. 
Cria um diretório oculto `.git` que contém todos os arquivos necessários para o repositório.


## `git clone`
Clona um repositório existente de um servidor remoto para o seu computador local.
Útil para começar a trabalhar com um projeto já existente.
git clone <url-do-repositório> 


## `git add`
Adiciona mudanças no diretório de trabalho ao índice (staging area). Isso prepara os arquivos para o próximo commit.



## `git add <nome-do-arquivo>`
Para adicionar todos os arquivos modificados:
git add .

## `git commit`
Grava as mudanças adicionadas ao índice no repositório.
É aqui que você salva o estado atual do seu código com uma mensagem descritiva.
git commit -m "Mensagem do commit"

## `git status`
Mostra o status dos arquivos no diretório de trabalho e no índice,
indicando quais arquivos foram modificados, quais estão no índice, etc.
git status


## `git push`
Envia os commits do seu repositório local para um repositório remoto. 
Isso compartilha suas mudanças com outros colaboradores.
git push <nome-remoto> <nome-branch>


## `git pull`
Atualiza o repositório local com as mudanças do repositório remoto.
 Isso faz fetch e merge das mudanças.
git pull

## `git branch`
Lista, cria ou deleta branches.
Branches permitem que você trabalhe em diferentes funcionalidades de forma isolada,
sem precisar correr o risco de efetuar alterações no código principal sem os devidos 
testes. 

Para listar todas as branches:


## `git branch`
Para criar uma nova branch:
git branch <nome-da-branch>


## `Para deletar uma branch:`
git branch -d <nome-da-branch>

## `git checkout`
Muda para uma branch específica ou restaura arquivos do índice ou do commit.
Para mudar para uma branch:
git checkout <nome-da-branch>


## `Para criar e mudar para uma nova branch:`
git checkout -b <nome-da-nova-branch>

## `git merge`
Funde uma branch com outra.
Geralmente, você estará na branch principal (por exemplo, main) 
e fundirá as mudanças de uma branch de funcionalidade.
git merge <nome-da-branch>

> **Sou programadora e atualmente trabalho como Data Engineer Junior na AB-Inbev. Acredito que aprendizado é um processo contínuo e estou sempre buscando novas formas de aprender e reforçar meus conhecimentos.**
