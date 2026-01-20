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

### Padronização de Commits

Padronizar commits em um repositório de código é essencial para manter a clareza e a organização do histórico de alterações. Um commit bem documentado facilita a colaboração e a manutenção do código. Aqui estão algumas práticas recomendadas para padronização de commits:

1. **Mensagens Claras e Concisas:**
   - Use o idioma do projeto para escrever as mensagens de commit.
   - A linha de assunto (subject line) deve ser curta (50 caracteres ou menos) e descrever sucintamente a alteração.
   - O corpo da mensagem deve detalhar a mudança, se necessário, e pode ser separado por uma linha em branco da linha de assunto.

2. **Verbos no Imperativo:**
   - Utilize verbos no imperativo presente, como "Adiciona", "Remove", "Corrige", etc.
   - Exemplo: `Corrige bug na autenticação de usuários`.

3. **Referência a Issues ou Tarefas:**
   - Sempre que possível, referencie a issue ou tarefa relacionada ao commit.
   - Exemplo: `Adiciona endpoint de login (#123)`.

4. **Separação de Assuntos:**
   - Cada commit deve abordar uma única funcionalidade ou correção. Evite commits que abrangem múltiplos assuntos.

5. **Formato Consistente:**
   - Utilize um formato consistente para as mensagens. Exemplo:
     ```
     <tipo>(<escopo>): <descrição>

     [Corpo da mensagem]
     ```

### Commits Semânticos (Conventional Commits)

Commits semânticos seguem uma convenção específica que facilita a automação de versionamento e a geração de changelogs. Essa convenção é amplamente utilizada e consiste em mensagens de commit estruturadas de maneira padronizada.

#### Estrutura Básica:

```
<tipo>(<escopo opcional>): <descrição>

[Corpo opcional]
[Rodapé opcional]
```

#### Tipos Comuns:

- `feat`: Introduz uma nova funcionalidade.
  - Exemplo: `feat: adiciona suporte a múltiplos idiomas`
- `fix`: Corrige um bug.
  - Exemplo: `fix: corrige erro de navegação no menu`
- `docs`: Alterações na documentação.
  - Exemplo: `docs: atualiza guia de instalação`
- `style`: Alterações de estilo (espaçamento, formatação, etc.) que não afetam a lógica do código.
  - Exemplo: `style: formata código conforme padrão ESLint`
- `refactor`: Mudanças no código que não corrigem bugs nem adicionam funcionalidades.
  - Exemplo: `refactor: otimiza algoritmo de busca`
- `test`: Adiciona ou corrige testes.
  - Exemplo: `test: adiciona testes unitários para componente Header`
- `chore`: Tarefas de manutenção.
  - Exemplo: `chore: atualiza dependências`

#### Exemplos de Commits Semânticos:

1. **Commit de Funcionalidade:**
   ```
   feat(auth): adiciona autenticação via OAuth

   Adiciona suporte para autenticação de usuários usando OAuth 2.0.
   ```

2. **Commit de Correção:**
   ```
   fix(login): corrige falha na verificação de senha

   Corrige a lógica de verificação de senha para permitir caracteres especiais.
   ```

3. **Commit de Documentação:**
   ```
   docs(readme): atualiza informações de configuração

   Adiciona passos detalhados para configurar o ambiente de desenvolvimento.
   ```

4. **Commit de Estilo:**
   ```
   style: ajusta espaçamento no arquivo main.css

   Remove espaços extras e ajusta indentação para seguir o padrão do projeto.
   ```

5. **Commit de Refatoração:**
   ```
   refactor(api): otimiza funções de busca

   Refatora funções de busca para melhorar a performance.
   ```

6. **Commit de Teste:**
   ```
   test: adiciona testes para componente de login

   Cria testes unitários para garantir a correta funcionalidade do componente de login.
   ```

### Benefícios dos Commits Semânticos:

1. **Clareza:**
   - Facilita a compreensão do histórico de commits, tornando-o mais legível.

2. **Automação:**
   - Permite a automação de versionamento semântico (SemVer) e a geração de changelogs.

3. **Manutenção:**
   - Simplifica a identificação de mudanças específicas, facilitando a manutenção do código.

Ao seguir estas práticas e a convenção de commits semânticos, a equipe de desenvolvimento garante uma maior organização, clareza e eficiência na gestão do código.


## Referências
- [ANGULAR. Contributing to Angular](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md)
- [CONVENTIONAL COMMITS. Summary](https://www.conventionalcommits.org/en/v1.0.0/)
- [GITHUB. Configurar diretrizes para os contribuidores do repositório](https://docs.github.com/pt/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
