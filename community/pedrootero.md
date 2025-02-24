## Informações apenas ilustrativas para a pratica do curso

## Autores

- [@pedrootero](https://www.github.com/pedrootero)

## Tech

- [Node.js] - Linguagem de programação backend para provisionar a infraestrutura como código
- [AWS-ECS] - Amazon Elastic Container Service (Orquestrador de containers)
- [AWS-ELB] - Amazon Load Balancer (balanceamento de carga)
- [AWS-ECR] - Amazon Elastic Container Registry (Repositório de containers)
- [Docker] - Para criar a imagem do container do backend

### Siga os passos abaixo:

Certifique-se de ter instalado o aws-cli

    https://aws.amazon.com/pt/cli/

```bash
  aws --v
```

Verifique se as credenciais AWS estão configuradas.

```bash
  aws configure list
```

Instale as dependencias do projeto

```bash
  npm i
```

faça o deploy do ambiente

```bash
  cdk bootstrap
```

```bash
   cdk deploy --all --require-approval never
```
