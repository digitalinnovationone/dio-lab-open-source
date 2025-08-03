# Guia de Comandos Git para Iniciantes 🚀

Pensando em minha situação atual, como mero aprendiz que sou, e em como é difícil começar algo novo, resolvi compartilhar um guia simples com os comandos Git mais usados.

Feito com ❤️ por Leonardo Silva (@Kamoniery)

---

## 📦 Iniciando um repositório

1. Cria um novo repositório Git local na pasta atual:
   
	 git init

2. Clona um repositório remoto  do GitHub para sua máquina local:

	git clone <url-do-repositorio>

---

📄 Status e histórico

1.  Mostra o estado atual do repositório (arquivos modificados, prontos para commit, etc):

	git status

2. Exibe o histórico de commits no terminal:

	git log

3. Exibe o histórico de forma resumida e visual:

	git log --oneline --graph --all

---

✍️ Salvando alterações

1. Adiciona um arquivo específico à staging area (pronto para commit):

	git add <arquivo>

2. Adiciona todos os arquivos modificados:

	git add .

3. Salva as alterações com uma mensagem explicativa:

	git commit -m "Mensagem do commit"

---

🔄 Sincronizando com o repositório remoto

1. Puxa as alterações do repositório remoto para o seu repositório local:

	git pull

2. Puxa as alterações e reordena seus commits por cima dos novos:

	git pull --rebase

3. Envia suas alterações locais para o repositório remoto:

	git push

---

🌱 Trabalhando com branches

1. Lista todos os branches:

	git branch

2. Cria uma nova branch:

	git branch nome-da-branch

3. Muda para a branch especificada:

	git checkout nome-da-branch

4. Cria e muda para a nova branch:

	git checkout -b nova-branch

---

🔗 Conectando repositórios remotos

1. Define o repositório remoto com o nome origin:

	git remote add origin <url>

2. Lista os repositórios remotos conectados:

	git remote -v

3. Adiciona o repositório original (por exemplo, da DIO) como upstream:

	git remote add upstream <url>

---

🧹 Comandos úteis de limpeza e correção

1. Salva temporariamente alterações não commitadas (ideal para trocar de branch sem perder progresso):

	git stash

2. Remove todas as alterações locais e volta ao último commit:

	git reset --hard

3. Remove arquivos e diretórios não rastreados (⚠️ cuidado!):

	git clean -fd

---

✅ Dicas extras

1. Sempre verifique git status antes de usar comandos críticos.

2. Use git log --oneline para entender sua linha do tempo de commits.

3. Faça commits pequenos e frequentes.

4. Use mensagens claras e descritivas nos commits. 

Muito obrigado por ler até aqui! Espero que este guia ajude você tanto quanto tem me ajudado. 😊

