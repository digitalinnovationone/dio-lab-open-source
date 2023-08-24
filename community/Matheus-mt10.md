# Olá, eu sou o Matheus! 👋

## 🚀 Sobre mim
Eu sou uma pessoa desenvolvedora full-stack. Estudante de Análise e desenvolvimento de sistemas, Atualmente trabalhando com a área de ensino atuando como instrutor de tecnologia. 

Busco adquirir conhecimentos sólidos atraves da minha graduação, com Bootcamps, cursos gratuitos ou mesmo conversando com profissionais que já estão na área paara trocar informações e experiencias 


## Resuminho...

👩‍💻 Trabalho atualmente na...

    - área de ensino, atuando como instrutor de tecnologia.

🧠 Estou aprendendo...

    - Java
    - Angular
    - Javascrip

🤔 Procuro ajuda com...

    - As tecnologias que estou estudando rsrs

📫 Como entrar em contato comigo...

    - matheus.info29@gmail.com


⚡️ Fatos curiosos...

    No meu tempo livre gosto de produzir beats usando o FL Studio

## Ferramentas e Tecnologias

<div>
    <img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40" height="40"/>
    <img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="40"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original-wordmark.svg" width="40"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-plain.svg" width="40" />
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/angularjs/angularjs-original.svg" width="40" />
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg"  width="40" />
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/canva/canva-original.svg" width="40" />
</div>

## Estou aprendendo
<div>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original-wordmark.svg" width="40"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-plain.svg" width="40" />
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/angularjs/angularjs-original.svg" width="40" />
</div>

## Estatísticas do GitHub
<div>
<a href="https://github.com/Matheus-mt10">
<img loading="lazy" height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Matheus-mt10&layout=compact&langs_count=7&theme=dracula"/> 

<img loading="lazy" height="180em" src="https://github-readme-stats.vercel.app/api?username=Matheus-mt10&show_icons=true&theme=dracula&include_all_commits=true&count_private=true"/>
</div>

## Contatos:

<div>
<a href="https://www.youtube.com/seu-canal-youtube-aqui" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" target="_blank"></a>
<a href="https://www.instagram.com/_theussantana/" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
</a>
<a href = "mailto:matheus.info29@gmail.com"><img loading="lazy" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
<a href="https://www.linkedin.com/in/matheus-santana-dev" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>   
</div>

![Snake animation](https://github.com/Matheus-mt10/Matheus-mt10/blob/output/github-contribution-grid-snake.svg)
          
name: Generate Datas

on:
  schedule: # execute every 12 hours
    - cron: "* */12 * * *"
  workflow_dispatch:

jobs:
  build:
    name: Jobs to update datas
    runs-on: ubuntu-latest
    steps:
      # Snake Animation
      - uses: Platane/snk@master
        id: snake-gif
        with:
          github_user_name: Matheus-mt10
          svg_out_path: dist/github-contribution-grid-snake.svg

      - uses: crazy-max/ghaction-github-pages@v2.1.3
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          

- uses: Platane/snk@v3
  with:
    # github user name to read the contribution graph from (**required**)
    # using action context var `github.repository_owner` or specified user
    github_user_name: ${{ github.repository_owner }}

    # list of files to generate.
    # one file per line. Each output can be customized with options as query string.
    #
    #  supported options:
    #  - palette:     A preset of color, one of [github, github-dark, github-light]
    #  - color_snake: Color of the snake
    #  - color_dots:  Coma separated list of dots color.
    #                 The first one is 0 contribution, then it goes from the low contribution to the highest.
    #                 Exactly 5 colors are expected.
    outputs: |
      dist/github-snake.svg
      dist/github-snake-dark.svg?palette=github-dark
      dist/ocean.gif?color_snake=orange&color_dots=#bfd6f6,#8dbdff,#64a1f4,#4b91f1,#3c7dd9

  env:
    
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}