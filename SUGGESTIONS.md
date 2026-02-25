# Sugestões de Melhoria Técnica - Community Feedback

Durante a execução deste lab, foram identificados pontos de otimização para melhorar a escalabilidade do projeto:

### 1. Estrutura de Diretórios
Para evitar o carregamento lento da pasta `community/`, sugere-se a segmentação por letra inicial:
- `community/a/`
- `community/b/`

### 2. Performance de Clone
Adicionar instrução de `git clone --depth 1` para novos contribuidores, reduzindo o tráfego de dados desnecessário.

### 3. Automação de Qualidade (CI)
Implementação de um linter para validar:
- Se o nome do arquivo .md corresponde ao nome do usuário.
- Se os links de redes sociais estão com formato correto.
