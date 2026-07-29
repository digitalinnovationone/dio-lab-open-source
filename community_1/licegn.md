
# DIO | Laboratório de contribuição a um projeto open source

Revisando comandos do git na prática.
[Digital Inovation One](https://web.dio.me/track/santander-bootcamp-2023-fullstack-java-angular)

## Alice Gonçalves do Nascimento

Olá, tenho 22 anos, moro em Brasília/DF e busco retomar meus estudos como desenvolvedora. 
Concluí o técnico de informática e ingressei em Engenharia de Software na Universidade de Brasília, mas por circunstâncias de trabalho precisei trancar, atualmente estou finalizando um tecnólogo em Redes de computadores e trabalhando como Auxiliar Administrativo.
Trabalhei um ano e meio como help desk e depois evoluí para técnica nível 2 na mesma empresa, atuando diretamente com o cliente por mais dois anos. Nas minhas rotinas de trabalho pude aprender muito sobre a área de Gestão, me aprofundando em ferramentas como excel e power bi além é claro de valiosas lições sobre liderança, relações interpessoais e resolução de problemas. Conheci as rotinas de diversos clientes da empresa e cheguei a atuar como Supervisora substituta da equipe de técnicos N2.

## Conecte-se comigo

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=0E76A8)](https://www.linkedin.com/in/licegn/)

[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram)](https://www.instagram.com/_ctrlalice/)

## Habilidades

![HTML5](https://img.shields.io/badge/HTML5-000?style=for-the-badge&logo=html5)
![Markdown](https://img.shields.io/badge/Markdown-000?style=for-the-badge&logo=markdown)
![CSS3](https://img.shields.io/badge/CSS3-000?style=for-the-badge&logo=css3&logoColor=264CE4)

![JavaScript](https://img.shields.io/badge/JavaScript-000?style=for-the-badge&logo=javascript)
![Java](https://img.shields.io/badge/Java-000?style=for-the-badge&logo=java)
![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)
![C](https://img.shields.io/badge/C-000?style=for-the-badge&logo=c)

___________________________________________________________

## GitHub

# Git's Commands

This page is about some commands from Git. 

😁 You also can contribute!

## ⚙️ Settings Up Git

- Configure your email 
-  `$ git config user.email [your_mail_here]`
- Configure your user name 
- `$ git config user.name [your_user_here]`
  
If you want to config your scope of work use the tags below.

- Local scope 
  - `$ git config --local user.email [your_mail_here]`
- Global scope 
  - `$ git config --global user.email [your_mail_here]`
- System scope 
  - `$ git config --system user.email [your_mail_here]`

## 📚 Basics Commands

### Create a new repository
  - Create a local repository
    - `$ git init`
  - Clone a remote repository
    - `$ git clone [url_remote_origin]`
  - Clone only brachys repository
    - `$ git clone -branch [branch_name] [url_remote_origin]`
  - Clone into a specific repository
    - `$ git clone [url_remote_origin] [dir_name]`
  
### Create a new connection with the remote repository
- List remote repositories
  - `$ git remote`
- Create a new connection to remote repository on server
  - `$ git remote add [remote_name] [url_to_remote]`
- Remove a connection to remote repository
  - `$ git remote rm [remote_name]`
- Rename a remote connection
  - `$ git remote rename [remote_old_name] [remote_new_name]`

### Create a new commit
- Include files in stage area
  - `$ git add --all or -a or .` 
- Create a commit with message
  - `$ git commit -m "your message here"`
- Combine all in one commit
  - `$ git commit -a -m "your message here"`
- Change the message to commit
  - `$git commit -amend "new message here"`

________________________________________________________

## Minhas contribuições

git commit --amend -m"nova mensagem" **(alterar a mensagem de um commit)**

git init **(inicializar um reposítório)**

git push **(enviar alterações do repositório local para o remoto)**

git pull -> git fetch **(só baixa as alterações do remoto) + git merge (mescla as alterações remoto e local)**

git log **(mostra os commits)**

git diff **(mostrar diferenças entre branchs)**

git clone + URL --branch teste --single-branch **(clonar uma branch)**

git stash **(arquiva uma modificação)**

git stash list **(listar modificações arquivadas)**

git stash apply **(aplicar última arquivada)**

git checkout -b -nomedabranch **(sai da branch atual e cria uma nova)**

git checkout **(sair da branch atual)**

touch caminhopasta/arquivo.extenção **(criar um arquivo)**