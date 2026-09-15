👋 Olá, eu sou Marcos Roberto
🚀 Sobre mim
🎓 Estudante de Ciência de Dados 
💻 Foco em Python, SQL, Machine Learning e Visualização de Dados 
📊 Buscando unir rigor técnico e impacto real nos projetos 
🌱 Sempre explorando novas tecnologias e frameworks 

📈 Minhas métricas no GitHub
 

⚡ PageSpeed Insights
🛠️ Configuração do Workflow
name: Metrics
on:
  schedule: [{cron: "0 * * * *"}]
  workflow_dispatch:

jobs:
  github-metrics:
    runs-on: ubuntu-latest
    steps:
      - uses: lowlighter/metrics@latest
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          plugin_pagespeed: yes
          plugin_pagespeed_url: https://seusite.com
          plugin_pagespeed_detailed: yes
          plugin_pagespeed_screenshot: yes
          plugin_pagespeed_pwa: yes
✅ O que esse setup entrega
🏎️ Pontuação de performance do site 
📸 Captura de tela automática 
📱 Status de PWA 
📊 Métricas detalhadas (FCP, LCP, TTI, CLS, etc.) 

🛠️ Projetos em destaque
listaPython → exercícios e utilitários em Python 
gerador_cpf → ferramenta simples para gerar CPFs válidos 
graphstreamlitllm → visualização de grafos com Streamlit e LLM 
neo4j-docker-cyphe → experimentos com grafos e Neo4j em Docker 
aplicativo_react → primeiros passos com React e front-end 

🌐 Onde me encontrar
📧 Email: marcosdo337@gmail.com 
