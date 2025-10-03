# [LuthLucas](https://github.com/LuthLucas)

## GitHub Stats

![Most Used Languages](https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api/top-langs/?username=LuthLucas&layout=compact&bg_color=000&border_color=30A3DC&title_color=E94D5F&text_color=FFF)

# Guia Básico de Comandos Git

Este guia apresenta os comandos mais utilizados no Git para facilitar o gerenciamento de repositórios e a colaboração em projetos.

## Configuração Inicial

Antes de começar a usar o Git, configure seu nome de usuário e e-mail:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
```

## Clonando um Repositório

Para clonar um repositório remoto para sua máquina local:

```bash
git clone https://github.com/usuario/repo.git
```

## Verificando o Status

Para verificar o status do repositório e ver as alterações pendentes:

```bash
git status
```

## Adicionando Arquivos ao Controle de Versão

Adicione arquivos específicos ou todos os arquivos modificados:

```bash
git add nome-do-arquivo
git add .
```

## Criando um Commit

Salve as alterações no histórico do repositório com uma mensagem descritiva:

```bash
git commit -m "Mensagem do commit"
```

## Enviando Alterações para o Repositório Remoto

Envie as alterações locais para o repositório remoto:

```bash
git push origin main
```

## Atualizando o Repositório Local

Para obter as alterações mais recentes do repositório remoto:

```bash
git pull origin main
```

## Criando e Alternando entre Branches

Crie uma nova branch e alterne para ela:

```bash
git branch nome-da-branch
git checkout nome-da-branch
```

Ou crie e alterne para a branch em um único comando:

```bash
git checkout -b nome-da-branch
```

## Mesclando Branches

Para mesclar uma branch ao branch atual:

```bash
git merge nome-da-branch
```

## Resolvendo Conflitos

Se houver conflitos durante a mesclagem, edite os arquivos conflitantes, marque-os como resolvidos e crie um commit:

```bash
git add nome-do-arquivo
git commit -m "Resolvendo conflitos"
```

## Excluindo uma Branch

Para excluir uma branch local:

```bash
git branch -d nome-da-branch
```

Para excluir uma branch remota:

```bash
git push origin --delete nome-da-branch
```

---

Para mais informações, consulte a [documentação oficial do Git](https://git-scm.com/doc).