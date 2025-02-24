# Desafio Git e GitHub
## Desafio de contribuição de repositório Open-Source pelo GitHub
Olá, meu nome é Leandro Oliota e esse é o link do repoositório [Ecessar o link](https://github.com/leandrooliota/dio-lab-open-source)

## 😁 Abaixo segue algumas anotações que podem ajudar!
<details>

<summary>Minhas anotações iniciais de Git e Github no Git Bash</summary>

### Pode ver como anotei alguns comandos e comentários

GIT e GITHUB
//procurar uma pasta para ser a pasta local de reposição de diretórios
Criar uma pasta de reposição
$ mkdir repo-local

$ git init
//para inicializar um repositório git (essa pasta local ganha o arquivo oculto .git e está pronta para se comunicar com a pasta remota


//clocando um repositório do remoto
$ git clone URL.do.repositório


//dar um $ cat config           dentro do .git do diretório mostra as configurações

//para saber quais link remotos estão conectados
$ git remote -v

//adicionar o local com o remoto
$ git remote add origin URL.do.repositório

//para limpar a tela
$ clear
Ou CTRL+L

//Inicialize um repositório Git no diretório escolhido: 
$ git init

//Dando o comando abaixo eu removo a força uma pasta de um “diretório escolhido”
$ rm – rf .git
//Deixando a pasta de ser um repositório git

//Para verificar basta dar o comando 
$ git status

//Para entrar em uma pasta
$ cd nome.da.pasta/

//Para voltar
$ cd ..
//Restaurar um arquivo modificado (voltar atrás na modificação)
$ git restore nome.exato.do.arquivo
Ex. $ git restore README.md

//Depois posso confirmar com 
$ git status

//Ver o histórico dos nossos commits
$ git log

//Corrigir essa mensagem (escrever a nova mensagem dentro do parêntese)
$ git commit –amend -m”adiciona gitignore e diretórios aaulas e resumos”

//outra forma
$ git commit –amend
Vai entrar no editor
i (para editar)
apertar ESC sair da edição
:wq (sair do editor de commit)

$ git log
// para rever novamente os commits e ver se foi alterado

Para restaurar um commit inicial
$ git reset --soft (colar o código do commit inicial)
//1) Como criar um commit:
1 Adicione o conteúdo que deseja inserir no commit: 
$ git add .
2 Crie um commit e adicione uma mensagem descritiva: $ git commit -m "message"

// git reset --mixed (é o comportamento padrão)
$ git reset --mixed (colar o rest do ultimo commit – igual em cima)
//vou adicionar novo comentário 
$ git add .

Depois
$ git commit -m”mixed”
//basicamente tem que fazer uma mudança e adicionar um comentário

$ git reset --hard (código do commit)
// vai ignorar todos os arquivos anteriores e desfez ele(apagou tudo)

Histórico detalhado (mostra todos os commit em histórico)
$ git reflog

//para criar diretório mkdir + nome do diretório
$ mkdir resumos
//inserir arquivos touch + nome dos arquivos
$ touch resumos/aula-01.md resumos/aula-02.md

$ git add . 
//adicionar os arquivos para area de preparação

$ git reset (nome do arquivos específico)
$ git reset resumos/aula-01.md
//tirou os arquivos da area de preparação

$ git restore –staged resumos/aula-02.md
//removeu de outra forma os arquivos da área de preparação


git remote add origin https://github.com/leandrooliota/dio-resumos-git-e-github.git

enviando do local para o remoto
$ git push -u origin main


Dentro do repositório para abrir o editor WEB usa o atalho clicando na tecla .
.

Como trazer do remoto para o local
AAAAAAAAA para fazer o git pull eu tenho que está dentro da pasta de origem (origin) a pasto do backup, ou a pasta que clonei
No meu caso a pasta “iniciando” dentro da pasta REPO-LOCAL do drive
Mas o pull é feito dentro da pasta clonada ou baixada, no local para o remoto
$ git pull


Passo 1
$ echo “commit-1-branch-main” > commit-1-branch-main.txt
//vai adicionar um comentário e um arquivo
Esse comando no Git Bash cria um arquivo de texto chamado commit-1-branch-main.txt e escreve dentro dele o texto "commit-1-branch-main". Vamos quebrar isso em partes:
•	echo: É um comando utilizado para imprimir texto no terminal.
•	"commit-1-branch-main": É o texto que será impresso.
•	> commit-1-branch-main.txt: É um redirecionamento que pega a saída do comando echo (que seria apenas imprimir o texto no terminal) e a direciona para um arquivo chamado commit-1-branch-main.txt, criando-o se ele ainda não existir ou sobrescrevendo seu conteúdo se já existir.
Portanto, após executar esse comando no Git Bash, você terá um arquivo de texto chamado commit-1-branch-main.txt com o conteúdo "commit-1-branch-main".

Passo 2
$ git add .

O comando:

git add .
significa "adicionar todas as alterações na área de staging". Vamos entender melhor:
Quebra do comando:
•	git add → Adiciona arquivos ao staging area (área de preparação para commit).
•	. → Significa "todos os arquivos no diretório atual e subdiretórios".
O que acontece ao rodar esse comando?
•	Se você criou um novo arquivo (commit-1-branch-main.txt no seu caso), ele será adicionado ao controle do Git.
•	Se você modificou algum arquivo já existente, essa modificação será incluída no staging.
•	Se você excluiu arquivos, essa remoção também será preparada para commit.
Depois de git add ., os arquivos não foram salvos definitivamente no repositório, apenas preparados para o commit. Para salvar as alterações no histórico do Git, o próximo passo é usar:
bash
CopyEdit
git commit -m "Mensagem explicando a alteração"
Se precisar de mais detalhes, me avise! 🚀

Passo 3
Próximo passo é o 
$ git commit -m ”Mensagem explicando a alteração”


Adicionando uma Branch teste
$ git checkout -b teste
O comando:
bash
CopyEdit
git checkout -b teste
faz duas coisas ao mesmo tempo:
1.	Cria uma nova branch chamada teste.
2.	Faz o checkout (ou seja, muda para essa nova branch imediatamente).
Portanto, após executar esse comando, você estará trabalhando na branch teste. Se desejar voltar para outra branch, pode usar o comando git checkout nome-da-branch.


•	Voltar para o Branch main
$git checkout main
// os comandos que foram criados na teste não estarão aqui na main

$ git Branch -v
//vai listar o último commit de cada Branch

•	MESCLANDO AS BRANCHS

$git merge nome.da.branch
$git merge teste
//no nosso caso a Branch teste

•	Excluir a Branch teste
$ git Branch -d teste

```ruby
   puts "Leandro Oliota"
```

</details>

Editando o commit para o padrão de atividade
feat: add leandrooliota profile
