# Git

O Git é um sistema de controle de versão distribuído, o que significa que um clone local do projeto é um repositório de controle de versão completo. Esses repositórios locais totalmente funcionais facilitam o trabalho offline ou remotamente. Os desenvolvedores confirmam seu trabalho localmente e, em seguida, sincronizam sua cópia do repositório com a cópia no servidor. Esse paradigma é diferente do controle de versão centralizado, no qual os clientes devem sincronizar o código com um servidor antes de criar novas versões do código.



## Comandos Básicos
> Configurar do nome de usuário e mail
-  `$ git config user.email email`
- `$ git config user.name "nome de usuario"`
  

## 📚 Comandos Básicos



### git init
este comando dá origem a um repositório novo, local ou remoto, ou reinicializa um repositório já existente;
  - Criando Repositório Local
    - `$ git init`

  - Iniciando um repositório  ou criando um repositório com um nome em específico
    - `$ git init <O nome do seu repositório>`

 ### git clone
cria uma cópia exata de um repositório já existente.
  - `$git clone <URL do seu projeto>`

 ### git commit
este comando move os arquivos da state area para um repositório local
   - `$git commit -m “seu comentário”`

 ### git add
este comando adiciona um arquivo alterado a uma staging area, ou seja, o prepara para ser vinculado a um commit

   - adicionar o arquivo em específico ao repositório
      - `$ git add arquivo`

   - adicionar todos os arquivos novos e/ou modificados ao repositório
      - `$ git add *`

 ### git Push
envia arquivos de um repositório local para um repositório remoto
     
   - `$ git push REMOTE-NAME BRANCH-NAME`

 ### git Pull
 traz um arquivo do repositório remoto para o repositório local
   
  - `$ git pull <endereço> *`

 ### git Merge
 serve para unir arquivos alterados ao arquivo original de um projeto
     
- `$ git merge <nome_do_branch> *`



### Referências
https://learn.microsoft.com/pt-br/devops/develop/git/what-is-git
https://www.codigofonte.com.br/artigos/top-25-comandos-do-git
https://kenzie.com.br/blog/o-que-e-git/