# Olá, eu sou Alan Lins Alves 😃👍👍

## 🎓 Sobre Mim


Sou Engenheiro Civil de formação, mas minha verdadeira paixão e foco de atuação têm se **voltado cada vez mais para a área de Dados**. Atualmente trabalho numa empresa de consultoria em Engenharia Civil mas **no momento encontro-me em um momento de transição de carreira**, onde o meu trabalho diário é predominantemente voltado para a **Engenharia de Dados** e produção de **Relatórios Power BI**.

Desde sempre, fui **fascinado por tecnologia** e, ao longo do tempo, desenvolvi um profundo interesse em compreender como os dados podem ser organizados, processados e analisados para auxiliar não nas **decisões estratégicas nos negócios**, mas também tentar **gerar impactos positivos** e tangíveis na vida das pessoas.

## 🛠️ Habilidades
### Linguagens de Programação

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)
![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white)

> Python com certeza é a linguagem de programação mais utilizada.
>As demais uso raramente.

### Bibliotecas do Python

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

### Bancos de Dados

![MicrosoftSQLServer](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

### Ferramentas Microsoft

![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white) ![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Microsoft Excel](https://img.shields.io/badge/Dataverse-%2357A143?style=for-the-badge&logo=microsoft-excel&logoColor=white)

### Cloud

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)


> Apenas utilizei uma vez em uma aplicação prática. Nas seções a seguir explico como foi a experiência.

### Controle de Versão

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

> Sou bem iniciante em controle de versão, mas estou aprendendo!

## 📚 Projetos na Área de Dados
A seguir resumo os **principais projetos relacionados a Dados que desenvolvi** recentemente. Todos estão no escopo da empresa que trabalho apenas um está relacionado ao meu Trabalho de Conclusão de Curso de Engenharia Civil.

### • Banco de Dados dos Colaboradores da Empresa 📋📈🧍‍♀️🧍‍♂️

Desde 2020, a empresa em que trabalho passou por um crescimento acelerado, **dobrando seu número de colaboradores em menos de quatro anos**. Esse aumento rápido evidenciou a necessidade de uma gestão eficiente dos dados dos funcionários, que até então eram controlados por **planilhas desconectadas**. Surgiu, então, a demanda por uma estrutura centralizada e integrada, capaz de abranger todos os tipos de contratação (CLT, PJ, estágio e jovem aprendiz), considerando suas particularidades e fluxos específicos. Fui selecionado para um grupo multidisciplinar, sendo responsável por **otimizar a organização dos dados**.

<img src="https://blog.leucotron.com.br/wp-content/uploads/2017/03/estender-1000-veja-como-a-comunicacao-interna-nas-empresas-e-importante.jpg" alt="drawing" width="200" class="center"/>
<br>
<br>

Nesse projeto, automatizei diversos processos manuais utilizando ferramentas como **Power Automate**, **Python** e **Power Query**, o que proporcionou maior precisão e agilidade na gestão de informações. Modelei o **Banco de Dados no Dataverse**, armazenando informações cruciais dos colaboradores, como histórico salarial, desempenho e outras métricas relevantes. Realizei vários **tratamentos nos dados diretamente no Dataverse**, por meio do **Fluxo de Dados**, uma solução **equivalente ao Power Query** só que na nuvem. Além disso, desenvolvi um dashboard no Power BI voltado para **análises estratégicas da diretoria**. Essa experiência permitiu que eu aplicasse minhas habilidades técnicas com impacto direto nos processos da empresa, aumentando a **eficiência e aprimorando a qualidade da tomada de decisões corporativas**.

### • Otimização e Lançamento do Dashboard Financeiro da Empresa

Uma das principais dificuldades enfrentadas pela alta liderança da empresa era a **necessidade de obter dados financeiros** prontos para análise de maneira rápida e eficiente. Inicialmente, eles recebiam apenas uma **planilha financeira alimentada manualmente** uma vez por mês, contendo informações sobre o desempenho dos produtos de cada diretor de desenvolvimento, como receita, custos diretos e indiretos, despesas corporativas e notas fiscais em aberto. Embora **já existisse um projeto de Dashboard no Power BI**, ele estava longe de ser utilizável devido à **extrema lentidão**. Todo o processo de **ETL estava sendo realizado totalmente no Power Query**, com tratamento pesado de dados, incluindo rateios, o que acabou tornando **inviável** a continuidade do desenvolvimento no Power BI. Minha missão era resolver esse problema de desempenho e viabilizar a análise rápida e eficiente dos dados.

<img src="https://images.datacamp.com/image/upload/f_auto,q_auto:best/v1551381985/2_balilz.png" alt="drawing" width="200" class="center"/>
<br>
<br>

Para isso, entrei em contato com o fornecedor responsável pelo sistema de gestão da empresa, onde os dados financeiros eram armazenados, e obtive **acesso ao Data Warehouse** (SQL Server), de onde o Power BI realizava as leituras dos dados. O primeiro passo foi entender todos os **cálculos e tratamentos aplicados no dashboard antigo**, que nunca havia sido lançado, para então **criar diversas VIEWS no SQL Server**, ou seja, com todos dos **tratamentos** necessários e mais pesados sendo realizados **diretamente no Data Warehouse**. No total, desenvolvi cerca de 20 Wiews SQL e realizei múltiplos testes de desempenho para garantir eficiência. Com os dados praticamente prontos no Data Warehouse sendo lidos pelo Power BI, o **tratamento no Power Query foi reduzido ao mínimo necessário**, o que resultou em uma grande melhoria de desempenho. Além disso, aproveitei a oportunidade para **adicionar novas visualizações ao dashboard** com base em feedbacks da diretoria. Esse projeto me proporcionou um grande **aprendizado sobre SQL** e trouxe à empresa uma solução muito mais eficiente para a análise de seus dados financeiros.

### • Armazenamento de dados de geolocalização no SQL Azure

Esse foi meu primeiro contato com a nuvem da **Azure**. Em um dos projetos de Engenharia Civil em andamento, na época um dos maiores da empresa, o gerente precisava analisar e gerenciar os **dados de geolocalização** de várias máquinas e caminhões que transportavam entulhos. O **volume de dados** era considerável, com **atualizações de posição a cada 5 segundos**, o que resultava em média 150.000 linhas diariamente. O gerente enfrentava dificuldades até mesmo para abrir uma semana de dados no Excel devido ao tamanho dos arquivos. Após uma conversa para entender o problema, ele me forneceu a **API** do fornecedor com credenciais e a partir disso era possível obter os dados de localização de cada veículo, identificados de forma única.

<img src="https://www.lambda3.com.br/wp-content/uploads/2017/02/sql-azure.png" alt="drawing" width="200" class="center"/>
<br>
<br>

Inicialmente, desenvolvi um **script em Python** que extraía esses dados diariamente via API e os armazenava em arquivos CSV. No entanto, devido ao grande volume de dados, tornou-se evidente a necessidade de um **banco de dados**. Foi nesse ponto que tive a ideia de usar o Azure, criando uma instância de **SQL Server na nuvem**, também criei as tabelas necessárias. Ajustei o script Python para **alimentar o banco de dados incrementalmente**, organizando os dados em tabelas como "Empresa", "Veículos" e "Localização". Por fim, criei um **dashboard no Power BI** que se conectava diretamente ao banco via **DirectQuery**, evitando que o Power BI armazenasse localmente esse imenso volume de dados, garantindo a velocidade do relatório.

### • Mapas de Susceptibilidade a Deslizamento de Terra com a Utilização de Redes Neurais

Esse projeto reflete minha **vontade por trabalhar com dados** e minha busca por **soluções práticas para problemas reais**. No final da minha graduação em Engenharia Civil, escolhi desenvolver um TCC com forte aplicação na área de dados. Em **Recife**, nos períodos de **chuvas intensas**, os **deslizamentos de terra** são uma causa recorrente de mortes, especialmente em comunidades que, por falta de espaço, se estabelecem em **áreas de alto risco**. Os **métodos convencionais** de criação de **mapas de suscetibilidade a deslizamentos de terra são lentos**, muitas vezes demorando semanas para ficarem prontos, e dependem fortemente da experiência do profissional que faz a avaliação in loco.

<img src="https://directorsblog.nih.gov/wp-content/uploads/2024/05/Neural-Connections1.1-1536x864.jpg" alt="drawing" width="200" class="center"/>
<br>
<br>

Com esse problema em mente, e com o apoio do meu orientador, reunimos dados **históricos de deslizamentos de terra** de uma comunidade específica de Recife, além de variáveis relacionadas à **geometria do terreno** proveniente do modelo digital de terreno. Criamos um banco de dados contendo pontos classificados como estáveis e instáveis. A partir dessa base, utilizei uma rede neural de calssificação, com ajuda da **biblioteca sklearn**, para treinar um **modelo capaz de prever a suscetibilidade a deslizamentos em cada ponto do terreno**. O resultado foi um mapa gerado de forma muito mais ágil, com potencial para **salvar vidas** ao acelerar o processo de identificação de áreas de risco, mitigando as consequências da demora associada aos métodos tradicionais.

## 💡 O que Estou Aprendendo

- Me aprofundando um pouco mais em modelagem de dados. Estou terminando de estudar o livro Modelagem de Dados de José Osvaldo de Sordi. Um livro muito bom pois tem vários estudos de casos.

<img src="https://www.editoradodireito.com.br/media/catalog/product/9/7/9788536532356.24_1.png" alt="drawing" width="200" class="center"/>
<br>
<br>

- Estou aprendendo mais sobre Machine Learning. Comecei a estudar com o intuito de aprender detalhes que antes eu não estava atento, isso ajudou bastante no meu TCC. O livro Mãos a Obra: Aprendizado de Máquina com sklean, keras e tensorflow de Aurélien Géron tem me ajudado bastante.

<img src="https://m.media-amazon.com/images/I/81R5BmGtv-L._SY522_.jpg" alt="drawing" width="200" class="center"/>
<br>
<br>

- Planejo iniciar em breve o Plano Oficial **Caminho de carreira do engenheiro de dados do Microsoft Learn**. Trata-se de um treinamento para obter a Certificação Azure Data Engineer Associate.

<img src="https://thinkadnet.com/wp-content/uploads/2020/07/Azure-White.png" alt="drawing" width="200" class="center"/>
<br>
<br>

- Logo em breve estarei iniciando meus estudos no livro Fundamentos de Engenharia de Dados de Joe Reis e Matt Housley.

<img src="https://m.media-amazon.com/images/I/610utNg-05L._SY522_.jpg" alt="drawing" width="200" class="center"/>
<br>

## 🎯 Objetivos
Estou motivado e determinado a aprofundar continuamente meus conhecimentos em engenharia de dados, buscando não apenas aprimorar minhas habilidades técnicas, mas também me posicionar de maneira estratégica para conquistar uma oportunidade de emprego significativa na área.

## 📫 Como Entrar em Contato Comigo

|  |  |
| :--- | :--- |
| **LinkedIn** | [Alan Alves](https://www.linkedin.com/in/alan-alves-3ba83b186/) |
| **Email** | alanlinsalves@gmail.com |
| **GitHub** | [github.com/AlanLinsAlves](https://github.com/AlanLinsAlves) |
| **Perfil do DIO** | [Alan Alves DIO](https://www.dio.me/users/alanlinsalves)|
