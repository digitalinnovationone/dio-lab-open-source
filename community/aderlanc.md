
# DIO - Resumo Git e GitHub

Repositório para armazenar resumos sobre Git e GitHub.

[Site DIO](https://web.dio.me/)

## 📚 Documentação
- [Documentação Git](https://git-scm.com/docs/git/pt_BR) 
- [Documentação GitHub](https://docs.github.com/pt)

## 💻 Principais comandos Git
--mkdir nome-da-pasta (cria uma pasta)

--git init (p inicilizar um repositótio .git na pasta criada)

--git remote add origin URL: conectar o repositório local com o   remoto. 

Ex: git remote add origin https://github.com/aderlanc/repo-remoto.git

Obs. A URL eu copio no meu github do repositório que desejo conectar

--git clone URL nome-do-diretorio-local (usado para clonar o repositório remoto)
 *nome-do-diretorio-local é opcional e usado se vc quiser mudar o nome da pasta no repositório local.

Ex:  git clone https://github.com/aderlanc/helloWorld.git novo-nome

--git clone URL --branch nome-da-branch --single-branch (se quiser clonar uma branch específica)

-- git status (mostra o status do meu repositório)

-- touch README.md (cria um arquivo no meu repositório)

--git add nome-arquivo (adiciona um arquivo na área de preparação)
Ex. git add README.md

Obs. o arquivo adicionado precisa ser commitado

--git add . (adiciona tudo que estiver pendente na área de preparação)

--git commit -m"commit inicial" (commita o repositório com uma mensagem -m)

--git log (mostra um log no repositório)

--echo resumos/ > .gitignore (colocou a parta resumos no gitignore, ou seja, não vai pro repositório remoto)

--rm -rf .git (remove um diretório)

--git restore nome-aquivo (restaura um arquivo)

--git commit --amend -m"corrigir a mensagem do último commit" (altera a mensagem do último commit)

--git commit --amend (entra no editor pra alterar a mensagem). Para sair digita: Esc : wq

--git reset --soft f9f6083fe33ca88d5402940ba6f4f84da6b71743 (desfazer o último commit, passando o rest do commit)

Obs. Pode pegar o rest do commit através do comando git log

--git reset --mixed f9f6083fe33ca88d5402940ba6f4f84da6b71743 (as alterações posteriores vão para a área de trabalho, ou seja, o git ainda não conhece).

--git reset --hard f9f6083fe33ca88d5402940ba6f4f84da6b71743 (cuidado!! desfaz definitivamente o commit)

--git reset resumos/Aula02.md (desfaz o commit de um arquivo específico)

--git reflog (fornece um histórico maid detalhado)

--git restore --staged resumos/Aula03.md (remove o arquivo da área de preparação)

--git restore --staged . (remove tudo da área de preparação)

--git remote add origin https://github.com/aderlanc/resumos-git-github.git

--git push -u origin main (envia as alterações da branch main para o repositório remoto)

*-teste de alteração no github*
