<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> Guia de Contribuição</span>
</h1>

[![Star](https://img.shields.io/github/stars/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/stargazers)
[![Forks](https://img.shields.io/github/forks/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/forks)
[![GitHub Issues](https://img.shields.io/github/issues/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/issues/)

Este projeto é feito para a comunidade. Qualquer pessoa pode contribuir!

## Como posso contribuir?

- 📝 **Criar seu Profile README** na pasta [`community`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/community) (é o que esse guia ensina e faz parte do desafio "**Contribuindo em um Projeto Open Source no GitHub**" da [DIO](https://www.dio.me/)).
- 🧰 Adicionar novos utilitários na pasta [`utils`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/utils).
- 🔎 Melhorar a página de pesquisa dos READMEs, editando a pasta [`docs`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/docs).
- ⚠️ Resolver, responder ou indicar **issues** (problemas e dúvidas abertos no projeto).
- ⭐ Dar uma **star** (favoritar) no repositório.

---

## Criando seu Profile README

Seu Profile README é uma página sobre você. Nela você pode colocar:

- **Badges** (selinhos) com suas habilidades;
- **Cards** com suas estatísticas do GitHub e seus projetos;
- **Links** para seus desafios e artigos na [DIO](https://www.dio.me/).

💡 Veja os exemplos na pasta [`community`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/community) e os utilitários na pasta [`utils`](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/utils) para se inspirar.

> Nos comandos abaixo, troque `SEU_USERNAME` pelo seu nome de usuário do GitHub.

### Passo 1: Faça um Fork

**O que fazer:** na página principal deste repositório, clique no botão **Fork** (canto superior direito).

**Por quê:** o fork cria uma cópia do projeto na sua conta. Você não tem permissão para alterar o projeto original, mas pode mexer livremente na sua cópia.

> [Documentação do GitHub sobre fork](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

### Passo 2: Clone o seu fork

**O que fazer:** abra o Git Bash e rode:

```bash
git clone https://github.com/SEU_USERNAME/dio-lab-open-source.git
```

**Por quê:** o fork está na internet (no GitHub). O `git clone` baixa uma cópia dele para o seu computador, para você poder editar os arquivos.

### Passo 3: Crie uma branch

**O que fazer:** entre na pasta do projeto e rode:

```bash
git checkout -b feat/community/SEU_USERNAME
```

Exemplo: `git checkout -b feat/community/falvojr`

**Por quê:** uma branch é uma "linha de trabalho" separada. Assim suas mudanças ficam isoladas e não mexem na versão principal do projeto.

### Passo 4: Crie seu Profile README

**O que fazer:** dentro da pasta `community`, crie um arquivo Markdown (`.md`) com o **mesmo nome do seu usuário do GitHub**. Exemplo: `community/falvojr.md`. Depois, escreva nele o seu perfil (veja as ideias na seção acima).

**Por quê:** o nome do arquivo é usado para identificar você. Se estiver diferente do seu usuário, o PR não será aprovado.

### Passo 5: Adicione o arquivo à "staging area"

**O que fazer:**

```bash
git add community/SEU_USERNAME.md
```

**Por quê:** a staging area é uma "lista de espera". Você escolhe quais mudanças vão entrar no próximo commit. Aqui, só o seu arquivo.

### Passo 6: Crie um commit

**O que fazer:**

```bash
git commit -m "feat: add SEU_USERNAME profile"
```

**Por quê:** o commit salva as mudanças da staging area no histórico do Git, junto com uma mensagem que explica o que foi feito. Use o padrão da [Convenção de Commits](#convenção-de-commits) (aqui, `feat` porque você está adicionando algo novo).

### Passo 7: Envie para o GitHub (push)

**O que fazer:**

```bash
git push origin feat/community/SEU_USERNAME
```

**Por quê:** até agora tudo está só no seu computador. O `git push` envia sua branch para o seu fork no GitHub.

> ℹ️ Se você criou o arquivo direto no site do GitHub, **pule este passo**: ele já está online.

### Passo 8: Abra um Pull Request (PR)

**O que fazer:** no GitHub, abra um Pull Request do seu fork para este repositório.

**Por quê:** o PR é o seu pedido para que as suas mudanças sejam adicionadas ao projeto original.

**Antes de enviar, confira:**

- ✅ O PR altera **somente** o arquivo `community/SEU_USERNAME.md` (veja na aba **Files changed**).
- ✅ O nome do arquivo é **exatamente** igual ao seu usuário do GitHub. Maiúsculas e minúsculas importam!

> [Como criar um Pull Request](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

**E depois?** Uma automação verifica seu PR e responde com uma mensagem. Se estiver tudo certo, ele é aprovado. Se não, leia a mensagem, confira os arquivos alterados e corrija.

---

## Convenção de Commits

Toda mensagem de commit começa com um **tipo**, seguido de `:` e uma descrição curta. Isso deixa o histórico do projeto organizado e fácil de ler.

| Tipo       | Use quando...                                        | Exemplo                                  |
| ---------- | ---------------------------------------------------- | ---------------------------------------- |
| `feat`     | adicionar algo novo                                  | `feat: add SEU_USERNAME profile`         |
| `fix`      | corrigir um erro                                     | `fix: fixed issue #12`                   |
| `docs`     | alterar a documentação                               | `docs: update README.md`                 |
| `style`    | mudar a aparência, sem mudar o funcionamento         | `style: add border to card`              |
| `refactor` | reorganizar o código, sem mudar o funcionamento      | `refactor: simplify UserService`         |
| `test`     | adicionar ou alterar testes                          | `test: add unit test for UserService`    |

## Referências

- [ANGULAR. Contributing to Angular](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md)
- [CONVENTIONAL COMMITS. Summary](https://www.conventionalcommits.org/en/v1.0.0/)
- [GITHUB. Configurar diretrizes para os contribuidores do repositório](https://docs.github.com/pt/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
