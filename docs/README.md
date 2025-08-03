<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> Profiles README DIO</span>
</h1>

## Sobre o Projeto
Página desenvolvida para fins didáticos para o curso **Contribuindo em um Projeto Open Source no GitHub** da [Digital Innovation One](https://www.dio.me/). Lembre-se de que Markdown é mais voltado para a documentação e apresentação de texto formatado, enquanto a remoção de bugs normalmente envolve a compreensão detalhada do código e o uso de ferramentas de desenvolvimento adequadas à linguagem de programação específica.

[![Preview](https://img.shields.io/badge/Preview-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://digitalinnovationone.github.io/dio-lab-open-source/)

```
docs/
├── assets/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
├── favicon.ico
├── index.html
└── README.md
```

## Tecnologias
![HTML](https://img.shields.io/badge/HTML-000?style=for-the-badge&logo=html5&logoColor=30A3DC)
![CSS](https://img.shields.io/badge/CSS-000?style=for-the-badge&logo=css3&logoColor=E94D5F)
![JavaScript](https://img.shields.io/badge/JavaScript-000?style=for-the-badge&logo=javascript&logoColor=30A3DC)

 ---
# Melhorando a Segurança do Token
Primeiro, a melhoria que vamos fazer no código é garantir que o token de segurança não esteja diretamente no código, mas sim em uma variável de ambiente.

Criando uma Variável de Ambiente para o Token
No seu sistema operacional, você deve definir uma variável de ambiente para armazenar o token de segurança. Aqui está como fazer isso:

No Windows:

Abra o Prompt de Comando ou PowerShell.

Use o comando abaixo para definir uma variável de ambiente temporária (essa variável ficará ativa apenas durante a sessão do terminal atual):

```setx GITHUB_TOKEN "seu_token_aqui"```

Se você preferir definir uma variável de ambiente temporária, sem a necessidade de reiniciar o terminal, use:

```set GITHUB_TOKEN="seu_token_aqui"```

No macOS/Linux:

Abra o terminal e edite o arquivo .bashrc ou .zshrc (dependendo do seu shell) para adicionar a variável permanentemente.

Para isso, abra o arquivo com um editor de texto:

```nano ~/.bashrc   # Ou ~/.zshrc, se você estiver usando Zsh```

Adicione a linha abaixo no final do arquivo:

```export GITHUB_TOKEN="seu_token_aqui"```

Salve e feche o arquivo. Após isso, execute o comando:

```source ~/.bashrc  # Ou ~/.zshrc```









