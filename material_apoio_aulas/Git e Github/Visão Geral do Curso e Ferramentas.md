# Visão Geral do curso e ferramentas, Instalação e Configuração

## Ferramenta

***O que é versionamento?***<br>
&nbsp;&nbsp;&nbsp;&nbsp; Controlam as versões de um arquivo ao longo do tempo. Onde registrará o hidtórico de atualizações de um arquivo; Gerencia quais foram as alterações, a data, autor e etc; Organiza, Controla com Segurança.

***Tipos de Sistemas de Controle de Versão***<br>
&nbsp;&nbsp;&nbsp;&nbsp;Dentre os Sistemas de Controle de Versão (VCS), temos:

* VCS - Centralizado (CVCS)<br>
&nbsp;&nbsp;&nbsp;&nbsp; *Exemplos:* CVS, Subversion, etc;<br>
&nbsp;&nbsp;&nbsp;&nbsp; O sistema Centralizado ele possuirá apenas um sistema central para o controle de versão, dentro de um servidor, dessa forma se algo acontecer com o arquivo ele for corrompido ou algo do tipo não terá como recuperar;

* VCS - Distribuido (DVCS)<br>
&nbsp;&nbsp;&nbsp;&nbsp; *Exemplos:* Git, Mercurial, etc;<br>
&nbsp;&nbsp;&nbsp;&nbsp; Aqui ele possui dois armazenamento o local e o remoto, onde o local é a sua maquina e o remoto é dentro da rede mas preciso o GitHub

## Instalação do Git

>⚠️ &nbsp; Para windows

**Site oficial:** <br>
`git-scm.com/download/win`

> Escolha o arquivo que mais se encaixara no seu pc >> ao baixar, clique nele e faça o next até o momento em que aparecer install e finish. <br><br>

## Configurando o GIT

1. Abrir git bash;

* Abrirá uma tela onde aparecerá o nome do nomedocomputador@usuário | MINGW64 [[mais informação sobre](https://www.google.com/search?q=mingw64+no+bash+do+git+o+que+%C3%A9&oq=mingw64+no+bash+do+git+o+que+%C3%A9&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABjvBTIHCAIQABjvBTIHCAMQABjvBTIHCAQQABjvBTIKCAUQABiiBBiJBdIBCjE4NjQ5ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8)] | e o diretório onde o terminal se encontra.

* Pode se alterar o tema apertando o botão direito do mouse em >> options >> looks.

<br>

2. Definir nome e email no git =

`git config --global use.name "[coloque seu nome aqui]" <enter>`

`git config --global user.email "[colque seu email aqui]" <enter>`

<br>

3. Visualizar =

`git config user.name <enter>`

`git config user.email <enter>`

<br> 

4. Ver qual o nome do repositório =

`git config init.defaultBranch <enter> [retornara o nome do repositório]`

5. Editar o nome do repositório =

`git config --global init.defaultBranch main <enter>`

* Para mais informações [documentação Git](https://git-scm.com/docs).

<br><br>

**ALGUNS COMANDOS**

`GIT CONFIG` [apenas] = mostrará informações sobre a ferramenta, ele permite visualizar de definir variáveis de configuração do git, onde essas variáveis elas ficam armazenadas em 3 lugares principais:

* `--global` = referente as configurações no usuário que se encontra no momento;

* `--system` = referente as configurações do sistema como um todo, onde abriga todos os usuários;

* `--local` = referente as configurações de um repositório especifico onde se encontra ou local.
<br><br>

![Static Badge](https://img.shields.io/badge/CRTL_%2B_L-black) ou digitar `clear`
 = Limpa o terminal;

![Static Badge](https://img.shields.io/badge/_%E2%87%A7_-black)
 = irá mostrar o último comando que foi digitado;

<br><br>

### REFERÊNCIAS

---

Material didático fornecido dentro da plataforma:<br>

* Você encontrará em: Versionamento de Código com Git e GitHub/Visão Geral do Curso e Ferramentas|Instalação e Configuração e Autenticação 

> Digitalizado em arquivo `.md` para melhor acesso ao conteúdo e podendo ser baixado para serem feitos anotações ou mesmo para fins de leitura apenas.