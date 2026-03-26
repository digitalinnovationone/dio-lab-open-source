[![README](https://img.shields.io/static/v1?label=readme&message=pt-BR&color=blue&style=plastic)](https://github.com/ewaldoMachado)

<h1 align="center">EWALDO MACHADO</h1>
<h3 align="center">Engenheiro de Software</h3>

### Sobre mim:

Sou um engenheiro de software por formação recente e músico profissional por quase duas décadas; uma trajetória que combina exatidão técnica com expressão criativa. Atualmente em transição de carreira, venho expandindo horizontes no universo de tecnologia descentralizada, aprofundando meus conhecimentos em *blockchain*, *web3* e inovações digitais emergentes. Essa mudança nasce do desejo de integrar minha experiência com sistemas e lógica à construção de soluções mais transparentes, seguras e colaborativas.

Minha jornada não é apenas sobre código ou notas musicais, mas sobre a busca constante por significado, inovação e impacto. Navego com naturalidade entre o pensamento lógico da engenharia e a sensibilidade  artística da música, construindo pontes entre diferentes dimensões do conhecimento humano.



### Linguagens e ferramentas mais utilizadas

<table align="center">
  <tr>
    <td align="center" width="96">
      <a href="https://developer.mozilla.org/docs/Web/CSS">
        <img src="https://skillicons.dev/icons?i=css" alt="icon" width="30" height="30"/>
      </a>
      <br>CSS
    </td>
    <td align="center" width="96">
      <a href="https://www.docker.com/">
        <img src="https://skillicons.dev/icons?i=docker" alt="icon" width="30" height="30"/>
      </a>
      <br>Docker
    </td>
    <td align="center" width="96">
      <a href="https://expressjs.com/">
        <img src="https://skillicons.dev/icons?i=express" alt="icon" width="30" height="30"/>
      </a>
      <br>Express
    </td>
    <td align="center" width="96">
      <a href="https://git-scm.com/">
        <img src="https://skillicons.dev/icons?i=git" alt="icon" width="30" height="30"/>
      </a>
      <br>Git
    </td>
    <td align="center" width="96">
      <a href="https://github.com/">
        <img src="https://skillicons.dev/icons?i=github" alt="icon" width="30" height="30"/>
      </a>
      <br>Github
    </td>
  </tr>
  <tr>
    <td align="center" width="96">
      <a href="https://developer.mozilla.org/docs/Web/HTML">
        <img src="https://skillicons.dev/icons?i=html" alt="icon" width="30" height="30"/>
      </a>
      <br>HTML
    </td>
    </td>
    <td align="center" width="96">
      <a href="https://www.javascript.com/">
        <img src="https://skillicons.dev/icons?i=js" alt="icon" width="30" height="30"/>
      </a>
      <br>Javascript
    </td>
    </td>
    <td align="center" width="96">
      <a href="https://www.mongodb.com/">
        <img src="https://skillicons.dev/icons?i=mongodb" alt="icon" width="30" height="30"/>
      </a>
      <br>Mongo
    </td>
    <td align="center" width="96">
      <a href="https://www.mysql.com/">
        <img src="https://skillicons.dev/icons?i=mysql" alt="icon" width="30" height="30"/>
      </a>
      <br>MySql
    </td>
    <td align="center" width="96">
      <a href="https://nodejs.org/">
        <img src="https://skillicons.dev/icons?i=nodejs" alt="icon" width="30" height="30"/>
      </a>
      <br>Node
    </td>
    </td>
  </tr>
  <tr>
    <td align="center" width="96">
      <a href="https://www.postgresql.org/">
        <img src="https://skillicons.dev/icons?i=postgres" alt="icon" width="30" height="30"/>
      </a>
      <br>Postgres
    </td>
    <td align="center" width="96">
      <a href="https://www.postman.com/">
        <img src="https://skillicons.dev/icons?i=postman" alt="icon" width="30" height="30"/>
      </a>
      <br>Postman
    </td>
    <td align="center" width="96">
      <a href="https://react.dev/">
        <img src="https://skillicons.dev/icons?i=react" alt="icon" width="30" height="30"/>
      </a>
      <br>React
    </td>
    <td align="center" width="96">
      <a href="https://code.visualstudio.com/docs">
        <img src="https://skillicons.dev/icons?i=vscode" alt="icon" width="30" height="30"/>
      </a>
      <br>VSCode
    </td>
    <td align="center" width="96">
      <a href="https://docs.soliditylang.org">
        <img src="https://skillicons.dev/icons?i=solidity" alt="icon" width="30" height="30"/>
      </a>
      <br>Solidity
    </td>
  </tr>
  <tr>
    </td>
  </tr>
</table>

### Conecte-se comigo

- Email pessoal:
  <a href="mailto:ewaldo2016@gmail.com">
  <img align="center" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" style="margin-left: 20px;">
  </a>

- Perfil Github:
  <a href="https://github.com/ewaldoMachado">
  <img align="center" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" style="margin-left: 25px;">
  </a>

- Perfil LinkedIn:
  <a href="https://www.linkedin.com/in/ewaldo-machado-dev">
  <img align="center" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="margin-left: 20px;">
  </a>

<br>

# Sugestão de implementação

# Agente de respostas

Com **GitHub Actions**, você pode automatizar respostas para interações no seu repositório. Aqui está um passo a passo para criar um agente de respostas

# Criar um agente de respostas com GitHub Actions.

# 1 - Criar um arquivo de Workflow.

No seu repositório, vá até a pasta .github/, crie uma pasta workflows e nela crie um arquivo YAML, por exemplo, responder-issues.yml.

# 2 - Definir o gatilho do workflow.

O agente pode ser acionado quando uma *issue* ou *pull requst* for aberta. No arquivo YAML, adicione:
```
name: Responder Issues
on:
  issues:
    types: [opened]

jobs:
  responder:
    runs-on: ubuntu-latest
    steps:
      - name: Responder à Issue
        uses: actions/github-script@v6
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          script: |
            github.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: "Olá! Obrigado por abrir esta issue. Nossa equipe analisará e responderá em breve. 🚀"
        }); 
```

# 3 - Configurar o repositório

Certifique-se de que a pasta .github/workflows/ existe no seu repositório.

O **GitHub Token** já está disponível por padrão para interações básicas.

# 4 - Testar e ativar

Faça o ***Commit*** e o ***push*** do arquivo YAML para o repositório.

Abra uma issue e veja o agente responder automaticamente!