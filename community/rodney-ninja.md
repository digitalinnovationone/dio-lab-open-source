# Contribuição | Aplicação das ferramentas Git e Github.

 Resumo básico dos comandos do Git e Github do curso praticado nas aulas de Git e Github, do curso: Versionamento de código com Git e Github [Santander Bootcapm 2024](https://web.dio.me/home)

## 📙 Links dos sites
 - [Link da página Git](https://git-scm.com/doc)

 - [Link do site Github](https://docs.github.com/pt)


## 💻 Resumos das aulas 1

| Aulas 1 | Resumos |
|-------|---------|
| Git config - Utilizado para configurar nome, e-mail ou remover ou redifinir dados sobre o usuário e armazenamento de credenciais| [Resumos](https://git-scm.com/docs/git-config)  


```
Exemplo:
git config --global user.name "nome e/ou sobrenome"
git config --global user.email meuprojetp@email.com
git config edit
git config rename-section
git config remove-section

Exemplos de Credential helpers
git config --global credential.helper store ou cache
```

## Aula 2 | Resumo |

| Aulas 2 | Resumos |
|-------|---------|
| Criar um repositório local e, criar o repositório no diretório do Github| [Resumos](https://git-scm.com/docs/git-init) 

```
Exemplos de comando para iniciar um projeto:
git init  - abre um novo repositório - projeto- no Git.

Exemplo de criar um repositório remoto no Github:
git remote add origin
```

## Aula 3 | Resumo |

| Aulas 3 | Resumos |
|-------|---------|
| Clonar um repositório no própio Git| [Resumos](https://git-scm.com/docs/git-clone) 


```
Exemplo do comando de clonagem:
git clone https://git.thub.com/username/nome-do-repositorio 

Obs: para criação da clonagem é preciso abrir o repositório no Github e, deve-se adicionar o https do repositório do Github
```
## Aula 4 | Resumo |

| Aulas 4 | Resumos |
|-------|---------|
| Criar commits - SAlva as alterações do projeto| [Resumos](https://git-scm.com/docs/git-commit)

exemplos de de commits:
git commit -m "mensagem"
git commit -a "mensagem"
docs - altera documentos como README nos projetos entre outros.



 ## 🔍 Referências
 - [Santander Bootcamp] Curso DIO.

 - [https://git-scm.com/doc]
 - [https://docs.github.com/pt]
 - [https://git-scm.com/docs/git-config]
 - [https://git-scm.com/docs/git-init]
 - [https://git-scm.com/docs/git-clone]
