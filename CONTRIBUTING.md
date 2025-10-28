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


## **Sugestão de Conteúdo Complementar a ser adicionado no [Guia de Contribuição](https://github.com/digitalinnovationone/dio-lab-open-source/blob/main/CONTRIBUTING.md):**

Manter uma boa higiene nas mensagens de commit é uma das práticas mais importantes para a manutenção de um projeto e colaboração em equipe.

Os tipos de commit, tais como `feat:`, `docs:`, `refactor:` fazem parte de um padrão muito popular chamado **Conventional Commits**.

Aqui está um detalhamento das melhores práticas:

  * Boas Práticas para Mensagens de Commit (Git/GitHub)

### O Padrão "Conventional Commits"

Essa é uma convenção que impõe uma estrutura clara às mensagens de commit. O objetivo é criar um histórico explícito que seja fácil de ler por humanos e por máquinas (para automação, como gerar CHANGELOGs).

A estrutura é:

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé opcional]
```

**Principais `<tipo>`:**

  * **feat:** (Feature) Usado ao adicionar uma nova funcionalidade ao código.
  * **fix:** Usado ao corrigir um bug na produção ou em desenvolvimento.
  * **docs:** Usado para alterações *apenas* na documentação (ex: README, comentários de código).
  * **refactor:** Usado para uma alteração de código que não corrige um bug nem adiciona uma funcionalidade (ex: otimização, limpeza de código, renomeação de variáveis).
  * **style:** Alterações que não afetam o significado do código (espaços em branco, formatação, ponto e vírgula).
  * **test:** Adicionando testes que faltam ou corrigindo testes existentes.
  * **chore:** Alterações em processos de build, ferramentas auxiliares ou configurações que não estão relacionadas ao código-fonte (ex: atualizar o `.gitignore`).
  * **perf:** (Performance) Uma alteração de código que melhora o desempenho.
  * **ci:** Alterações nos arquivos e scripts de configuração de CI (Integração Contínua).

-----

### As 7 Regras de Ouro para Commits

Independentemente de você usar o "Conventional Commits", estas 7 regras (popularizadas por Tim Pope) são a base de qualquer boa mensagem de commit:

1.  **Separe o assunto do corpo com uma linha em branco:** O Git é otimizado para isso.
2.  **Limite a linha de assunto (subject) a 50 caracteres:** Isso mantém as mensagens curtas e fáceis de ler no `git log`.
3.  **Comece a linha de assunto com letra maiúscula:** É uma convenção de estilo, como um título.
4.  **Não termine a linha de assunto com um ponto:** O assunto é um título, não uma frase.
5.  **Use o modo imperativo na linha de assunto:**
      * **Bom:** `Adiciona feature de login` (Como se estivesse dando uma ordem).
      * **Ruim:** `Adicionada feature de login` (Passado).
      * **Ruim:** `Adicionando feature de login` (Gerúndio).
6.  **Quebre as linhas do corpo (body) em 72 caracteres:** Isso garante que o texto seja legível em qualquer terminal sem quebras estranhas.
7.  **Use o corpo para explicar *o quê* e *por quê* (vs. *como*):** O código mostra *como* a mudança foi feita. O corpo do commit deve explicar *por que* essa mudança foi necessária e *qual* foi o impacto.

-----

### Juntando Tudo: Um Exemplo Ideal

Aqui está um exemplo que combina o "Conventional Commits" com as "7 Regras de Ouro".

#### 

```
feat(auth): Adiciona sistema de login com Google OAuth

Implementa o fluxo de autenticação OAuth2 para permitir que novos
usuários se cadastrem e façam login utilizando suas contas Google.

Isso resolve a Issue #*123 e melhora significativamente a experiência
de onboarding, reduzindo o atrito no cadastro.
```

#### 

**Análise deste exemplo:**

  * **Tipo:** `feat` (nova funcionalidade).
  * **Escopo:** `(auth)` (módulo de autenticação).
  * **Assunto:** `Adiciona sistema de login...` (Imperativo, maiúscula, \< 50 caracteres, sem ponto final).
  * **Linha em Branco:** Separa o assunto do corpo.
  * **Corpo:** Explica *o quê* (OAuth2) e *por quê* (resolve a Issue #*123, melhora onboarding). As linhas têm menos de 72 caracteres.

-----

### Por que se Preocupar com Isso?

  * **Revisão de Código (Code Review):** Facilita para seus colegas entenderem rapidamente o que sua mudança faz.
  * **Histórico (`git log`):** Permite navegar pelo histórico do projeto de forma eficiente.
  * **Depuração (`git bisect`):** Ajuda a encontrar qual commit introduziu um bug.
  * **Automação:** Permite gerar automaticamente notas de lançamento (CHANGELOGs) e controlar o versionamento (Semantic Versioning).
 
-----
### Referências:

Você gostaria de ver mais exemplos de `types` do Conventional Commits (como `ci:`, `perf:`, `style:`)?

**Fontes Principais:**

Conventional Commits: Este é o site oficial da especificação, que detalha todos os tipos, regras e a estrutura exata. O objetivo é ter um padrão legível por máquinas para automação:** 
[Conventional Commits (www.conventionalcommits.org)](https://www.conventionalcommits.org/en/v1.0.0/)

As "7 Regras de Ouro" para Mensagens de Commit: Estas são as regras de formatação mais famosas (ex: limite de 50 caracteres no assunto, uso do modo imperativo) que foram popularizadas por Tim Pope e excelentemente documentadas por Chris Beams.:** 
[How to Write a Git Commit Message (cbea.ms)](https://cbea.ms/git-commit/)

**Fontes Adicionais (Leitura Recomendada):**
[Atlassian Git Tutorial - git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit)
[Write Better Commits, Build Better Projects](https://github.blog/2022-06-30-write-better-commits-build-better-projects/)
[How to Write Better Git Commit Messages – A Step-By-Step Guide](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)
    
    
## Convenção de Commits 

| Tipo de Commit |Descrição                                                            | Exemplo
| ---------------|----------------------------------------------------------------------|-----------
| `feat`         | Adiciona uma nova funcionalidade ao projeto.                         | `feat: add USENAME.md profile`
| `fix`          | Corrige um bug ou problema no projeto.                               | `fix: fixed issue fix#IssueNumber`
| `docs`         | Altera a documentação do projeto.| `docs: update README.md`
| `style`        | Realiza mudanças na aparência, sem alterar a funcionalidade.         | `style: add EFFECTNAME to COMPONENT`
| `refactor`     | Realiza mudanças no código que não alteram a funcionalidade.         | `refactor: refactor at CLASSNAME`
| `test`         | Adiciona ou modifica testes no projeto.                              | `test: add unit test for UserService`

## Referências
- [ANGULAR. Contributing to Angular](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md)
- [CONVENTIONAL COMMITS. Summary](https://www.conventionalcommits.org/en/v1.0.0/)
- [GITHUB. Configurar diretrizes para os contribuidores do repositório](https://docs.github.com/pt/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
