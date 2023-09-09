# Objetivo

Atender a demanda de um guia breve sobre os comandos básicos do terminal e do git.

## Comandos básicos do terminal

- mkdir: Cria uma pasta no diretório local
- cat >nome-do-arquivo.extensão: Cria arquivo de texto de forma rápida
- cat nome-do-arquivo.extensão: Exibe o conteúdo de um arquivo
- cat config: Mostra as configurações do diretório atual
- dir: Exibe os arquivos presentes no diretório
- ls: Lista os arquivos presentes no diretório, o mesmo que o "dir"
- cd: Retorna para o disco local
- cd /caminho/: Entra no caminho desejado
- rmdir <nome-do-diretório>: Remove a pasta ou diretório desejado
- touch nome-do-arquivo.extensão: Adiciona um arquivo no diretório atual (funcionalidade similar ao do "cat", mas possui suas peculariadades, caso queira saber mais, dê o comando touch --help)

## Comandos do git utilizados até então

*Os comandos listados aqui irão se limitar aos que foram usados ao decorrer do curso de "Versionamento de Código com Git e GitHub" & "Contribuindo em um Projeto Open Source no GitHub".*

- git init: Inicializa um repositório novo na pasta atual
- git clone URL "nome desejado": Clona um repositório existente
- git clone URL --branch "nome da branch" --single-branch: Clona somente uma ramificação (branch) do repositório desejado
- git remote add origin URL: Vincula uma ramificação ao repositório origem
- git status: Exibe as condições do diretório de trabalho, caso haja incoerências entre o repositório remoto e local, além de mostrar arquivos que não estão sendo monitorados pelo git
- git add: Adiciona os arquivos do repositório local para serem incluídos no próximo commit
- git add nome-do-arquivo: Adiciona determinado arquivo para ser incluído no próximo commit
- git commit -m"mensagem": Efetua uma atualizações com todas as alterações adicionadas até então, acompanhada de uma breve descrição do que se trata
- git commit --amend -m"mensagem" - Altera a descrição do último commit
- git --amend - Abre o editor, possibilitando alteração no próprio git
- git log: Exibe o histórico de commits
- rm -rf .git: Remove forçadamento um arquivo do monitoramento do git, logo não será mais incluso nos próximos commits
- git restore "nome-do-arquivo.extensão": Restaura a versão anterior do arquivo escolhido
- git reset --soft hash-do-commit: O repositório main passa a apontar para o commit escolhido, deixa todos os seus arquivos alterados como "Changes to be committe", no caso, o próximo commit irá incluí-los
- git reset --mixed hash-do-commit: O repositório main passa a apontar para o commit escolhido, o próximo commit não irá incluir o que foi resetado, além de não reconhecê-lo como monitorado pelo git
- git reset --hard hash-do-commit: O repositório main passa a apontar para o commit escolhido, além de descartar todos os commits posteriores ao desejado
- git reflog: Histórico de commits mais rebuscado
- git push -u origin main: Envia as alterações do repositório local para o remoto
- git pull: Busca e baixa novos conteúdos do repositório remoto par o local
- git checkout -b "nome": Cria uma nova branch no repositório local
- git branch -v: Lista os últimos commits em cada branch
- git merge "nome-da-branch-desejada": Mescla duas branchs
- git branch -d "nome-da-branch-desejada": Deleta a branch desejada
- git fetch: Verifica se há mudanças no repositório alvo
- git stash: Salva alterações locais e reverte o diretório para coincidir ao commit principal
- git stash list: Lista modificações que foram arquivadas
- git stash apply: Aplica as modificações arquivadas
- git remote add upstream URL: Espelha o repositório remoto ao local
- git fetch upstream: Verifica se há mudanças no repositório remoto

*Este documento está aberto a modificações visto que há a possibilidade de erros, afinal assim como os senhores leitores, também estou aprendendo.*

Em resposta aos Issues de número #4633, #4648, #3151, #3113

## Referências 

- [Atlassian](https://www.atlassian.com/br/git/tutorials)
- [Documentação Git](https://git-scm.com)