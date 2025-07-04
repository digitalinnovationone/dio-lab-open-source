## 📄 Guia de Contribuição

[![Star](https://img.shields.io/github/stars/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/stargazers)
[![Forks](https://img.shields.io/github/forks/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/forks)
[![GitHub Issues](https://img.shields.io/github/issues/digitalinnovationone/dio-lab-open-source?style=social)](https://github.com/digitalinnovationone/dio-lab-open-source/issues/)

Este é um projeto feito para a comunidade, então sinta-se livre para contribuir! 🚀

Você pode colaborar criando seu Profile README na pasta [community](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/community), inserindo utilitários na pasta [utils](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/utils), ou melhorando a interface em [docs](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/docs).

Outras formas de contribuir:

* ⚠️ Resolvendo, respondendo ou sinalizando **issues**
* ⭐ Adicionando aos favoritos (**star**) o repositório

---

## 🧹 Contribuindo no diretório "Community"

Essa é uma das formas de completar o desafio "**Contribuindo em um Projeto Open Source no GitHub**" da [Digital Innovation One](https://www.dio.me/).

Você pode colaborar criando um Profile README com informações sobre você e compartilhando com a comunidade!

Exemplos de arquivos:

* [falvojr.md](https://github.com/digitalinnovationone/dio-lab-open-source/blob/main/community/falvojr.md)
* [camilakellen.md](https://github.com/digitalinnovationone/dio-lab-open-source/blob/main/community/camilakellen.md)

---

### Passo a passo para contribuir:

### 1) Faça um **Fork** deste Repositório

Clique no botão **"Fork"** no canto superior direito da página.

> 📘 Saiba mais: [Criar fork de um repositório](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

---

### 2) Clone o repositório no seu computador

Abra o terminal e rode:

```bash
git clone https://github.com/SEU_USERNAME/dio-lab-open-source.git
```

> Substitua `SEU_USERNAME` pelo seu nome de usuário no GitHub.

---

### 3) (Opcional) Atualize o fork com o repositório original

Caso o projeto original já tenha novas alterações:

```bash
git remote add upstream https://github.com/digitalinnovationone/dio-lab-open-source.git
git pull upstream main
```

---

### 4) Crie uma nova **branch** para a sua contribuição

```bash
git checkout -b feat/community/SEU_USERNAME
```

---

### 5) Crie seu Profile README

Crie um arquivo Markdown na pasta `community/` com **exatamente o seu nome de usuário** no GitHub, por exemplo:

```bash
community/seuusername.md
```

> ⚠️ Atenção: o nome do arquivo deve ser **idêntico ao seu usuário** (respeitando maiúsculas/minúsculas).

Você pode usar badges, cards, estatísticas do GitHub, projetos, links para artigos na DIO, etc.

Dicas:

* Explore os exemplos na pasta [community](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/community)
* Use os recursos prontos da pasta [utils](https://github.com/digitalinnovationone/dio-lab-open-source/tree/main/utils)

---

### 6) Adicione seu arquivo à "staging area"

```bash
git add community/SEU_USERNAME.md
```

---

### 7) Faça o commit

```bash
git commit -m "feat: add SEU_USERNAME profile"
```

> 📌 Veja abaixo a convenção de commits utilizada.

---

### 8) Envie a sua branch para o repositório remoto

```bash
git push origin feat/community/SEU_USERNAME
```

---

### 9) Crie um **Pull Request**

Acesse o seu fork no GitHub e clique em **"Compare & pull request"**.
Verifique:

* ✅ O PR modifica **somente o arquivo community/SEU\_USERNAME.md**
* ✅ O nome do arquivo está correto
* ✅ A descrição está clara

> 📘 Mais ajuda: [Como criar um Pull Request](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

Após isso, nossa automação irá validar sua submissão. Se estiver tudo certo, será aprovado! 🎉

---

## ✅ Convenção de Commits

| Tipo     | Descrição                                                   | Exemplo                               |
| -------- | ----------------------------------------------------------- | ------------------------------------- |
| feat     | Adiciona uma nova funcionalidade ao projeto                 | feat: add SEU\_USERNAME profile       |
| fix      | Corrige um bug ou problema no projeto                       | fix: corrigido problema na feature X  |
| docs     | Altera a documentação do projeto                            | docs: atualização do README.md        |
| style    | Mudanças de estilo (espaços, formatação) sem alterar lógica | style: aplica padding no componente Y |
| refactor | Refatoramento que não altera a funcionalidade               | refactor: reorganização da classe Z   |
| test     | Adiciona ou modifica testes                                 | test: adiciona teste para UserService |

---

## Referências

* [Angular - Guia de Contribuição](https://github.com/angular/angular/blob/main/CONTRIBUTING.md)
* [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
* [GitHub - Diretrizes para contribuidores](https://docs.github.com/pt/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
