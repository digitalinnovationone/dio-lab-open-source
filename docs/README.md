<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> Profiles README DIO</span>
</h1>

## Sobre o Projeto
Página desenvolvida para fins didáticos para o curso **Contribuindo em um Projeto Open Source no GitHub** da [Digital Innovation One](https://www.dio.me/). Lembre-se de que Markdown é mais voltado para a documentação e apresentação de texto formatado, enquanto a remoção de bugs normalmente envolve a compreensão detalhada do código e o uso de ferramentas de desenvolvimento adequadas à linguagem de programação específica.

[![Preview](https://img.shields.io/badge/Preview-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://digitalinnovationone.github.io/dio-lab-open-source/)

# Comandos Básicos do Git

## Criando e Inicializando o Repositório

| Comando                          | Descrição |
|----------------------------------|-----------|
| `mkdir nome_da_pasta`           | Cria uma nova pasta. |
| `git init`                       | Inicializa um repositório Git na pasta atual. |
| `git status`                     | Mostra o estado atual dos arquivos no repositório. |
| `touch README.md`                | Cria um arquivo `README.md`. |

## Adicionando Arquivos ao Git

| Comando                          | Descrição |
|----------------------------------|-----------|
| `git add .`                      | Adiciona todos os arquivos ao controle do Git. |
| `git add nome_arquivo.extensao`  | Adiciona apenas um arquivo específico. |
| `git commit -m "mensagem"`       | Cria um commit com a mensagem informada. |

## Histórico e Reversão

| Comando                          | Descrição |
|----------------------------------|-----------|
| `git log`                        | Exibe o histórico de commits. |
| `git restore nome_arquivo`       | Restaura o arquivo para o estado antes da modificação. |
| `git commit --amend -m "nova mensagem"` | Modifica a mensagem do último commit. |
| `git reset --hard nome_do_commit` | Apaga todas as alterações até um commit específico. |
| `git reset --soft nome_do_commit` | Reverte o commit sem perder os arquivos locais. |
| `git reset --mixed nome_do_commit` | Remove commits mas mantém as alterações no diretório. |
| `git reset nome_do_arquivo`      | Remove um arquivo da área de staging. |
| `git restore --staged nome_do_arquivo` | Remove um arquivo da área de staging sem perder as alterações. |
| `git stash`                      | Salva as mudanças temporariamente sem fazer commit. |

## Trabalhando com Repositórios Remotos

| Comando                          | Descrição |
|----------------------------------|-----------|
| `git remote add origin nome_do_repositorio` | Conecta o repositório local ao GitHub. |
| `git push -u origin main`        | Envia os arquivos para o repositório remoto. |
| `git pull`                       | Atualiza o repositório local com as mudanças do remoto. |
| `git fetch origin main`          | Baixa as atualizações do repositório remoto sem mesclar. |
| `git merge origin/main`          | Mescla as atualizações do repositório remoto. |
| `git diff main origin/main`      | Mostra as diferenças entre a branch local e remota. |
| `git clone ENDEREÇO_HTTP --branch nome_da_branch --single-branch` | Clona apenas uma branch específica. |

## Trabalhando com Branches

| Comando                          | Descrição |
|----------------------------------|-----------|
| `git checkout -b nome_da_branch` | Cria e muda para uma nova branch. |
| `git checkout nome_da_branch`    | Alterna para uma branch específica. |
| `git checkout main`              | Retorna para a branch principal. |
| `git branch -v`                  | Lista as branches e suas últimas alterações. |
| `git merge nome_da_branch`       | Mescla uma branch na `main`. |
| `git branch -d nome_da_branch`   | Deleta uma branch após o merge. |
| `git checkout commit_hash -- nome_do_arquivo` | Restaura um arquivo para uma versão específica do commit. |
