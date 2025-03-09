##Dicas git


#o Git é uma ferramenta para versionar seus codigos. vamos imaginar que uma equipe esta trabalhando em um codigo e subindo sempre as alterações no drive,chega um ponto em que existem varias versoes de um mesmo codigo cada uma com diferentes alterações e vc ja nem sabe mais onde deve trabalhar em qual versao,e pra isso existe o git e o github, o github é como se fosse uma pagina para os seus codigos onde voce pode ver tudo o que foi feito nele desde o inicio,pequenas ou grandes alterações e tornando mais facil de trabalhar em equipe com um mesmo codigo,

o passo a passo do git resumido
`git-clone,git-commit,git-pull e git-push`

#GIT-CLONE :  Quando trabalhamos com um codigo que ja esta sendo versionado pelo git,precisamos dele localmente para fazemos as alterações e trabalhar em cima dele para isso usamos esse comando chamado git clone que ira criar uma copia da versão selecionada do codigo localmente permitindo que façamos as alterações que queremos

O comando git clone pode tem uma função onde podemos mudar o nome que queremos no nosso clone antes do git fazer essa clonagem por exemplo
`git clone https://github.com/FabricioMoraes36/New_.git Novo-Repo`
O clone que se chama new_git agora se chamara Novo-Repo

#GIT COMMIT: essa palavra é muito usada no meio dev, os commits sao as alterações que fizemos no codigo,sao as versoes que estamos criando para aquele mesmo codigo que clonamos anteriormente,mas antes de fazer o commit precisar ver se n tem ninguem trabalhando naquela mesma versão pra nao dar merda e pra isso usamos o comando git pull,ele vai puxar as ultimas alterações e mescla com o seu arquivo

primeiro queremos adicionar nosso arquivo ao nosso repositorio e usamos por exemplo:

`git.add README.md`

apos adicionarmos para salvar esse commit usaremos

`git commit -m"Meu primeiro commit"`

o -m e as "" servem para escrevermos o que foi feito nessa alteração como por exemplo se mudasse uma função no codigo escreveriamos isso no nosso commit

com `git log` podemos ver os nossos commits como nesse exemplo apareceria assim: 

commit xxxxxxxxxx8956b3bb746915d4663cf708e1b848
Author: xxxxxxxxx.xxxxxxxxxxx.xxxxxxxxxxx.xxxxxxxxx
Date:   Sat xx x xx:xx:x xxx -xxx

    commit inicial

com o nome de usuario que setamos no git, o email,data e tal e abaixo o nosso comentario sobre esse commit

caso uma alteração fosse feita nesse readme que estamos usando de exemplo,uma alteração direta pelo bloco de notas e usassemos o `git status` ele ja apresentaria o erro do arquivo, mas se desfizermos a alteração e usar o `git status` mais uma vez ele vai reconhecer que o arquivo esta igual ao do ultimo commit feito


#GIT PUSH : É onde voce finalmente sobe seu codigo no git

#CONFIGURAÇÕES DO GIT

Para inserir seu nome e email para todos os seus repositorios no git vc abre a bash apos instalar o git e usa os comandos:

`git config --global user.name fulano
`git config --global user.email fulano@gmail.com`

isso ira setar seu nome e email e eles irao aparecer nos seus commits lembrando que se vc alterar isso depois a mudança nao sera aplicada a repositorios com nome de usuario ou emails antigos,usamos o termo global pra aplicar para tudo e nao so localmente nao so pra um projeto em especifico e tal

`Ctrl + L` limpa o terminal da bash pra n ficar confuso

git config  init.defaultBranch - este comando ira mostrar a branch principal do seu git ela pode vir como master mas o correto é alterar para main pq hoje em dia é mais usado e tal,usando o comando :

`git config init.defaultBranch main`

isso ira alterar o nome da sua branch e deixando em um padrão ali

para ver as suas configurações gerais do git use o comando: 

`git config --global --list`


#CRIANDO UM REPOSITORIO LOCAL

usando a git bash na pasta em que deseja colocar seu repositorio use o comando :

`mkdir repo-local`

isso criara uma pasta nova que sera nosso repositorio

para entrar nessa pasta utilize o comando: `cd repo-local/` E apos isso use o comando `git init` que transformara em um repositorio

Para vincular um repositorio local com um remoto usamos o comando:
`git remote add origin https://github.com/FabricioMoraes36/Teste1.git`
Origin é um nome padrao e é recomendado deixar assim
se usar o comando: 
`cd .git` para entrar na pasta .git e depois `cat config` para exibir a config da mesma voce ira notar que o git mostra o repositorio remoto que esta vinculado ao seu repositorio local

`git status ` é o responsavel por nos mostrar o status do nosso repositorio,o numero de commits etc

#MAIS COMANDOS DO GIT

Caso tenha iniciado o repositorio mas nao era isso que voce queria ou esta na pasta errada 
usando o comando `rm -rf .git` ira retirar a pasta .git e nao ira iniciar o repositorio

Ou se sem querer voce apagou o conteudo do readme.md que estava usando como exemplo antes,com o comando git restore README.md, o proprio git ira restaurar para a ultima versao alterada desse arquivo mas use com sabedoria pq ele descarta todas as alterações e vai que as vezes vc n quer perder todas né

A alteração da mensagem do ultimo commit  pode ser feita usando o comando

`$ git commit --amend -m"nova mensagem do commit"`

outra maneira de alterar pode ser usando apenas `$ git commit --amend
isso ira abrir o editor onde voce pode mudar ali a mensagem do commit,para inserir a mensagem use a tecla i,para sair use Esc + :wq, para escrever  e sair ou so Q para sair
 


 

