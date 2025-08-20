# Visão Geral do curso e ferramentas, Instalação e Configuração
## Ferramenta

***O que é versionamento?***<br>
&nbsp;&nbsp;&nbsp;&nbsp; Controlam as versões de um arquivo ao longo do tempo. Onde registrará o hidtórico de atualizações de um arquivo; Gerencia quais foram as alterações, a data, autor e etc; Organiza, Controla com Segurança.

***Tipos de Sistemas de Controle de Versão***<br>
&nbsp;&nbsp;&nbsp;&nbsp;Dentre os Sistemas de Controle de Versão (VCS), temos:
* VCS - Centralizado (CVCS)
&nbsp;&nbsp;&nbsp;&nbsp; *Exemplos:* CVS, Subversion, etc;
&nbsp;&nbsp;&nbsp;&nbsp; O sistema Centralizado ele possuirá apenas um sistema central para o controle de versão, dentro de um servidor, dessa forma se algo acontecer com o arquivo ele for corrompido ou algo do tipo não terá como recuperar;

* VCS - Distribuido (DVCS)
&nbsp;&nbsp;&nbsp;&nbsp; *Exemplos:* Git, Mercurial, etc;
&nbsp;&nbsp;&nbsp;&nbsp; Aqui ele possui dois armazenamento o local e o remoto, onde o local é a sua maquina e o remoto é dentro da rede mas preciso o GitHub

## Instalação do Git
>⚠️ &nbsp; <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" height="20" width="20"><title>Git for Windows</title><path d="M11.976.0003a1.541 1.541 0 0 0-1.0928.4526L8.707 2.6287l2.7604 2.7604c.6417-.2166 1.377-.0715 1.8882.4399.514.5145.6583 1.2563.4362 1.9l.9101.9102 3.2768-3.2764L13.0684.4529A1.5394 1.5394 0 0 0 11.976.0003ZM7.638 3.698 5.926 5.4101l4.9095 4.9095c.1535.1536.332.267.5217.3423V8.831a1.8198 1.8198 0 0 1-.6024-.4011c-.5441-.5437-.6749-1.3422-.3958-2.0104Zm10.916 2.24-3.2765 3.2764 1.1743 1.1747c.6436-.2217 1.3862-.0782 1.9001.4366.7185.7183.7185 1.8823 0 2.6008-.7186.7187-1.8823.7187-2.6012 0-.5402-.5407-.674-1.3344-.4003-2l-1.1427-1.1423-.588.588c-.6036.604-.6036 1.5829 0 2.1865l4.9935 4.993 4.9342-4.9342c.6035-.6038.6035-1.5829 0-2.1865zM5.34 5.9956.4528 10.8825c-.6037.604-.6037 1.5828 0 2.1864l4.8395 4.8396 4.8873-4.8873c.6035-.6038.6035-1.5828 0-2.1865zm7.5293 2.9497v1.4986c.0516-.04.1048-.077.1522-.1243l.611-.611zm-1.5121 4.2224c-.2317.072-.4514.1927-.6349.376-1.6323 1.6325-3.2647 3.2649-4.8971 4.8972l5.1065 5.1062c.6033.6035 1.582.6035 2.1861 0l4.8967-4.8968-5.1065-5.1065c-.012-.012-.0264-.0202-.0387-.0317v1.9618a1.854 1.854 0 0 1 .4863.3477c.7183.7182.7183 1.8819 0 2.6012-.7185.7182-1.883.7182-2.6008 0-.7184-.7193-.7184-1.883 0-2.6012a1.8406 1.8406 0 0 1 .6024-.4012z"/></svg> &nbsp; para windows

**Site oficial:**



`git-scm.com/download/win`

> Escolha o arquivo que mais se encaixara no seu pc >> ao baixar, clique nele e faça o next até o momento em que aparecer install e finish. <br><br>

## Configurando o GIT


1. Abrir git bash;

* Abrirá uma tela onde aparecerá o nome do nomedocomputador@usuário | MINGW64 \[[mais informação sobre](https://www.google.com/search?q=mingw64+no+bash+do+git+o+que+%C3%A9&oq=mingw64+no+bash+do+git+o+que+%C3%A9&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABjvBTIHCAIQABjvBTIHCAMQABjvBTIHCAQQABjvBTIKCAUQABiiBBiJBdIBCjE4NjQ5ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8)] | e o diretório onde o terminal se encontra.

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

<br><br>
**COMANDOS**

`GIT CONFIG` [apenas] = mostrará informações sobre a ferramenta, ele permite visualizar de definir variáveis de configuração do git, onde essas variáveis elas ficam armazenadas em 3 lugares principais:

* `--global` = referente as configurações no usuário que se encontra no momento;

* `--system` = referente as configurações do sistema como um todo, onde abriga todos os usuários;

* `--local` = referente as configurações de um repositório especifico onde se encontra ou local.
<br><br>

![Static Badge](https://img.shields.io/badge/CRTL_%2B_L-black) ou digitar `clear`
 = Limpa o terminal;

![Static Badge](https://img.shields.io/badge/_%E2%87%A7_-black)
 = irá mostrar o que foi digitado anteriormente;

