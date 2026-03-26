# Digital Innovation - Trilha Python 🐍 </br> 
> Dicas de uso sobre a funcionalidade Projects do GitHub

---

O **GitHub Projects** é uma ferramenta que auxilia no **gerenciamento de tarefas** e no **acompanhamento de issues e pull requests** diretamente dentro do repositório. 

Excelente para mapear as atividades durante o desenvolvimento do projeto, pois permite ter uma visão **KanBan**.

---

## 🔹 Benefícios principais
- Organização das **issues** e **pull requests**.  
- Melhor visibilidade do progresso do projeto.  
- Possibilidade de criar **automação de tarefas**.  
- Integração direta com o fluxo de commits e merges.  

---

## 🚀 Exemplo prático

1. Criar uma **issue** no repositório.  
2. Associar essa issue a um **Project**.  
3. Criar um **branch** com o número da issue.  
4. Realizar commits referenciando a issue (`refs #1` ou `closes #1`).  
5. Abrir um **Pull Request** → ao ser mergeado, a issue é fechada automaticamente.  

---

## 💻 Comandos básicos do fluxo

```bash
# Criar um branch a partir do main
git checkout main
git pull origin main
git checkout -b 1-configuracao

# Adicionar alterações
git add .

# Commitar referenciando a issue #1
git commit -m "Adiciona configuração inicial (closes #1)"

# Enviar branch para o GitHub
git push origin 1-configuracao
```


## Acompanhamento
</br>

![GitHub issues](https://img.shields.io/github/issues/silva-alexandre/dio-lab-open-source?style=for-the-badge&logo=github)
![GitHub pull requests](https://img.shields.io/github/issues-pr/silva-alexandre/dio-lab-open-source?style=for-the-badge&logo=git)
![GitHub forks](https://img.shields.io/github/forks/silva-alexandre/dio-lab-open-source?style=for-the-badge&logo=github)
![GitHub stars](https://img.shields.io/github/stars/silva-alexandre/dio-lab-open-source?style=for-the-badge&logo=github)
</br>

![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
