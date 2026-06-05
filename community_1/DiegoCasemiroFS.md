# Colinha de Git

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/diego-casemiro-00b83823a/)

... o Git é uma ferramenta de versionamento de código, isso serve para realizar o desenvolvimento de código em equipe e é muito útil em varios aspectos, 
vamos explorar cada um deles em cada ponto citado ao longo da planilha ...

## 1. Quando você quiser iniciar uma Api

```bash
git init                         # Inicializa um repositório Git
git add README.md                # Adiciona um README, onde ficam as especificações do projeto
git commit -m "first commit"     # Comenta as alterações feitas na API
git branch -M main               # Define o nome da branch principal como "main"
git remote add origin https://github.com/seu-usuario-GitHub/nome-da-api.git     # Faz o link do repositório local com o remoto
git push -u origin main          # Envia as alterações feitas localmente para o repositório remoto
```

## 2. Caso a Api ja esteja em processo de desenvolvimento e você queira adiociona-la ao Git

```bash
git remote add origin https://github.com/seu-usuario-GitHub/nome-da-api.git     # Faz o link do repositório local com o remoto
git branch -M main               # Define o nome da branch principal como "main"
git push -u origin main          # Envia as alterações feitas localmente para o repositório remoto
```

... agora você pode acessar uma API ou disponibilizar a sua propria no GitHub, uma utilidade que podemos explorar desde já é o uso dos commits ...  

... cada commit é uma memória do que foi feito até aquele momento na API, então, além de você possuir um histórico da sua API, você pode acessar as versões 
do seu código e retornar em qualquer uma delas caso queira recomeçar, como diz o filósofo Belo ...

obs: é sempre bom utilizar o "git status" para verificar o status da api

... num ambiente de desenvolvimento onde vários devs estão fazendo varias alterações na mesma API, é quase que obrigatório que cada dev faça as suas alterações
 na sua branch, depois disso ele devolve as alterações que ele fez pra branch principal (main), para isso seguiremos o seguinte passo a passo...

## 3. Caso você queira trocar de Branch para alterações na Api

```bash
git checkout "nome-da-sua-branch"     # Altera para a branch desejada
```

... é importante entender que a branch é como uma linha do tempo, e o nome dessa linha é "main", cada vez que você for fazer uma alteração da aplicação, você cria
uma nova "branch", que pode ser entendida como uma ramificação na nossa linha do tempo ...

![Texto Alternativo](https://www.iugu.com/hs-fs/hubfs/undefined-3-1.png?width=602&height=345&name=undefined-3-1.png)

## 4. Após as alterações serem feitas

```bash
git push set --upstream -origin "nome-da-sua-branch"     # Cria a branch no repositório remoto, caso ainda não tenha sido criada
git push                                                # Envia as alterações 
```

...e quando você quiser devolver as alterações feitas pra aplicação, essa nova branch, ou essa ramificação, encontra a nossa linha do tempo novamente ...

## 5. Caso eu queira acessar as alterações feitas por outro Dev

```bash
git merge "branch-de-outro-dev"     # Mistura as informações de outra branch com a branch local
```

## 6. Caso você queira atualizar o repositório local com as informações do remoto

```bash
git pull     # Pega as atualizações do repositório remoto e aplica no repositório local
```

... e quando você é contratado no meio do projeto, você precisa baixa-lo no seu pc pra começar a colaborar com o desenvolvimento dele ...

## 7. Caso você queira clonar um projeto já em andamento

```bash
git clone "url-do-projeto"
```

Lembre-se de usar `git status` para verificar o status do seu repositório.
