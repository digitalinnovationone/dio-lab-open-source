# Segue um resumo dos comandos **Git** mais utilizados, direto ao ponto.


---

# Comandos Git Essenciais

Este **README** apresenta um resumo dos comandos Git mais frequentemente utilizados para o controle de versão de projetos.

## 1. Configuração Inicial

Antes de começar, configure seu nome de usuário e e-mail no Git:

* **`git config --global user.name "Seu Nome"`**
    * Define o nome do autor que será exibido em seus commits.
* **`git config --global user.email "seu.email@example.com"`**
    * Define o e-mail do autor que será associado aos seus commits.

---

## 2. Iniciar e Clonar Repositórios

* **`git init`**
    * Inicializa um novo repositório Git no diretório atual. Essencial para começar a versionar um projeto do zero.
* **`git clone <url_do_repositorio>`**
    * Clona um repositório existente de uma URL remota para o seu computador local.

---

## 3. Adicionar e Commitatar Mudanças

* **`git status`**
    * Mostra o estado atual da sua árvore de trabalho, incluindo arquivos modificados, adicionados e não rastreados.
* **`git add <nome_do_arquivo>`**
    * Adiciona um arquivo específico para a "staging area" (área de preparação), que é a próxima etapa antes de commitar as mudanças.
* **`git add .`**
    * Adiciona todos os arquivos modificados e novos (no diretório atual e subdiretórios) para a staging area.
* **`git commit -m "Mensagem do commit"`**
    * Registra as mudanças que estão na staging area no histórico do repositório. A mensagem é crucial para descrever as alterações.
* **`git commit -am "Mensagem do commit"`**
    * Atalho para adicionar e commitar arquivos que já estão sendo rastreados pelo Git (não funciona para arquivos novos).

---

## 4. Visualizar Histórico e Diferenças

* **`git log`**
    * Exibe o histórico de commits do repositório, mostrando o autor, data e mensagem de cada commit.
* **`git log --oneline`**
    * Exibe o histórico de commits de forma concisa, uma linha por commit.
* **`git diff`**
    * Mostra as diferenças entre o diretório de trabalho e a staging area.
* **`git diff --staged`**
    * Mostra as diferenças entre a staging area e o último commit.
* **`git diff <commit1> <commit2>`**
    * Mostra as diferenças entre dois commits específicos.

---

## 5. Ramificação (Branching)

* **`git branch`**
    * Lista todas as branches locais no repositório.
* **`git branch <nome_da_branch>`**
    * Cria uma nova branch com o nome especificado.
* **`git checkout <nome_da_branch>`**
    * Muda para a branch especificada, permitindo trabalhar nela.
* **`git checkout -b <nome_da_nova_branch>`**
    * Cria uma nova branch e já muda para ela.
* **`git branch -d <nome_da_branch>`**
    * Exclui a branch local especificada (somente se ela já foi mergeada).
* **`git branch -D <nome_da_branch>`**
    * Exclui a branch local especificada, forçando a exclusão mesmo se não foi mergeada.

---

## 6. Fusão (Merging) e Rebase

* **`git merge <nome_da_branch>`**
    * Combina as mudanças da branch especificada na branch atual.
* **`git rebase <nome_da_branch>`**
    * Reescreve o histórico de commits da branch atual, aplicando seus commits "em cima" dos commits da branch especificada.

---

## 7. Repositórios Remotos

* **`git remote -v`**
    * Lista as URLs dos repositórios remotos configurados.
* **`git remote add origin <url_do_repositorio>`**
    * Adiciona um repositório remoto com o nome "origin" e a URL especificada.
* **`git push -u origin <nome_da_branch>`**
    * Envia os commits da branch local para o repositório remoto. O `-u` define o upstream para futuras operações de push e pull.
* **`git pull origin <nome_da_branch>`**
    * Baixa as mudanças do repositório remoto e as mescla na branch local.
* **`git fetch origin`**
    * Baixa as informações do repositório remoto, mas não mescla as mudanças na branch local.

---

## 8. Desfazer Mudanças

* **`git reset <nome_do_arquivo>`**
    * Desfaz o `git add` de um arquivo, movendo-o da staging area de volta para o diretório de trabalho.
* **`git reset --hard <hash_do_commit>`**
    * Desfaz todas as mudanças **permanentemente** até o commit especificado, descartando qualquer alteração não commitada. **Use com extrema cautela!**
* **`git revert <hash_do_commit>`**
    * Cria um novo commit que desfaz as mudanças de um commit anterior, mantendo o histórico de commits intacto.
* **`git restore <nome_do_arquivo>`** (Git 2.23+)
    * Desfaz as mudanças não stageadas em um arquivo, restaurando-o para a versão do último commit.
* **`git restore --staged <nome_do_arquivo>`** (Git 2.23+)
    * Remove um arquivo da área de staging, semelhante ao `git reset <nome_do_arquivo>`.

---

Este resumo deve cobrir a maioria das suas necessidades diárias com Git! Para mais detalhes, consulte a documentação oficial do Git.
