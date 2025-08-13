# 🔒 Melhoria de Segurança: Remoção de Token Hardcoded:

```markdown
<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> Melhorias de Segurança no Código</span>
</h1>

## 🚨 Problema Crítico de Segurança

[![Security](https://img.shields.io/badge/Security-Critical-FF0000?style=for-the-badge)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
[![Best Practices](https://img.shields.io/badge/Best_Practices-Important-FFA500?style=for-the-badge)](https://docs.github.com/en/code-security/security-advisories/guidance-on-how-to-secure-your-code)

### Token de Acesso Exposto no Código

> ⚠️ **Atenção**: O código atual contém um token de acesso pessoal (PAT) hardcoded, o que representa um grave risco de segurança, mesmo que o token tenha sido revogado.

```python
# ❌ Implementação Atual (Insegura)
TOKEN = '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'  # Token exposto no código-fonte
```

## 🛡️ Solução Proposta:

[![Environment Variables](https://img.shields.io/badge/Environment_Variables-Recommended-008000?style=for-the-badge)](https://12factor.net/config)

### Migração para Variáveis de Ambiente

```python
# ✅ Nova Implementação (Segura)
import os
TOKEN = os.getenv('GITHUB_TOKEN')  # Token lido de variável de ambiente
```

## 📝 Passos para Implementação:

<table>
  <thead>
    <tr align="left">
      <th>Nº</th>
      <th>Ação</th>
      <th>Comando/Detalhes</th>
    </tr>
  </thead>
  <tbody align="left">
    <tr>
      <td>01</td>
      <td>Criar novo token GitHub</td>
      <td>Settings > Developer Settings > Personal Access Tokens</td>
    </tr>
    <tr>
      <td>02</td>
      <td>Configurar variável de ambiente</td>
      <td><code>export GITHUB_TOKEN='seu_novo_token'</code></td>
    </tr>
    <tr>
      <td>03</td>
      <td>Atualizar arquivo .gitignore</td>
      <td>Adicionar <code>.env</code> para evitar vazamentos</td>
    </tr>
    <tr>
      <td>04</td>
      <td>Documentar uso no README</td>
      <td>Explicar configuração necessária para novos contribuidores</td>
    </tr>
  </tbody>
</table>

## 🔗 Recursos Adicionais:

[![GitHub Docs](https://img.shields.io/badge/GitHub-Docs-181717?style=for-the-badge&logo=github)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
[![OWASP](https://img.shields.io/badge/OWASP-Best_Practices-000000?style=for-the-badge)](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

> 💡 **Dica**: Considere também implementar um sistema de rotação automática de tokens para maior segurança:

## 🤝 Como Contribuir para Esta Melhoria:

1. Faça um fork do repositório
2. Crie uma branch: `git checkout -b fix/security-token`
3. Implemente as mudanças
4. Envie o Pull Request com uma descrição clara das alterações

[![PR Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](https://github.com/digitalinnovationone/dio-lab-open-source/pulls)

<div align="center">Contribuição de segurança por <strong>Filipe Maciel</strong></div> 
