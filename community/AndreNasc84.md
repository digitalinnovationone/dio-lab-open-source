
# Contribuindo em um Projeto Open Source

A seguir, a descrição de cada passos realização na atividade de contribuição ao projeto Open Source com base nas orientações da mentora Elidiana.

#Passo 01:# Acessei o repositório digitalinnovationone/dio-lab-open-source, para efetuar o processo FORK do projeto dio-lab-open-source.

#Passo 02:# No console do git, efetuei o clone do meu repositorio.
$ git clone https://github.com/andrenas84/dio-lab-open-source.git
Cloning into 'dio-lab-open-source'...
remote: Enumerating objects: 228949, done.
remote: Counting objects: 100% (31758/31758), done.
remote: Compressing objects: 100% (85/85), done.
remote: Total 228949 (delta 31723), reused 31688 (delta 31673), pack-reused 197191 (from 1)
Receiving objects: 100% (228949/228949), 987.19 MiB | 3.52 MiB/s, done.
Resolving deltas: 100% (139372/139372), done.
Updating files: 100% (28101/28101), done.

#Passo 03:# Acessei o repositório local clonado.
cd dio-lab-open-source/

repo/dio-lab-open-source (main)
$ git pull
Already up to date.

#Passo 04:# Efetuei o camando abaixo para manter meu repositório local atualizado 
git remote add upstream https://github.com/digitalinnovationone/dio-lab-open-source.git

Observação: Para atualizar (e mesclar) o meu repositório local com base nas novas atualizações do projeto no repositório de origem, devo efetuar o seguinte comando: git pull upstream main
Para atualizar apenas, sem mesclar, utilizo o seguinte comando: git fetch upstream main

#Passo 05:# Verifiquei se realmente o meu comando de manter repositorio atualizado fez efeito.
git remote -v
origin  https://github.com/AndreNas84/dio-lab-open-source.git (fetch)
origin  https://github.com/AndreNas84/dio-lab-open-source.git (push)
upstream        https://github.com/digitalinnovationone/dio-lab-open-source.git (fetch)
upstream        https://github.com/digitalinnovationone/dio-lab-open-source.git (push)

#Passo 06:# Criei uma branch já com checkout na mesma.
git checkout -b feat/community/andrenas84
Switched to a new branch 'feat/community/andrenas84'

#Passo 07:# Acessei a pasta community e criei um arquivo .md 
cd community/

touch community/andrenas84.md

#Passo 08:# Editei o arquivo criado. Este aqui rs...

#Passo 09:# Renomei o meu arquivo como mesmo nome do meu user: andrenas84

#Passo 10:# Adicionei as alterações na staging area com o comando
git add community/andrenas84.md
