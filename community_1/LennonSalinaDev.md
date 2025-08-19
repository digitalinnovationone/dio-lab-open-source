
# 👨🏽‍💻Sobre mim e sobre o readme 📙
Olá meu meu nome é [Lennon](https://github.com/LennonSalinaDev), estou participando do bootcamp da DIO [Santander 2025 - Back-End com Python](https://web.dio.me/track/santander-2025-python-back-end). Fiz um resumo do curso de versionamento de código com git e github da expert DIO [Ediana Andrada](https://github.com/elidianaandrade). Neste guia trago os tópicos mais importante para quem está iniciando e deseja treinar o básico 🤞. ME SIGA se também for ou deseja ser um [usuário DIO](https://www.dio.me/users/lennon_salina).

# Guia Git e GitHub

## ✨ Introdução ao Controle de Versão

### O que é um VCS?
Um Sistema de Controle de Versão (VCS - *Version Control System*) é uma ferramenta que registra o histórico de alterações de arquivos ao longo do tempo. Ele permite:
- Organização, controle e segurança das modificações;
- Identificação de quem alterou o quê e quando;
- Reversão de mudanças e comparações entre versões.

### Tipos de VCS
- **Centralizado (CVCS)**: há um único servidor central com todos os arquivos versionados.
  - CVS
  - Subversion (SVN)

- **Distribuído (DVCS)**: cada usuário possui uma cópia local completa do repositório.
  - Git
  - Mercurial

---

## 🐙 Git

O Git é um sistema de controle de versão distribuído, gratuito e de código aberto (*open source*).

### Características:
- Leve e rápido;
- Suporte robusto a *branching* e *merging*;
- Utilização massiva na indústria de software.

### Fluxo Básico de Comandos Git
```bash
# Clonar repositório remoto
$ git clone <URL>

# Salvar alterações
$ git commit -m "mensagem"

# Atualizar repositório local
$ git pull

# Enviar alterações para o remoto
$ git push
```

---

## 💻 GitHub

Plataforma para hospedagem de código com integração ao Git, amplamente utilizada para colaboração em projetos.

### Destaques:
- Comunidade ativa e global;
- Mascote: **Octocat**;
- Suporte a *issues*, *pull requests*, *actions*, entre outros.

---

## ⚙️ Configuração Inicial do Git
```bash
# Nome e e-mail globais
$ git config --global user.name "Seu Nome"
$ git config --global user.email "email@exemplo.com"

# Definir branch padrão
$ git config --global init.defaultBranch main

# Ver configurações globais
$ git config --global --list
```

---

## 🔐 Autenticação no GitHub

### Via Token (HTTPS)
1. Acesse: **Settings > Developer Settings > Personal Access Tokens**
2. Gere um token (*classic*) com as permissões adequadas
3. Use o token como senha no `git clone`
```bash
$ git config --global credential.helper store
```

### Via SSH
```bash
# Gerar chave
$ ssh-keygen -t ed25519 -C "email@exemplo.com"

# Iniciar agente
$ eval "$(ssh-agent -s)"
$ ssh-add ~/.ssh/id_ed25519

# Copiar chave pública
$ cat ~/.ssh/id_ed25519.pub
```

Adicione a chave no GitHub em **Settings > SSH and GPG Keys**

---

## 📂 Criando Repositório Local
```bash
$ mkdir nome-do-repo && cd nome-do-repo
$ git init
$ git remote add origin <URL>
```

## 💾 Salvando Alterações
```bash
$ touch README.md
$ git add README.md
$ git commit -m "Commit inicial"
$ git push -u origin main
```

### Ignorar arquivos:
```bash
$ echo "resumos/" > .gitignore
$ touch aulas/.gitkeep
```

---

## 🔄 Desfazendo Alterações
```bash
# Remover versionamento
$ rm -rf .git

# Restaurar arquivo
$ git restore README.md

# Alterar mensagem do último commit
$ git commit --amend -m "Nova mensagem"

# Resetar commit
$ git reset --soft <hash>
$ git reset --mixed <hash>
$ git reset --hard <hash>

# Ver histórico detalhado
$ git reflog
```

> ⚠️ Sempre confirme as alterações antes de enviar ao repositório remoto.

---

## 🚀 Envio e Sincronização com o Repositório Remoto
```bash
# Conectar repositório
$ git remote add origin <URL>

# Enviar alterações
$ git push -u origin main

# Baixar e mesclar alterações remotas
$ git pull
```

---

## 📋 Branches (Ramificações)
```bash
# Criar nova branch
$ git checkout -b nome-da-branch

# Listar branches
$ git branch -v

# Mesclar branch
$ git merge nome-da-branch

# Excluir branch
$ git branch -d nome-da-branch
```

### Diferenças entre branches:
```bash
$ git diff branch1 branch2
```

### Clonar branch específica:
```bash
$ git clone <URL> --branch nome-da-branch --single-branch
```

---

## 🧰 Stash (Salvar alterações temporárias)
```bash
$ git stash         # Guardar modificações
$ git stash list    # Listar stashes
$ git stash pop     # Aplicar e remover
$ git stash apply   # Aplicar e manter
```

---

> 📅 **Observação Final:**
> Este guia foi baseado no curso de versionamento de código com git e github da DIO. Concluído em julho de 2025 [certificado](https://hermes.dio.me/certificates/7HQLIVLQ.pdf)