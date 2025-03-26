# Principais Comandos do Git

## Configuração Inicial

- `git config --global user.name "seu nome"`: Define o nome do usuário.
- `git config --global user.email "seu email"`: Define o email do usuário.

## Criando um Repositório

- `git init`: Inicializa um novo repositório Git na pasta atual.
- `git clone url_do_repositório`: Clona um repositório remoto.

## Trabalhando com Arquivos e Commits

- `git status`: Mostra o estado atual do repositório, incluindo quaisquer alterações não confirmadas.
- `git add nome_do_arquivo`: Adiciona um arquivo ao próximo commit.
- `git commit -m "mensagem do commit"`: Cria um novo commit com as alterações adicionadas.
- `git log`: Mostra o histórico de commits.

## Trabalhando com Branches

- `git branch`: Lista todas as branches do repositório.
- `git branch nome_da_branch`: Cria uma nova branch.
- `git checkout nome_da_branch`: Muda para a branch especificada.
- `git merge nome_da_branch`: Mescla a branch especificada na branch atual.

## Trabalhando com Repositórios Remotos

- `git remote add origin url_do_repositório`: Adiciona um repositório remoto.
- `git push origin nome_da_branch`: Envia as alterações para o repositório remoto.
- `git pull origin nome_da_branch`: Recebe as alterações do repositório remoto.
