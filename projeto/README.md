# Projeto Spring Boot Simples

Este projeto demonstra como criar uma API e páginas HTML básicas usando Spring Boot.

## Pré-requisitos

- Java 17 instalado e configurado no PATH (`java -version` deve funcionar)
- Maven instalado para compilar e executar (`mvn -version`)

## Como executar

```bash
mvn spring-boot:run
```

Após iniciar a aplicação, acesse:

- `http://localhost:8080/projeto` – página inicial
- `http://localhost:8080/projeto/home` – segunda página
- `http://localhost:8080/projeto/getAll` – lista de usuários em JSON

## Estrutura principal

- `ProjetoApplication` inicia a aplicação Spring Boot.
- `ProjetoController` contém os endpoints HTTP.
- `Usuario` representa um usuário simples (sem banco de dados).
- Templates HTML ficam em `src/main/resources/templates`.
