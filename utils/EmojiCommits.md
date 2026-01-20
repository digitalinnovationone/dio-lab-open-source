## 🚀 Convenção de Commits com Emojis

Utilizamos emojis para identificar rapidamente o tipo de mudança feita no projeto. Isso facilita a leitura e organização do histórico de commits. Veja abaixo os principais:

| Emoji | Tipo (PT-BR)         | Tipo (EN)             | Descrição (PT-BR)                                          |
|-------|----------------------|-----------------------|------------------------------------------------------------|
| 🎉    | Commit Inicial       | Initial commit        | Primeiro commit de criação do projeto                      |
| 📝    | Texto                | Text                  | Atualização de textos, conteúdo ou arquivos markdown       |
| ✨    | Novo Recurso         | New feature           | Implementação de uma nova funcionalidade                   |
| 🐛    | Bugfix               | Bug fix               | Correção de um erro no código                              |
| 🚑    | Correção Crítica     | Hotfix                | Correção crítica ou urgente                                |
| 🔒    | Segurança            | Security              | Ajustes voltados para segurança                            |
| 📇    | Metadata             | Metadata              | Alteração de metadados como título, versão, autor etc.    |
| ♻️    | Refatoração          | Refactor              | Refatoração de código sem alteração de comportamento       |
| 📚    | Documentação         | Docs                  | Mudanças ou acréscimos na documentação                     |
| ♿    | Acessibilidade       | Accessibility         | Melhorias de acessibilidade no sistema                     |
| 🐎    | Performance          | Performance           | Melhorias na performance da aplicação                      |
| 🎨    | CSS                  | CSS                   | Alterações em estilos CSS                                  |
| 💄    | CSS (UI)             | UI style              | Ajustes visuais ou na interface do usuário (UI)            |
| 🔧    | Configuração         | Configuration         | Alterações em arquivos de configuração                     |
| 🚨    | Teste                | Test                  | Inclusão ou modificação de testes                          |
| 💩    | Depreciado           | Deprecated            | Código ruim ou que será substituído                        |
| 🗑️    | Removendo Código     | Remove code           | Exclusão de trechos de código                              |
| 🗑️    | Removendo Arquivo    | Remove file           | Exclusão de arquivos                                       |
| 🚧    | WIP                  | Work in progress      | Alterações em andamento ainda não finalizadas              |
| 📁    | Pasta                | Folder                | Criação ou reorganização de pastas                         |
| 📄    | Arquivo              | File                  | Criação ou alteração de arquivos                           |

---

## Por que usar Emoji Commits?

O uso de emojis nos commits vai muito além de apenas decorar o histórico do Git. Eles ajudam a comunicar de forma rápida e visual o propósito de cada alteração, facilitando a leitura e entendimento do histórico do projeto. Isso é especialmente útil em projetos colaborativos, onde múltiplas equipes e desenvolvedores contribuem simultaneamente.

### Benefícios do uso de Emoji Commits:

- **Clareza e Organização:** Os emojis funcionam como etiquetas visuais que indicam rapidamente o tipo de mudança realizada, como correção de bugs, adição de novas funcionalidades ou melhorias na documentação.
- **Padronização:** Ter um padrão definido para os commits ajuda a manter um histórico consistente e profissional, reduzindo ambiguidades e facilitando a revisão do código.
- **Comunicação Efetiva:** Permite que todos os membros da equipe, incluindo gerentes e colaboradores não técnicos, compreendam facilmente o progresso do projeto.
- **Automação e Integração:** Muitas ferramentas de CI/CD, análise de código e geração de changelogs utilizam emojis para categorizar automaticamente os commits, acelerando processos.

---

## Exemplos de commits com emojis (usando Tipo PT-BR)

```bash
git commit -m "🎉 Commit Inicial: criação do projeto base"
git commit -m "📝 Texto: atualização do README com instruções"
git commit -m "✨ Novo Recurso: adiciona sistema de login"
git commit -m "🐛 Bugfix: corrige validação do formulário"
git commit -m "🚑 Correção Crítica: corrige falha no módulo de pagamento"
git commit -m "🔒 Segurança: atualiza dependências para corrigir vulnerabilidades"
git commit -m "📇 Metadata: altera versão do projeto para 1.1.0"
git commit -m "♻️ Refatoração: reorganiza funções de cálculo"
git commit -m "📚 Documentação: adiciona guia de contribuição"
git commit -m "♿ Acessibilidade: melhora contraste das cores"
git commit -m "🐎 Performance: otimiza consultas ao banco de dados"
git commit -m "🎨 CSS: ajusta estilo do cabeçalho"
git commit -m "💄 CSS (UI): melhora layout da página inicial"
git commit -m "🔧 Configuração: atualiza arquivo .env"
git commit -m "🚨 Teste: adiciona testes unitários para o serviço X"
git commit -m "💩 Depreciado: remove função obsoleta"
git commit -m "🗑️ Removendo Código: exclui código legado"
git commit -m "🗑️ Removendo Arquivo: remove arquivo temporário"
git commit -m "🚧 WIP: implementa esqueleto da nova feature"
git commit -m "📁 Pasta: reorganiza estrutura de diretórios"
git commit -m "📄 Arquivo: adiciona arquivo de configuração do Docker"
