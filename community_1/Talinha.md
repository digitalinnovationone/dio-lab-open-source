
## Adicionando extensões de renderização

As extensões de renderização são como upgrades para o Markdown básico, ou seja, enquanto o Markdown básico te dá as ferramentas para criar um texto formatado simples, as extensões de renderização expandem essas ferramentas, permitindo que você adicione elementos mais avançados, como gráficos, diagramas, tabelas mais complexas e até mesmo interatividade, dependendo das extensões que você usa.
 
### Exemplos:

#### Mermaid (criação de diagramas e gráficos )
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

```mermaid
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    Campaign A: [0.3, 0.6]
    Campaign B: [0.45, 0.23]
    Campaign C: [0.57, 0.69]
    Campaign D: [0.78, 0.34]
    Campaign E: [0.40, 0.34]
    Campaign F: [0.35, 0.78]
```

#### Table of Contents (tabela de conteúdos com links)

<!-- TOC -->
- [Seção 1](#seção-1)
- [Seção 2](#seção-2)
  - [Subseção 2.1](#subseção-21)
  - [Subseção 2.2](#subseção-22)
<!-- /TOC -->

