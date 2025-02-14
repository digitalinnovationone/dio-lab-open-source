
# Contribuição de Projeto passo a passo

Passo a passo para melhor compreesão do que deve e como ser feito, faça bom proveito.


1 Clone o Repositório Localmente:
No seu fork do repositório, clique no botão "Code" e copie o URL.

2 No seu ambiente de desenvolvimento, abra um terminal e execute o comando abaixo, substituindo pelo seu nome de usuário no GitHub:
git clone https://github.com//dio-lab-open-source.git

3 Adicionando um Remote "Upstream":
Para manter seu repositório local atualizado com o repositório original, adicione um remote chamado "upstream" com o seguinte comando:
git remote add upstream https://github.com/elidianaandrade/dio-lab-open-source.git

4 Mantendo seu Fork Atualizado:
Periodicamente, para obter as alterações mais recentes do repositório original, execute o seguinte comando:
git pull upstream main

5 Criando uma Nova Branch para Sua Contribuição:
Antes de fazer qualquer alteração, crie uma nova branch com um nome descritivo para sua contribuição. Por exemplo:
git checkout -b feat/community/SEU_USERNAME

6 Desenvolvendo sua Contribuição:
Siga as orientações no guia para desenvolver sua contribuição. No caso de adicionar um perfil na pasta "community," crie um arquivo Markdown com o mesmo nome do seu nome de usuário no GitHub, e personalize seu perfil.

7 Adicionando suas Alterações à "Staging Area":
Use o comando git add para adicionar as alterações que você deseja incluir em seu próximo commit. Por exemplo:
git add community/SEU_USERNAME.md

8 Criando um Commit com uma Mensagem Descritiva:
Use o comando git commit para criar um commit com uma mensagem clara e informativa. Siga a convenção de commits do projeto, como "feat" para adicionar uma nova funcionalidade. Por exemplo:
git commit -m "feat: adicionar perfil de SEU_USERNAME"

9 Enviando suas Alterações para o Repositório Remoto:
Use o comando git push para enviar suas alterações para o seu repositório remoto no GitHub. Por exemplo:
git push origin feat/community/SEU_USERNAME


## Referência

 -https://github.com/digitalinnovationone/dio-lab-open-source/issues/15857

## 🚀 Sobre mim
Eu sou uma pessoa desenvolvedora full-stack...

