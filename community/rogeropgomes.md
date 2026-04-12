
# DIO - RESUMOS GIT E GITHUB
Repositórios para armazernar resumos GIT e GITHUB do BootCamp da Suzano na 
[DIO](https://web.dio.me/course/406684a4-396d-4160-94b9-ead934e18564/learning/599dd3dd-d189-474f-a55c-22f37b4472da?autoplay=1&back=%2Ftrack%2Fsuzano-python-developer&moduleId=undefined&tab=forum)


## 😁 Documentação (win+. abre menu de emoji no markdown)
## 🖥️ Resumos das Aulas

| Aulas | Resumos |
| ----- | ------- |
| Gravando Alterações no Repositório Local |
| Para Criar Tabelas como esta usar "alt 124" | Barra reta é feita com alt+124 |

# 💽 Comandos Git e GitHub
| Lista de comandos | Função | 
| ----------------- | ------ |
| mkdir "títuto" | cria o repositório com esse título |
| touch "nome da pasta" | cria um arquivo vazio na pasta |
| cd "caminho" | entra com o git bash na pasta do caminho selecionado |
| git init | inicia o git no repositório criado |
| git status | mostra os status da arvore e da área de preparação |
| git add | adiciona a área de preparação |
| touch README.md | cria um arquivo READMe tipo markdown |
| untracked files | arquivos não rastreados, ou seja que não estão nos comits anteriores ou na área de preparação |
| ctrl + l | limpa 
| git add README.md | adiciona o arquivo à áre ade preparação |
| git commit -m "commit inicial" | executa o commit e o nomeia com o texto |
| git log | ve os registros de alteração comitadas |
| git remote add upstream "link do repositorio" | conecta o repositório local com a branch a ser realizado o pull request para que seja mantido atualizado sempre o repositorio local atraves do git remoto dele |
| git remote -v | ve as conexões que fizemos no repositorio local |
| git pull upstream main | atualiza na main as ultimas alteração do repositorio remoto no repositorio local |
| git checkout -b feat/community/rogeropgomes | cria uma nova pasta no repositório local |


# Situação de tentar salvar um diretório vazio

| mkdir resumos | cria um diretorio vazio |
| ------------- | ----------------------- |
| git status | retorna que não há nada para realizar commit |
| echo resumos/ > .gitignore | faz o git ignorar a pasta resumos do arquivo |
| echo | ver o que faz |
| touch nome/.gitkeep | é uma convenção para o git reconhecer arquivos vazios |

