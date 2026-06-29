# 🤝 GitHub Cheat Sheet

## 📂 Clonando o Repositório
```bash
git clone https://github.com/organizacao/repositorio.git
cd repositorio
```

## 🌱 Criando uma Branch para Trabalhar
```bash
git checkout -b feature/nome-da-funcionalidade
```

## 🔄 Ciclo de Trabalho
```bash
git add .                           # Adiciona mudanças
git commit -m "feat: nova função X" # Commit com padrão de convenção
git push origin feature/nome-da-funcionalidade
```

## 📬 Criando um Pull Request (PR)
1. Vá até o GitHub.
2. Clique em **"Compare & pull request"**.
3. Preencha o título e a descrição com o que foi feito.
4. Selecione revisores e assigne alguém se necessário.
5. Clique em **"Create pull request"**.

## ✅ Revisando um PR
- Comente diretamente em trechos do código.
- Use **"Approve"**, **"Request changes"** ou **"Comment"**.
- Após aprovação, use o botão **"Merge pull request"** (caso tenha permissão).

## 🔄 Mantendo sua Branch Atualizada
```bash
git checkout main
git pull origin main
git checkout feature/nome-da-funcionalidade
git rebase main                    # OU git merge main
```

## 🧼 Deletando Branch após o Merge
```bash
git branch -d feature/nome         # Local
git push origin --delete feature/nome  # Remoto
```

## 📝 Boas Práticas em Equipe
- Nomeie branches com o padrão: `feature/`, `bugfix/`, `hotfix/`.
- Use commits claros e com prefixos como `feat:`, `fix:`, `docs:`, `refactor:`.
- Sempre crie uma branch nova a partir da `main` ou `develop`.
- Crie PRs pequenos e objetivos.
- Revise e comente no código dos colegas.
- Use `issues` para documentar tarefas e bugs.

---

## 📁 Estrutura de Arquivos Úteis
- `README.md` – Instruções do projeto.
- `CONTRIBUTING.md` – Regras para contribuir (se existir).
- `.gitignore` – Arquivos a ignorar.
- `CODEOWNERS` – Define revisores obrigatórios.

