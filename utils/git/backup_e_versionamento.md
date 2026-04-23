# Backups e versionamento do codigo

## Entendendo o que se trata

Você já passou pelo cenário onde estava programando em um projeto, apagou alguns arquivos, e depois de realizar o commit, acabou se arrependendo e não tinha como voltar?
Ou então, estava durante horas programando, não salvou o arquivo e veio a perder o arquivo?

Esse artigo é pra você.

Vou listar boas praticas e comandos uteis para serem utilizados.

## Funcionamento

Nossa ideia para manter qualquer alteração feita, possível de ser desfeita ou recuperada, é realizar um novo mini commit a cada nova alteração, como um trecho novo do codigo ou um novo objeto, para isso, podendo ser utilizado os comandos padroes de commit

`git add .`

`git commit -m "Explicação da alteração"`

Quando quiser recuperar alguma versão que por acaso tenha perdido, você pode utilizar o seguinte comando, para poder listar as versões do seu codigo, atráves das commits.

`git log [-numero de commits que deseja ver])`

Ex:  `git log -10`

após isso, você pode executar o comando para sair da branch atual e selecionar atraves do numero de branch especifico do commit para retornar á snapshot do arquivo:

Para mudar a branch ou versão do commit: `git checkout [versão-do-commit] -b [nome-nova-branch]`

Ex: `git checkout 75a6c43ce6d412123edde1fac33485f72569efcf -b NovaBranch`

Caso tenha finalizado suas edições e deseja limpar o historico de commits, você pode criar uma nova branch, adicionar os arquivos, comitar e realizar um push na branch main da origem.

`git add .`
`git commit -m "sua commit"`
`git push -u origin sua-branch`

## Como o backup pode te salvar?

Evitar a perda do seu progresso é essencial, tanto para sua produtividade quanto para sua sanidade.
Quem não odeia perder horas de trabalho, apenas por um pique de luz, ou algo como isso.
Essas boas praticas de versionamento pode te ajudar em horas que menos esperar.
