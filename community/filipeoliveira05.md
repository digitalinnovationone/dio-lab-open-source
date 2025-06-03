# filipeoliveira05 - Guia de Comandos Git

Este documento contém uma lista dos comandos Git mais comuns e as suas descrições. O Git é um sistema de controlo de versões distribuído amplamente utilizado para rastrear alterações no código-fonte.

---

## Configuração Inicial

```bash
git config --global user.name "O Teu Nome"
```
Define o nome de utilizador para todos os repositórios no teu sistema.

```bash
git config --global user.email "o.teu.email@example.com"
```
Define o email associado ao nome de utilizador.

---

## Inicialização e Clonagem

```bash
git init
```
Inicializa um novo repositório Git local.

```bash
git clone <url-do-repo>
```
Clona um repositório remoto para o teu computador.

---

## Estado e Registo

```bash
git status
```
Mostra o estado atual do repositório, incluindo ficheiros modificados e ficheiros prontos para commit.

```bash
git log
```
Mostra o histórico de commits do repositório.

---

## Adicionar e Cometer

```bash
git add <nome-do-ficheiro>
```
Adiciona um ficheiro específico à área de staging.

```bash
git add .
```
Adiciona todas as alterações à área de staging.

```bash
git commit -m "Mensagem do commit"
```
Confirma as alterações na branch atual com uma mensagem descritiva.

---

## Branching e Merging

```bash
git branch
```
Lista todas as branches no repositório.

```bash
git branch <nome-da-branch>
```
Cria uma nova branch.

```bash
git checkout <nome-da-branch>
```
Muda para a branch especificada.

```bash
git merge <nome-da-branch>
```
Faz merge da branch especificada na branch atual.

---

## Atualização e Publicação

```bash
git pull
```
Atualiza a branch local com as alterações do repositório remoto.

```bash
git push origin <nome-da-branch>
```
Envia as alterações para o repositório remoto na branch especificada.

---

## Reverter Alterações

```bash
git checkout -- <nome-do-ficheiro>
```
Descarta alterações locais no ficheiro especificado.

```bash
git reset --soft HEAD~1
```
Reverte o último commit, mantendo as alterações na área de staging.

```bash
git reset --hard HEAD~1
```
Reverte o último commit e descarta todas as alterações associadas.

---

## Remover Ficheiros

```bash
git rm <nome-do-ficheiro>
```
Remove um ficheiro do repositório e da área de staging.

```bash
git rm --cached <nome-do-ficheiro>
```
Remove um ficheiro apenas da área de staging, mantendo-o no diretório local.

---

## Tags

```bash
git tag <nome-da-tag>
```
Cria uma tag para marcar um ponto específico na história do repositório.

```bash
git push origin <nome-da-tag>
```
Envia a tag para o repositório remoto.

---

## Utilização com SSH

```bash
ssh-keygen -t ed25519 -C "o.teu.email@example.com"
```
Gera uma nova chave SSH (substitui `ed25519` por `rsa` se necessário).

```bash
ssh-add ~/.ssh/<nome-da-chave>
```
Adiciona a chave SSH ao agente SSH.

---

## Ajuda

```bash
git help <comando>
```
Mostra a documentação detalhada para o comando especificado.
