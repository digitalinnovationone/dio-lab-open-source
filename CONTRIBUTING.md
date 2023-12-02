<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> Guia de Contribuição</span>
</h1>

### Instruções
1. Faça um **Fork** deste repositório;
2. Clone localmente: `git clone https://github.com/SEU_USERNAME/dio-lab-open-source.git`;
3. Adicione o remote upstream para manter seu repositório local atualizado: `git remote add upstream https://github.com/elidianaandrade/dio-lab-open-source.git`;
    > Utilize o comando `git pull upstream main` para baixar e mesclar as alterações no seu repositório local com base na branch `main` deste repositório original de onde você fez o fork, ou `git fetch upstream main` para baixar sem mesclar. Veja mais em: [Primeiros Passos com Git e GitHub](https://github.com/elidianaandrade/dio-curso-git-github/blob/main/materiais-de-apoio/03-primeiros-passos-com-git-e-github.md).
4. Crie uma nova **branch** e nomeie como `feat/community/SEU_USERNAME`:
    > Exemplo: `git checkout -b feat/community/elidianaandrade`
5. Dentro da pasta [`community`](https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community), crie um arquivo em Markdown (extensão `.md`) e nomeie com o mesmo nome do seu usuário no GitHub;
    > Exemplo: `community/elidianaandrade.md` <br>
6. Desenvolva o seu perfil. Para isso, você pode ver exemplos na pasta [`community`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/community) e adicionar alguns dos utilitários presentes na pasta [`utils`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/utils);
    > **Observação:** Use os outros exemplos como inspiração e não cópia.
7. Adicione suas alterações à "staging area" com o comando `git add community/SEU_USERNAME.md`;
    > **Observação:** Você pode utilizar o comando `git add .` para adicionar todas as alterações de uma vez só.
8. Crie um commit e adicione a mensagem indicando a adição do seu perfil `git commit -m"feat: add SEU_USERNAME profile"`;
    > **Observação:** Verificar a [`Convenção de Commits`](https://github.com/kkademorais/dio-lab-open-source/blob/main/CONTRIBUTING.md#conven%C3%A7%C3%A3o-de-commits) para escrever a mensagem do seu commit de forma clara e padronizada.
9. Envie as alterações para o seu repositório remoto `git push origin feat/community/SEU_USERNAME`;
    > **Observação:** Você pode utilizar o comando `git push origin` para mandar as alterações sem precisar especificar a URL, desde que você tenha feito o passo **3**. 
10. Crie um **Pull Request**.

## Convenção de Commits 

| Tipo de Commit | Descrição|
| ---------------|----------|
| `feat`         | Adiciona uma nova funcionalidade ao projeto.   |
| `fix`          | Corrige um bug ou problema no projeto.         |
| `docs`         | Altera a documentação do projeto. Ex.: README, comentários no código.                                            |
| `style`        | Realiza mudanças na aparência, sem alterar a funcionalidade.                                                   |
| `refactor`     | Realiza mudanças no código que não alteram a funcionalidade.                                                   |
| `test`         | Adiciona ou modifica testes no projeto.        |
