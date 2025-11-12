#Franklin Canduri

💻Estudante de Engenharia da Computação
📊Cientista de Dados
🗄️Engenheiro de Dados
☁️Desenvolvedor em Nuvem
🐍Desenvolvedor Python e ☕ Java

GitHub: [https://github.com/CanduriFranklin](https://github.com/CanduriFranklin)
LinkedIn: [https://www.linkedin.com/in/franklin-canduri-335576227/](https://www.linkedin.com/in/franklin-canduri-335576227/)

---

## 📘 Guia Profissional de Git e GitHub

Este repositório foi desenvolvido para fins educacionais, fornecendo materiais de apoio e exercícios práticos para ajudar desenvolvedores a dominar Git e GitHub.

Ele foi projetado para servir como um **guia de referência** tanto para iniciantes quanto para usuários avançados.

---

## 🎯 Motivação para esta contribuição

A principal razão para esta contribuição é:

- **Compartilhar conhecimento** sobre Git e GitHub de forma estruturada e acessível.

- **Apoiar a comunidade de desenvolvedores** com recursos práticos.

- **Incentivar a colaboração** e as melhores práticas em projetos de código aberto.

# Guia Profissional de Git e GitHub


---

## 📖 Introdução
**Git** é um sistema de controle de versão distribuído amplamente utilizado para rastrear alterações em arquivos e coordenar o trabalho em projetos de software.  
**GitHub** é uma plataforma baseada em nuvem que utiliza Git para hospedar repositórios e facilitar a colaboração entre desenvolvedores.

---

## 🔑 Conceitos Fundamentais

### O que é Git?
Git é um sistema de controle de versão distribuído criado por **Linus Torvalds em 2005** para gerenciar o kernel Linux.  
É conhecido por sua **eficiência, confiabilidade** e suporte para fluxos de trabalho **não lineares**.  

📚 Documentação oficial: [Git Documentation](https://git-scm.com/doc)

### O que é GitHub?
GitHub é uma plataforma que utiliza Git para hospedar repositórios de código.  
Além do armazenamento, oferece ferramentas de colaboração como **pull requests, issues, code reviews e GitHub Actions**.  

📚 Documentação oficial: [GitHub Docs](https://docs.github.com/)

---

## ⚙️ Características do Git
- Distribuído: cada desenvolvedor possui uma cópia completa do histórico.  
- Rápido: operações como commits, diffs e merges são locais.  
- Seguro: utiliza SHA-1 para garantir integridade.  
- Flexível: suporta múltiplos fluxos de trabalho e integrações.  

## 🌐 Características do GitHub
- Colaboração: pull requests, code reviews e discussões.  
- Integração contínua: automação com GitHub Actions.  
- Documentação: suporte a wikis e READMEs.  
- Comunidade: milhões de projetos e desenvolvedores ativos.  

📚 Guia de README: [GitHub - About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)  
📚 Guia de Repositórios: [GitHub - About Repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)

---

## ⚙️ Configuração Inicial do Git

Antes de começar a usar o Git, configure sua identidade e credenciais:

```bash
# Definir nome de usuário
git config --global user.name "Seu Nome"

# Definir e-mail
git config --global user.email "seuemail@exemplo.com"

# Verificar configurações
git config --list

# Configurar cache temporário de credenciais
git config --global credential.helper cache

# Configurar armazenamento de credenciais (texto simples)
git config --global credential.helper store
⚠️ Nota: Para ambientes profissionais, recomenda-se usar o Git Credential Manager ou chaves SSH para maior segurança.

📝 Comandos Básicos do Git
bash
# Inicializar um repositório
git init

# Clonar um repositório
git clone <url-do-repositorio>

# Verificar status
git status

# Adicionar arquivos
git add <arquivo>

# Fazer commit
git commit -m "Mensagem do commit"

# Enviar alterações
git push origin <nome-do-branch>
🚀 Comandos Avançados do Git
bash
# Histórico de commits
git log

# Criar e alternar branch
git checkout -b <nome-do-branch>

# Mesclar branches
git merge <nome-do-branch>

# Resolver conflitos
git status
git add <arquivo>
git commit

# Reverter commit
git revert <hash-do-commit>

# Resetar para estado anterior
git reset --hard <hash-do-commit>
✅ Boas Práticas
Commits pequenos e frequentes.

Mensagens de commit claras e descritivas.

Branches separados para novas funcionalidades.

Revisões de código antes de merges.

📚 Guia oficial: GitHub Flow

🛠️ Recursos Adicionais do GitHub
GitHub CLI: gerencie repositórios e PRs pelo terminal → GitHub CLI Docs

GitHub Copilot: sugestões inteligentes de código → GitHub Copilot Docs

GitHub Sponsors: apoio financeiro para projetos open source → GitHub Sponsors

🎯 Motivação desta Contribuição
Este guia foi criado com os seguintes objetivos:

Facilitar o aprendizado de Git e GitHub.

Promover boas práticas de versionamento e colaboração.

Servir como referência rápida para comandos essenciais.

Contribuir com a comunidade oferecendo material acessível e organizado.

Inspirar desenvolvedores a explorar documentação oficial e projetos similares.

📌 Conclusão
Git e GitHub são ferramentas indispensáveis para equipes modernas. Com Git, você controla o histórico de forma eficiente. Com GitHub, você amplia a colaboração e integra automações que aceleram o desenvolvimento.