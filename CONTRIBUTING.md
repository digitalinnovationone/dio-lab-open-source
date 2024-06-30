<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> Guia de Contribuição</span>
</h1>

[![Star](https://img.shields.io/github/stars/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/stargazers)
[![Forks](https://img.shields.io/github/forks/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/forks)
[![GitHub Issues](https://img.shields.io/github/issues/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/issues/)

 Este é um projeto feito para a comunidade, então sinta-se livre para contribuir. Algumas formas de contribuição além do seu exemplo de Profile README, é inserir outros utilitários na pasta [`utils`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/utils), ou melhorar a página de pesquisa dos READMEs fazendo modificações nos arquivos da pasta [`docs`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/docs). <br>
 Além disso, você também pode contribuir:
 
⚠️ Resolvendo, respondendo ou indicando **issues**

⭐ Adicionando aos favoritos (**star**) 

##  Contribuindo no diretório "Community" 
 A contribuição no diretório "Community" é uma das formas de completar o Desafio do lab "**Contribuindo em um Projeto Open Source no GitHub**" da [Digital Innovation One](https://www.dio.me/). Você pode colaborar criando um Profile README contendo informações sobre você que deseje compartilhar com a comunidade. <br>
 Para isso, você pode inserir: badges indicando suas habilidades; cards com suas estatísticas no GitHub e projetos que criou, colaborou ou que deseje que outras pessoas colaborem. Além disso, você pode inserir também links para seus desafios de projeto e artigos na plataforma da [Digital Innovation One](https://www.dio.me/). <br>
 Inspire-se consultando os exemplos na pasta [`community`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/community), confira alguns utilitários na pasta [`utils`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/utils) e use sua criatividade para criar o seu 😊💙.

### 1) Faça um **Fork** deste Repositório
Acesse a página principal do repositório e clique no botão "Fork" no canto superior direito da página.
> [!NOTE]  
> Um "fork" no GitHub é uma cópia de um repositório que pode ser criada por qualquer usuário. <br>
> Para mais detalhes, reveja a aula ou acesse a documentação do GitHub: [Criar fork de um repositório](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

### 2) Clone localmente
Abra o seu Git Bash e digite o comando `git clone` seguido da URL do seu fork para clonar o seu repositório localmente. Por exemplo:
```bash
git clone https://github.com/SEU_USERNAME/dio-lab-open-source.git
```
Pressione enter, e uma cópia do seu fork no GitHub será criada localmente.

### 3) Crie uma nova **branch** 
Utilize o comando `git checkout -b` para criar e alternar para a nova branch e nomeie-a como `feat/community/SEU_USERNAME`
> Exemplo: `git checkout -b feat/community/falvojr`

### 4) Crie o seu Profile README
 Dentro da pasta [`community`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/community), crie um arquivo em Markdown (extensão `.md`) e nomeie com o mesmo nome do seu usuário no GitHub:

> Exemplo: `community/falvojr.md`

#### 4.1) Desenvolva o seu Profile README
Para isso, você pode se inspirar nos exemplos no diretório [`community`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/community) e adicionar alguns dos utilitários presentes na pasta [`utils`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/utils)

### 5) Adicione suas alterações à "staging area" 
Utilize o comando `git add community/SEU_USERNAME.md` para adicionar sua alteração (nesse caso o arquivo markdown criado)  à "staging area" no Git.

### 6) Crie um Commit
Crie um commit e adicione a mensagem indicando a adição do seu perfil:
```bash
git commit -m"feat: add SEU_USERNAME profile"
```
>[!IMPORTANT]
> Verifique a [`Convenção de Commits`](https://github.com/digitalinnovationone/dio-lab-open-source/blob/main/CONTRIBUTING.md#conven%C3%A7%C3%A3o-de-commits) para escrever a mensagem do seu commit de forma clara e padronizada.

### 7) Envie as Alterações para o seu Repositório Remoto
Envie as alterações realizadas no seu repositório local para a branch `feat/community/SEU_USERNAME` no seu repositório remoto com o comando:
```bash
git push origin feat/community/SEU_USERNAME
```
>[!WARNING]
> Caso você tenha criado seu arquivo diretamente no repositório remoto no GitHub, esse processo não será necessário.

### 8) Crie um **Pull Request**.

Atente-se para a seguir as orientações para a contribuição, principalmente:
- Seu PR deve modificar apenas o arquivo community/SEU_USERNAME.md (dê uma olhadinha na aba "Files changed");
- O nome desse arquivo deve ser exatamente igual ao nome de usuário no GitHub (nossa validação é case-sensitive).

>[!NOTE]
> Caso não saiba como criar uma solicitação de pull, reveja o lab ou acesse a documentação do GitHub: [Como criar uma solicitação de pull
](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

Após criar o seu Pull Request, nossa automação irá validar a sua submissão. Caso esteja tudo certo, será retornada uma mensagem indicado que seu PR foi aprovado. Do contrário, leia atentamente as orientações e verifique os arquivos modificados para saber se atende as instruções para contribuição.
    
    
## Convenção de Commits 

| Tipo de Commit |Descrição                                                            | Exemplo
| ---------------|----------------------------------------------------------------------|-----------
| `feat`         | Adiciona uma nova funcionalidade ao projeto.                         | `feat: add USENAME.md profile`
| `fix`          | Corrige um bug ou problema no projeto.                               | `fix: fixed issue fix#IssueNumber`
| `docs`         | Altera a documentação do projeto.| `docs: update README.md`
| `style`        | Realiza mudanças na aparência, sem alterar a funcionalidade.         | `style: add EFFECTNAME to COMPONENT`
| `refactor`     | Realiza mudanças no código que não alteram a funcionalidade.         | `refactor: refactor at CLASSNAME`
| `test`         | Adiciona ou modifica testes no projeto.                              | `test: add unit test for UserService`

## Comandos do Sistema Operacional (SO) no Git Bash

| **Comando** | **Descrição**
|-------------|-------------------------------------------------------------------------------
| `ls`        | Lista o conteúdo do diretório atual.
| `cd`        | Muda o diretório atual para o especificado.                              
| `pwd`       | Exibe o caminho completo do diretório de trabalho atual.                 
| `mkdir`     | Cria um novo diretório.                                                  
| `rmdir`     | Remove um diretório vazio.                                                
| `rm`        | Remove arquivos ou diretórios.                                            
| `cp`        | Copia arquivos ou diretórios.                                             
| `mv`        | Move ou renomeia arquivos ou diretórios.                                  
| `touch`     | Cria um novo arquivo vazio ou atualiza a data e hora de um arquivo existente.
| `echo`      | Exibe uma linha de texto ou uma string passada como argumento.            
| `cat`       | Exibe o conteúdo de um arquivo.                                           
| `nano`      | Abre o editor de texto Nano para editar arquivos.                         
| `chmod`     | Modifica as permissões de um arquivo ou diretório.                        
| `chown`     | Modifica o proprietário de um arquivo ou diretório.                       
| `grep`      | Pesquisa texto usando padrões.                                            
| `find`      | Pesquisa arquivos e diretórios em uma hierarquia de diretórios.           
| `tar`       | Arquiva vários arquivos em um único arquivo tarball.                      
| `zip`       | Compacta arquivos em um arquivo zip.                                      
| `unzip`     | Extrai arquivos de um arquivo zip.                                        
| `df`        | Exibe a quantidade de espaço livre no sistema de arquivos.                
| `du`        | Exibe o uso do espaço em disco de arquivos e diretórios.                  
| `ps`        | Exibe uma lista de processos em execução.                                 
| `kill`      | Envia um sinal para um processo, geralmente para terminar o processo.     

## Comandos do Git

|**Comando**     | **Descrição**
|----------------|-----------------------------------------------------------------------------
| `git init`     | Inicializa um novo repositório Git.
| `git clone`    | Clona um repositório Git existente.
| `git status`   | Exibe o status dos arquivos no diretório de trabalho e no índice (staging area).
| `git add`      | Adiciona arquivos ao índice (staging area).                                 
| `git commit`   | Salva as mudanças no repositório local.
| `git push`     | Envia os commits do repositório local para um repositório remoto.         
| `git pull`     | Atualiza o repositório local com as mudanças de um repositório remoto.    
| `git fetch`    | Baixa commits, arquivos e referências de um repositório remoto.           
| `git merge`    | Combina mudanças de diferentes ramificações.                              
| `git branch`   | Lista, cria ou exclui ramificações.                                       
| `git checkout` | Alterna entre ramificações ou restaura arquivos da árvore de trabalho.    
| `git log`      | Exibe o histórico de commits do repositório.                              
| `git diff`     | Mostra as diferenças entre commits, ramificações e arquivos.              
| `git stash`    | Salva temporariamente as mudanças não comitadas.                          
| `git remote`   | Gerencia repositórios remotos.                                            
| `git tag`      | Cria, lista, exclui ou verifica tags.                                     
| `git rebase`   | Reaplica commits em cima de outro ponto na história do repositório.       
| `git reset`    | Redefine o índice (staging area) e a árvore de trabalho para coincidir com um commit.
| `git rm`       | Remove arquivos do índice (staging area) e da árvore de trabalho.         
| `git mv`       | Move ou renomeia arquivos e adiciona as mudanças ao índice (staging area).

## Referências
- [ANGULAR. Contributing to Angular](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md)
- [CONVENTIONAL COMMITS. Summary](https://www.conventionalcommits.org/en/v1.0.0/)
- [GITHUB. Configurar diretrizes para os contribuidores do repositório](https://docs.github.com/pt/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
