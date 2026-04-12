
# 👋 Olá, eu sou [André]!  

## 🚀 Sobre mim  
- 🎓 Formação: [Técnologo em ADS e Bacharelado em Eng. Civil]  
- 🌱 Atualmente aprendendo: [Tudo sobre IAs e desenvolvimento]  
- 🎯 Interesses: [Tudo sobre tecnologia, música, filmes, jogos etc...]  
  

## 🛠️ Tecnologias & Ferramentas  
- 💻 Linguagens: `JavaScript`, `Python`, `C#`, `Java`  
- 🛠️ Ferramentas: `Git`, `Docker`, `Postman`, `VS Code`  
- 📊 Banco de Dados: `MySQL`, `PostgreSQL`, `MongoDB`  

## 📈 Estatísticas do GitHub  
![Estatísticas do GitHub](https://github-readme-stats.vercel.app/api?username=AndreParise&show_icons=true&theme=dracula)  

## 📌 Projetos  
- 🔗 [Projeto 1 - Nome do Projeto]()  
- 🔗 [Projeto 2 - Nome do Projeto]()  

## 🌎 Onde me encontrar  
- 📧 Email: [Seu Email]  


## Aqui está a explicação detalhada de cada comando e ação do desafio da DIO:  

### 1. **Faça um Fork deste repositório**  
- O "fork" cria uma cópia do repositório original na sua conta do GitHub. Isso permite que você faça alterações sem modificar o repositório original.  
- Para isso, vá até o repositório original no GitHub e clique no botão **Fork** no canto superior direito.  

---

### 2. **Clone localmente**  
bash
git clone https://github.com/SEUUSERNAME/dio-lab-open-source.git

- Esse comando copia o repositório que você fez o fork para o seu computador.  
- Ele baixa todos os arquivos e mantém uma conexão com seu repositório remoto no GitHub.  

---

### 3. **Adicione o remote upstream**  
bash
git remote add upstream https://github.com/digitalinnovationone/dio-lab-open-source.git

- Aqui, você adiciona um novo "remote" chamado **upstream** que aponta para o repositório original.  
- Isso permite que você mantenha seu repositório atualizado com o código mais recente do original.  

---

### 4. **Atualize seu repositório local**  
bash
git pull upstream main

- Esse comando baixa e mescla (merge) as alterações mais recentes do repositório original (upstream) para o seu repositório local.  

**Alternativamente:**  
bash
git fetch upstream main

- Esse comando **apenas baixa** as alterações, mas não mescla com seu código. Você precisaria fazer isso manualmente depois.  

---

### 5. **Crie uma nova branch**  
bash
git checkout -b feat/community/seunomedeusuario

- Cria uma nova branch com o nome feat/community/seunomedeusuario e já muda para essa branch.  
- "feat" é uma convenção que indica que essa branch contém uma nova funcionalidade (feature).  

---

### 6. **Crie um arquivo Markdown dentro da pasta "community"**  
- Navegue até a pasta community e crie um arquivo .md com o mesmo nome do seu usuário no GitHub.  
- Exemplo: falvojr.md.  

---

### 7. **Desenvolva o seu perfil**  
- Adicione informações sobre você ao arquivo .md.  
- Você pode usar os exemplos dentro da pasta community como referência.  

---

### 8. **Adicione o arquivo à "staging area"**  
bash
git add community/seunomedeusuario.md

- Esse comando adiciona o arquivo modificado ao "staging area", preparando-o para o commit.  

---

### 9. **Crie um commit com mensagem explicativa**  
bash
git commit -m "feat: add seunomedeusuario profile"

- Esse comando salva as alterações localmente com uma mensagem descritiva.  
- "feat" indica que foi adicionada uma nova funcionalidade.  

---

### 10. **Envie as alterações para o repositório remoto**  
bash
git push origin feat/community/seunomedeusuario

- Esse comando envia suas alterações para o repositório remoto no GitHub, na branch feat/community/seunomedeusuario.  

---

### 11. **Crie um Pull Request (PR)**  
- Vá até o GitHub, acesse o seu repositório e clique no botão **Compare & pull request**.  
- Isso solicita a inclusão do seu código no repositório original.  
- Aguarde a aprovação do mantenedor do repositório.  

---
