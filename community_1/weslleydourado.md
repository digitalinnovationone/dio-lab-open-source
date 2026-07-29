# Mini Tutorial Git: 6 passos para enviar seu projeto para o GitHub

Um passo a passo para usar o git e githut rápido e fácil. Em 6 passos envie um projeto para o GitHub.

## Vamos Começar!

Estas instruções darão a você os conceitos e aplicações práticas iniciais do Git, capaz de tornar seu projeto públicamente acessível no GitHub.

### Requisitos

[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://docs.github.com/)
[![Git](https://img.shields.io/badge/Git-000?style=for-the-badge&logo=git&logoColor=E94D5F)](https://git-scm.com/doc)

Requer o software git intalado no seu computador 
- [Baixar o Git](https://git-scm.com/downloads) de acordo com a versão do OS você utiliza.

Url:

    https://git-scm.com/downloads

![alt text](image-2.png)

### Git Prático

Um passo a passo para usar o git e githut rápido e fácil.

### 1. Intalação do Git

Acesse o [site oficial](https://git-scm.com/downloads) e faça o download do instalador Git.
Retorne ao tópico requisitos. 

### 2. Configurações iniciais

Terminal:
```
git config --global user.name "<seu nome>"
git config --global user.email "<emailexemplo@dio.me>"
```

Terminal (verificar):
```
git config user.name
git config user.email
```

### 3. Criar novo repositório local Git

Terminal:
```
git init
```
Ou
### 3.1 Obter cópia de um repositório remoto para local

```
git clone https://github.com/nome-usuario/repositorio.git
```

### 4. Adicionar os arquivos 

Terminal:
```
git add .
```
Ou 

```
git add <nome-do-arquivo>
```

### Verificar o Status

Terminal:
```
git status
```

### 5. Comitar as mudanças adicionadas

Terminal:
```
git commit -m "sua-mensagem-da-ação"
```

### 6. Enviar para o GitHub

Terminal:
```
git remote add origin  https://github.com/seu-usuario/seu-repositorio.git
git push -u origin <branch-name> 
```

## Autor

  - **Weslley Dourado** - *Provided README community:*
  [dio-lab-open-source/community/weslleydourado.md](https://github.com/weslleydourado/dio-lab-open-source/blob/main/community/weslleydourado.md)

## License

Este projeto está licenciado pela a [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - consulte a [LICENSE.md](LICENSE.md) no arquivo para detalhes

## Para mais saber e conhecimento 

  * [e-Book Git <i>on-line</i> 2ed](https://git-scm.com/book/pt-br/v2) em Português.
  * [Tutorial Git](https://git-scm.com/docs/gittutorial) - A tutorial introduction to Git
