# Guia de Emojis para Commits

O uso de emojis em mensagens de commit ajuda a identificar rapidamente o propósito de cada alteração no histórico de um projeto, seguindo padrões como o Gitmoji. Esta prática torna o log mais legível e visualmente organizado.

## Tabela Principal de Emojis

| Emoji | Código               | Função Principal           | Descrição Detalhada                                                 |
| :---: | :------------------- | :------------------------- | :------------------------------------------------------------------ |
|  ✨   | `:sparkles:`         | **Novo Recurso**           | Introdução de uma nova funcionalidade ao código.                    |
|  🐛   | `:bug:`              | **Correção de Bug**        | Correção de um erro, falha ou comportamento inesperado.             |
|  ⚡️  | `:zap:`              | **Melhora de Performance** | Alteração de código que resulta em melhoria de desempenho.          |
|  🔥   | `:fire:`             | **Remoção de Código**      | Remoção de código, arquivos ou funcionalidades obsoletas.           |
|  💄   | `:lipstick:`         | **Ajustes de UI/Estilo**   | Alterações que afetam a interface do usuário (CSS, layout, etc.).   |
|  ♻️   | `:recycle:`          | **Refatoração**            | Alteração no código que não corrige um bug nem adiciona um recurso. |
|  📝   | `:memo:`             | **Documentação**           | Adição ou atualização na documentação (README, guias, etc.).        |
|  ✅   | `:white_check_mark:` | **Testes**                 | Adição, atualização ou correção de testes.                          |
|  🔒   | `:lock:`             | **Segurança**              | Implementação de melhorias ou correções de segurança.               |
|  🚀   | `:rocket:`           | **Deploy**                 | Deploy de código em ambiente de produção ou homologação.            |
|  🚧   | `:construction:`     | **Em Progresso (WIP)**     | Funcionalidade ou alteração ainda em desenvolvimento.               |
|  🔧    | `:wrench:`           | **Configuração**           | Alterações em arquivos de configuração, scripts e ferramentas.      |
|  📦   | `:package:`          | **Dependências**           | Adição, atualização ou remoção de dependências.                     |
|  💥   | `:boom:`             | **Breaking Change**        | Introdução de uma alteração que quebra a compatibilidade.           |
|  ⏪   | `:rewind:`           | **Reversão**               | Reversão de um commit ou de uma série de alterações.                |

## Tabela de Emojis Adicionais

| Emoji | Código                        | Função                     | Descrição                                                          |
| :---: | :---------------------------- | :------------------------- | :----------------------------------------------------------------- |
|  🎉   | `:tada:`                      | **Commit Inicial**         | Início de um novo projeto.                                         |
|  🚑   | `:ambulance:`                 | **Correção Crítica**       | Correção de um bug crítico que precisa de atenção imediata.        |
|  🎨   | `:art:`                       | **Estrutura/Formato**      | Melhorias na estrutura ou formato do código, sem alterar a lógica. |
|  📚   | `:books:`                     | **Documentação Extensa**   | Alterações significativas ou adição de muita documentação.         |
|  🧪   | `:test_tube:`                 | **Testes Experimentais**   | Código de teste experimental ou prova de conceito.                 |
|  🔖   | `:bookmark:`                  | **Release / Versão**       | Criação de uma nova release ou tag de versão.                      |
|  👷   | `:construction_worker:`       | **CI/CD**                  | Alterações em arquivos e scripts de Integração/Entrega Contínua.   |
|  ⬆️   | `:arrow_up:`                  | **Atualizar Dependências** | Atualização de dependências para novas versões.                    |
|  ⬇️   | `:arrow_down:`                | **Downgrade Dependências** | Reversão de dependências para versões mais antigas.                |
|  ➕   | `:heavy_plus_sign:`           | **Adicionar Dependência**  | Adicionar uma nova dependência ao projeto.                         |
|  ➖   | `:heavy_minus_sign:`          | **Remover Dependência**    | Remover uma dependência do projeto.                                |
|  🚚   | `:truck:`                     | **Mover/Renomear**         | Movimentação ou renomeação de arquivos e diretórios.               |
|  ♿️  | `:wheelchair:`                | **Acessibilidade**         | Melhorias relacionadas à acessibilidade (A11Y).                    |
|  💡   | `:bulb:`                      | **Comentários no Código**  | Adição ou melhoria de comentários no código fonte.                 |
|  🔍   | `:mag:`                       | **SEO**                    | Melhorias relacionadas a Otimização para Mecanismos de Busca.      |
|  📱   | `:iphone:`                    | **Responsividade**         | Ajustes e melhorias para a responsividade do layout.               |
|  🌐   | `:globe_with_meridians:`      | **Internacionalização**    | Adição ou atualização de textos para diferentes idiomas (i18n).    |
|  🏗️   | `:building_construction:`     | **Arquitetura**            | Mudanças significativas na arquitetura do projeto.                 |
|  🧹   | `:broom:`                     | **Limpeza de Código**      | Limpeza de código, formatação e remoção de código morto.           |
|  🤡   | `:clown_face:`                | **Mocking**                | Adição ou atualização de dados ou funções de mock.                 |
|  🔀   | `:twisted_rightwards_arrows:` | **Merge**                  | Realização de um merge entre branches.                             |

## Como Usar

A forma mais comum de utilizar esses emojis é no início da mensagem de commit, seguido pelo tipo (opcional) e a descrição.

**Exemplos:**

````bash
git commit -m "✨ feat: Adiciona funcionalidade de login com redes sociais"
```bash
git commit -m "🐛 fix: Corrige falha de cálculo no carrinho de compras"
```bash
git commit -m "📝 docs: Atualiza o README.md com instruções de instalação"
````

A adoção de um padrão como este torna o log de commits muito mais legível e organizado, beneficiando toda a equipe de desenvolvimento.
