<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> Contribuindo em um Projeto Open Source no GitHub</span>
</h1>

Repositório desenvolvido para fins didáticos, com a disponibilização de materiais de apoio e exercício prático para o lab **Contribuindo em um Projeto Open Source no GitHub** da [Digital Innovation One](https://www.dio.me/).

[![Link do Lab](https://img.shields.io/badge/▶-000?style=for-the-badge&logo=movie&logoColor=E94D5F)](https://web.dio.me/lab/desafio-de-projeto-contribuindo-em-um-projeto-open-source-no-github/learning/913f26fd-1018-4643-b59a-6356ea77dc2e) 
[![Link do Lab](https://img.shields.io/badge/Acesse%20o%20Lab%20na%20Plataforma-E94D5F?style=for-the-badge)](https://web.dio.me/lab/desafio-de-projeto-contribuindo-em-um-projeto-open-source-no-github/learning/913f26fd-1018-4643-b59a-6356ea77dc2e)

## Objetivo
Aprender o básico sobre contribuição no GitHub.

## Ferramentas
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://docs.github.com/)
[![Git](https://img.shields.io/badge/Git-000?style=for-the-badge&logo=git&logoColor=E94D5F)](https://git-scm.com/doc) 

## Percurso
<table>
  <thead>
    <tr align="left">
      <th>Nº</th>
      <th>Etapas</th>
    </tr>
  </thead>
  <tbody align="left">
    <tr>
      <td>01</td>
      <td>Introdução ao Lab</td>
    </tr>
    <tr>
      <td>02</td>
      <td>Formas de Contribuir num Projeto Open Source</td>
    </tr>
    <tr>
      <td>03</td>
      <td>Desenvolvendo e Enviando uma Contribuição</td>  
    </tr>
    <tr>
      <td>04</td>
      <td>Dicas e Materiais de Apoio</td>    
    </tr>
  </tbody>
</table>

##  Desafio: Profile README
 Contribua no diretório "Community", criando um Profile README contendo informações sobre você que deseje compartilhar com a comunidade. Para isso, você pode inserir: badges indicando suas habilidades; cards com suas estatísticas no GitHub e projetos que criou, colaborou ou que deseje que outras pessoas colaborem. Além disso, você pode inserir também links para seus desafios de projeto e artigos na plataforma da [Digital Innovation One](https://www.dio.me/). <br>
 Inspire-se consultando os exemplos na pasta [`community`](https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community), confira alguns utilitários na pasta [`utils`](https://github.com/elidianaandrade/dio-lab-open-source/tree/main/utils) e use sua criatividade para criar o seu 😊💙.

### Instruções (PT/BR)
1. Faça um **Fork** deste repositório;
2. Clone localmente: `git clone https://github.com/SEUUSERNAME/dio-lab-open-source.git`;
3. Adicione o remote upstream para manter seu repositório local atualizado: `git remote add upstream https://github.com/elidianaandrade/dio-lab-open-source.git`;
    > Utilize o comando `git pull upstream main` para baixar e mesclar as alterações no seu repositório local com base na branch `main` deste repositório original de onde você fez o fork, ou `git fetch upstream main` para baixar sem mesclar. Veja mais em: [Primeiros Passos com Git e GitHub](https://github.com/elidianaandrade/dio-curso-git-github/blob/main/materiais-de-apoio/03-primeiros-passos-com-git-e-github.md).
4. Crie uma nova **branch** e nomeie como `feat/community/seunomedeusuario`: `git checkout -b feat/community/seunomedeusuario`;
    > Exemplo: `git checkout -b feat/community/sicabralBR`
5. Dentro da pasta [`community`](https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community), crie um arquivo em Markdown (extensão `.md`) e nomeie com o mesmo nome do seu usuário no GitHub;
    > Exemplo: `elidianaandrade.md` <br>
6. Desenvolva o seu perfil. Para isso, você pode ver exemplos na pasta [`community`](https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community) e adicionar alguns dos utilitários presentes na pasta [`utils`](https://github.com/elidianaandrade/dio-lab-open-source/tree/main/utils);
    > **Observação:** Use os outros exemplos como inspiração e não cópia.
7. Adicione suas alterações à "staging area" com o comando `git add community/seunomedeusuario.md`;
8. Crie um commit e adicione a mensagem indicando a adição do seu perfil `git commit -m"feat: add seunomedeusuario profile"`;
9. Envie as alterações para o seu repositório remoto `git push origin feat/community/seunomedeusuario`; 
10. Crie um **Pull Request**.

### Instructions (EN/US)
1. **Fork** the repository;
2. Clone locally: `git clone https://github.com/SEUUSERNAME/dio-lab-open-source.git`;
3. Add upstream remote to keep your local repository up to date: `git remote add upstream https://github.com/elidianaandrade/dio-lab-open-source.git`;
    > Use the command `git pull upstream main` to download and merge changes to your local repository based on the branch `main` from this original repository you forked it from, or `git fetch upstream main` to download without merging. See more at: [Getting Started with Git and GitHub](https://github.com/elidianaandrade/dio-curso-git-github/blob/main/materiais-de-apoio/03-primeiros-passos-com-git-e-github.md).
4. Create a new **branch** and name it as `feat/community/seunomedeusuario`: `git checkout -b feat/community/yourusername`;
    > Example: `git checkout -b feat/community/elidianaandrade`
5. Inside the folder [`community`](https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community), create a file in Markdown (extension `.md`) and name it the same as your GitHub username;
    > Example: `elidianaandrade.md` <br>
6. Develop your profile. For this you can see examples in the folder [`community`](https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community) and add some of the utilities present in the folder [`utils`](https://github.com/elidianaandrade/dio-lab-open-source/tree/main/utils);
    > **Note:** Use the other examples as inspiration, not copy.
7. Add your changes to the "staging area" with the command `git add community/yourusername.md`;
8. Create a commit and add the message indicating the addition of your profile `git commit -m"feat: add yourusername profile"`;
9. Push changes to your remote repository `git push origin feat/community/yourusername`; 
10. Create a **Pull Request**.

## Desafio de Projeto da DIO
Agora que você já sabe as formas de contribuir em um projeto Open Source, está na hora de colocar em prática o seu conhecimento sobre contribuição no GitHub! <br>
Para concluir este Desafio de Projeto, basta enviar a **URL do seu "fork" de um projeto Open Source que você contribuiu** para a entrega do desafio na plataforma [DIO](https://www.dio.me/).

> [!NOTE]   
> Por exemplo, a URL https://github.com/falvojr/dio-lab-open-source é o "**fork**" feito pelo usuário do GitHub "`falvojr`" para a contribuição no repositório `dio-lab-open-source`.

### Contribua com seu Profile README
Para contribuir neste repositório, uma das formas é através da contribuição no diretório "**community**", criando um Profile README contendo informações sobre você que deseje compartilhar com a comunidade. <br>
Para isso, você pode inserir: badges indicando suas habilidades; cards com suas estatísticas no GitHub e projetos que criou, colaborou ou que deseje que outras pessoas colaborem. Além disso, você pode inserir também links para seus desafios de projeto e artigos na plataforma da [Digital Innovation One](https://www.dio.me/). <br>
 Inspire-se consultando os exemplos na pasta [`community`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/community), confira alguns utilitários na pasta [`utils`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/utils) e use sua criatividade para criar o seu 😊💙.

#### Utilitários

[![Badges](https://img.shields.io/badge/Badges-30A3DC?style=for-the-badge)](https://github.com/digitalinnovationone/dio-lab-open-source/blob/main/utils/badges/badges.md)
[![Card Stats](https://img.shields.io/badge/Card%20Stats-E94D5F?style=for-the-badge)](https://github.com/digitalinnovationone/dio-lab-open-source/blob/main/utils/cards/github-stats.md)
[![Badges](https://img.shields.io/badge/Card%20Streak%20States-30A3DC?style=for-the-badge)](https://github.com/digitalinnovationone/dio-lab-open-source/blob/main/utils/cards/github-streak-stats.md)

> [!IMPORTANT]   
> Confira as instruções antes de enviar a sua contribuição em [CONTRIBUTING.md](https://github.com/digitalinnovationone/dio-lab-open-source/blob/main/CONTRIBUTING.md)

### Fórum do Repositório (GitHub Discussions)
GitHub Discussions é um fórum de comunicação colaborativo dentro do GitHub. Caso tenha dúvidas, você pode abrir uma discussão, dentro de uma categoria apropriada, na aba "Discussions" do repositório do projeto.

> [!WARNING]  
> **Atenção:** Antes de criar uma nova discussão, verifique se sua dúvida já foi respondida em discussões anteriores. Use a função de pesquisa para encontrar tópicos relevantes.

---

## Contribua
[![Star](https://img.shields.io/github/stars/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/stargazers)
[![Forks](https://img.shields.io/github/forks/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/forks)
[![GitHub Issues](https://img.shields.io/github/issues/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/issues/)

 Este é um projeto feito para a comunidade, então sinta-se livre para contribuir. Algumas formas de contribuição além do seu exemplo de Profile README, é inserir outros utilitários na pasta [`utils`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/utils), ou melhorar a página de pesquisa dos READMEs fazendo modificações nos arquivos da pasta [`docs`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/docs). <br>
 Além disso, você também pode contribuir:
 
⚠️ Resolvendo, respondendo ou indicando **issues**

⭐ Adicionando aos favoritos (**star**) 

### Membros da comunidade que já contribuiram:
<a href="https://github.com/digitalinnovationone/dio-lab-open-source/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=digitalinnovationone/dio-lab-open-source"/>
</a>

##
<div align="center">Feito com 💙 por <a href="https://github.com/elidianaandrade">Eli</a>.</div>
