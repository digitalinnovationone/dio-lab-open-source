<h1 align="center">Mário Prazeres</h1>
<h3 align="center">Backend Engineer · Python · Java · AI/LLMOps</h3>

<p align="center">
  <a href="https://www.linkedin.com/in/mario-prazeres/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://pypi.org/project/promptforge-llmops/"><img src="https://img.shields.io/badge/PyPI-promptforge--llmops-blue?style=for-the-badge&logo=pypi&logoColor=white"/></a>
  <a href="https://github.com/marketplace/actions/promptforge-eval"><img src="https://img.shields.io/badge/GitHub%20Marketplace-promptforge--eval-2088FF?style=for-the-badge&logo=github-actions&logoColor=white"/></a>
</p>

---

Engenheiro Backend com Licenciatura em Engenharia Informática (Média 16/20, Projecto Final **19/20**).  
Autor do **PromptForge** — um framework LLMOps open-source publicado no PyPI e no GitHub Marketplace.  
Trago uma mentalidade de produção a cada base de código: fiabilidade, observabilidade e intolerância a falhas silenciosas.

---

## 🛠 Stack

### Linguagens e Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

### Bases de Dados e Infraestrutura
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Neon](https://img.shields.io/badge/Neon-00E599?style=for-the-badge&logo=neon&logoColor=black)

### Qualidade, CI/CD e AI
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Codecov](https://img.shields.io/badge/Codecov-F01F7A?style=for-the-badge&logo=codecov&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI%20API-412991?style=for-the-badge&logo=openai&logoColor=white)

---

## 📌 Projectos em Destaque

### 🔬 [PromptForge — LLMOps Framework](https://github.com/MPrazeres-1983/promptforge)
> `pip install promptforge-llmops` · [PyPI](https://pypi.org/project/promptforge-llmops/) · [GitHub Marketplace](https://github.com/marketplace/actions/promptforge-eval)

Framework minimalista que trata prompts como artefactos versionados, hashados e diffáveis — resolvendo o problema de regressão silenciosa quando prompts mudam em produção.

- Provider Adapter Pattern (OpenAI + Anthropic + qualquer provider compatível)
- LLM-as-judge com rúbricas explícitas, normalização de scores e rationale por dimensão
- CLI com 8 subcomandos: `eval`, `diff`, `history`, `new`, `report`, `dashboard`, `runs`, `validate`
- GitHub Action oficial — regression testing em qualquer pipeline em 3 linhas de YAML

[![CI](https://github.com/MPrazeres-1983/promptforge/actions/workflows/ci.yml/badge.svg)](https://github.com/MPrazeres-1983/promptforge/actions)
![PyPI](https://img.shields.io/pypi/v/promptforge-llmops)

---

### 🏗️ [Issue Tracker API](https://github.com/MPrazeres-1983/issue-tracker-api)
> Python · Flask 3.0 · PostgreSQL · JWT · Docker · PromptForge · [Live Demo](https://issue-tracker-api-860i.onrender.com/api/v1/health)

API production-ready com arquitectura Controller-Service-Repository. **Integra o PromptForge** para classificação automática de issues por IA com regression testing do prompt em CI.

- Autenticação JWT dual-token, bcrypt, RBAC (Admin/Developer/Viewer)
- ~200 testes automatizados com pytest + factory-boy, 75%+ cobertura (Codecov)
- Endpoint `POST /issues/suggest` — classifica prioridade e status via LLM
- CI/CD com job `prompt-eval`: dataset de 12 issues reais valida o classifier em cada push

[![CI/CD](https://github.com/MPrazeres-1983/issue-tracker-api/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/MPrazeres-1983/issue-tracker-api/actions)
[![codecov](https://codecov.io/gh/MPrazeres-1983/issue-tracker-api/graph/badge.svg)](https://codecov.io/gh/MPrazeres-1983/issue-tracker-api)

---

### ☕ [Task Manager API](https://github.com/MPrazeres-1983/task-manager-api)
> Java 21 · Spring Boot 3.2 · Flyway · Docker · Swagger UI

API enterprise-grade com JWT via Spring Security, isolamento de dados por utilizador, paginação server-side e migrações de schema auditáveis com Flyway.

- Tratamento de erros via ProblemDetail (RFC 7807)
- Suite de testes com JUnit 5, Mockito, MockMvc e H2 in-memory
- Relatórios JaCoCo em cada `mvn clean verify`

---

### 🍽️ [Meal Planner — Projecto Final de Licenciatura](https://github.com/MPrazeres-1983/Meal-Planner)
> Python · Flask · PostgreSQL · pytest · GitHub Actions · **Nota: 19/20** · [Live Demo](https://meal-planner-8zsa.onrender.com)

Aplicação full-stack de planeamento semanal de refeições com RBAC, 31 testes automatizados e deploy em produção no Render.

---

## 🎓 Formação e Certificações

- 🎓 **Licenciatura em Engenharia Informática** — Universidade Aberta (Média 16/20 · Projecto Final 19/20)
- 📄 **Google Data Analytics Professional Certificate** — Google / Coursera
- 🐍 **Programação Avançada em Python** — Passaporte Qualifica
- 💾 **SQL Avançado** — Passaporte Qualifica

---

## 📫 Contacto

[![LinkedIn](https://img.shields.io/badge/LinkedIn-mario--prazeres-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/mario-prazeres/)
[![Email](https://img.shields.io/badge/Email-marioprazeres@msn.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:marioprazeres@msn.com)
[![X](https://img.shields.io/badge/X-@Tuti__1983-000000?style=flat&logo=x)](https://x.com/Tuti_1983)

---

*Aberto a colaborações e oportunidades em Backend Engineering, LLMOps e AI infrastructure.*
