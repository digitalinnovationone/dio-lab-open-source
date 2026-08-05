# Contribuindo para o Repositório Open Source

Sou Victor Barbosa de Freitas. Abaixo, exemplifico o passo a passo para contribuir com o repositório. Para me conhecer melhor, minhas redes sociais estão listadas abaixo.

[Instagram](https://www.instagram.com/victor12_freitas/) | [Github](https://github.com/VictorBaFreitas) | [LinkedIn](https://www.linkedin.com/in/victor-freitas-b64089240/)

Estou assumindo que você já realizou as configurações iniciais, como criar um token ou chave SSH para controle do repositório remoto, além das configurações primárias para registrar seu e-mail e nome no terminal local.

[Configuração Inicial](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Configura%C3%A7%C3%A3o-Inicial-do-Git) | [Criar Token ou Chave SSH](https://www.dio.me/articles/autenticando-token-chave-ssh)

## Passo a Passo:

### 1. Fazer Fork do Repositório

* No GitHub, dentro do repositório do lab, clique em "Fork". Adicione um nome para o seu repositório local e uma descrição, se necessário.
* Agora, dentro do seu repositório, clique em "Code" e copie um dos métodos para clonar o repositório na máquina local.

### 2. Clonar o Repositório

**Terminal:**

* Abra o seu terminal e execute o comando copiado. Não se esqueça de substituir "SeuUsuário" se estiver usando o meu comando.
* Os comandos abaixo permitem clonar o repositório e mantê-lo atualizado com o repositório original.

```
git clone https://github.com/SeuUsuário/dio-lab-open-source.git
git remote add upstream https://github.com/SeuUsuário/dio-lab-open-source.git
git pull upstream main
```

### 3. Criar uma Branch

* Para enviar sua contribuição, seja uma alteração ou um novo arquivo, é necessário criar uma nova branch.
* Após clonar o repositório, marque o caminho atual e o diretório em que você está e execute os comandos abaixo, substituindo "SeuUsuário" e "NomeDoSeuRepositório" (o padrão será `dio-lab-open-source`).

```
cd NomeDoSeuRepositório
git checkout -b feat/community/SeuUsuário
cd community/
```

### 4. Incrementar Atualizações

* Após alterar ou adicionar um arquivo, você deve enviar sua contribuição. Certifique-se de que o arquivo esteja dentro do diretório `community` e na sua branch criada. Utilize os comandos `pwd` e `git branch` para verificar.

* Após a verificação, envie as alterações para o repositório e crie uma PR (Pull Request). Não se esqueça de substituir "NomeDoSeuArquivo" e "SeuUsuário".

```
pwd
git branch
git add NomeDoSeuArquivo
git push origin feat/community/SeuUsuário
```

### 5. Criar Pull Request

* No site do GitHub, no seu repositório, aparecerá a opção para criar uma Pull Request para mesclar as novas alterações com a branch `main`. Adicione um comentário relevante sobre suas alterações e pronto! Apenas aguarde a aprovação. Sua contribuição estará feita!

---

# Contributing to the Open Source Repository

I'm Victor Barbosa de Freitas. Below, I’ll outline the steps to contribute to the repository. To get to know me better, my social media links are listed below.

[Instagram](https://www.instagram.com/victor12_freitas/) | [Github](https://github.com/VictorBaFreitas) | [LinkedIn](https://www.linkedin.com/in/victor-freitas-b64089240/)

I’m assuming that you have already completed the initial setup, such as creating a token or SSH key for remote repository control, as well as the primary configuration for registering your email and name in your local terminal.

[Initial Setup](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Configura%C3%A7%C3%A3o-Inicial-do-Git) | [Create Token or SSH Key](https://www.dio.me/articles/autenticando-token-chave-ssh)

## Step-by-Step:

### 1. Fork the Repository

* On GitHub, within the lab repository, click on "Fork". Add a name for your local repository and a description if needed.
* Now, inside your repository, click on "Code" and copy one of the methods to clone the repository to your local machine.

### 2. Clone the Repository

**Terminal:**

* Open your terminal and execute the copied command. Be sure to replace "SeuUsuário" if you are using my command.
* The commands below allow you to clone the repository and keep it updated with the original repository.

```
git clone https://github.com/YourUsername/dio-lab-open-source.git
git remote add upstream https://github.com/YourUsername/dio-lab-open-source.git
git pull upstream main
```

### 3. Create a Branch

* To submit your contribution, whether it's a change or a new file, you need to create a new branch.
* After cloning the repository, note the current path and directory you are in and execute the commands below, replacing "YourUsername" and "YourRepositoryName" (the default will be `dio-lab-open-source`).

```
cd YourRepositoryName
git checkout -b feat/community/YourUsername
cd community/
```

### 4. Commit Updates

* After making changes or adding a file, you should send your contribution. Ensure that the file is within the `community` directory and in your created branch. Use the `pwd` and `git branch` commands to verify.

* After verification, push the changes to the repository and create a PR (Pull Request). Be sure to replace "YourFileName" and "YourUsername".

```
pwd
git branch
git add YourFileName
git push origin feat/community/YourUsername
```

### 5. Create a Pull Request

* On the GitHub website, in your repository, you’ll see an option to create a Pull Request to merge the new changes with the `main` branch. Add a relevant comment about your changes, and that's it! Just wait for approval. Your contribution will be complete!

---

