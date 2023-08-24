import pandas as pd
import os


back_end = ['Java', 'JavaScript', 'Python', '.NET', 'PHP', 'GO', 'Rust', ' C ', 'C++', 'Git', 'GitHub',
 'GitLab', 'SQL', 'NoSQL', 'Arquitetura', 'Software', 'API', 'Testes', 'Monitoramento', 'Log',
 'CI/CD', 'Mensageria', 'Orientados a Eventos', 'RabbitMQ', 'Kafka']

front_end = ['HTML', 'UX', 'Designer', 'CSS', 'JavaScript', 'Framework', 'React', 'Angular']

mobile = ['iOS', 'Android', 'Kotlin', 'Java', 'Swift', 'Objective-C', 'Multiplataforma', 'Flutter', 'React Native']

game = ['Games', 'Unity 3D', 'Unreal Engine', 'Roblox', 'C++', 'C#', 'Lua', '.NET', 'Metaverse']

crm = ['CRM', 'Dynamics 365', 'Salesforce', 'Activecampaing', 'Google Analytics', 'Power BI',
       'Low-code', 'automação', 'Outsystems', 'Microsoft']

cloud = ['Cloud', 'Computação em Nuvem', 'Provedor', 'GCP', 'Google Cloud Platform', 'Microsoft Azure',
         'Amazon Web Services', 'AWS']

web_IA = ['JavaScript', 'Game', 'Roblox', 'Metaverso', 'Blockchain', 'Mercado Internacional', 'NFT',
          'Ethereum', 'Web 3.0', 'Machine Learning']

data_analytics = ['Excel', 'Estatística', 'Matemática', 'SQL', 'NoSQL', 'Banco de Dados', 'Power BI', 'Python',
                  'Análise de Dados', 'Ciência de Dados', 'Machine Learning', 'Data Science', ' R ', 'Cloud',
                  'Análises Temporais', 'Deploy', 'Spark', 'Big Data']

data_engineering = ['Python', 'Java', 'Scala', 'Git', 'GitHub', 'GitLab', 'Infraestrutura', 'Virtualização', 
                    'Containers', 'Virtualbox', 'Docker', 'SQL', 'NoSQL', 'Banco de Dados', 'Armazenamento',
                    'BigQuery', 'Data Lake', 'Azure', 'Databricks', 'Processamento', 'Pipeline de Dados', 'ETL',
                    'Modelagem Dimensional', 'Cloud', 'Machine Learning', 'Análises Temporais', 'Deploy', 'Big Data',
                    'Spark', 'Hadoop', 'Testes', 'CI/CD', 'Monitoramento', 'Log', 'Mensageria', 'RabbitMQ', 'Kafka',
                    'Orientados a Eventos', 'Orquestração', 'Apache Airflow', 'Google Composer', 'Power BI']

infra_devops_security = ['Infraestrutura', 'CISCO', 'CCNA', 'Administração', 'Linux', 'CLI', 'Gerenciamento',
                         'Servidores', 'FTP', 'JSCAPE', 'SSH', 'OpenSSH', 'HTTP', 'Apache', 'Samba', 'DNS', 'BIND',
                         'SMTP', 'IMAP', 'Postfix', 'Virtualização', 'Containers', 'Virtualbox', 'Docker', 'Orquestração',
                         'Kubernetes', 'Go', 'Python', ' C ', 'C++', 'Git', 'GitHub', 'GitLab', 'CI/CD', 'Cloud',
                         'Monitoramento', 'Observalidade', 'Zabbix', 'Sematext', 'Criptografia', 'Segurança', 'Cybersecurity']

qualidade = ['Lógica de Programação', 'Pensamento Computacional', 'Quality Assurance', 'QA']

lideranca = ['Liderança', 'Equipes Ágeis', 'Desenvolvimento Ágil', 'Cultura Ágil', 'Scrum Master', 'Soft Skills']


# Criando dicionários para cada categoria
categories = {
    'back_end': back_end,
    'front_end': front_end,
    'mobile': mobile,
    'game': game,
    'crm': crm,
    'cloud': cloud,
    'web_IA': web_IA,
    'data_analytics': data_analytics,
    'data_engineering': data_engineering,
    'infra_devops_security': infra_devops_security,
    'qualidade': qualidade,
    'lideranca': lideranca
}

# Convertendo as listas em dicionários com valor 0
dict_representation = {}
for cat, skills in categories.items():
    dict_representation[cat] = {skill: 0 for skill in skills}

# Convertendo em DataFrame
df = pd.DataFrame.from_dict(dict_representation, orient='index')


# Juntar todas as listas em uma única lista
all_keywords = back_end + front_end + mobile + game + crm + cloud + web_IA + data_analytics + data_engineering + infra_devops_security + qualidade + lideranca

# Remover duplicados (se houver)
all_keywords = list(set(all_keywords))

# Lendo e comparando o conteúdo dos arquivos
path_to_files = "../community/"  
for filename in os.listdir(path_to_files):
    with open(os.path.join(path_to_files, filename), 'r') as f:
        file_content = f.read()
        
        # Verificar cada keyword
        for keyword in all_keywords:
            if keyword in file_content:
                # Adiciona 1 para a categoria correspondente (se o valor não é NaN)
                if keyword in back_end and df.loc['back_end', keyword] is not None:
                    df.loc['back_end', keyword] += 1
                if keyword in front_end and df.loc['front_end', keyword] is not None:
                    df.loc['front_end', keyword] += 1
                if keyword in mobile and df.loc['mobile', keyword] is not None:
                    df.loc['mobile', keyword] += 1
                if keyword in game and df.loc['game', keyword] is not None:
                    df.loc['game', keyword] += 1
                if keyword in crm and df.loc['crm', keyword] is not None:
                    df.loc['crm', keyword] += 1
                if keyword in cloud and df.loc['cloud', keyword] is not None:
                    df.loc['cloud', keyword] += 1
                if keyword in web_IA and df.loc['web_IA', keyword] is not None:
                    df.loc['web_IA', keyword] += 1
                if keyword in data_analytics and df.loc['data_analytics', keyword] is not None:
                    df.loc['data_analytics', keyword] += 1
                if keyword in data_engineering and df.loc['data_engineering', keyword] is not None:
                    df.loc['data_engineering', keyword] += 1
                if keyword in infra_devops_security and df.loc['infra_devops_security', keyword] is not None:
                    df.loc['infra_devops_security', keyword] += 1
                if keyword in qualidade and df.loc['qualidade', keyword] is not None:
                    df.loc['qualidade', keyword] += 1
                if keyword in lideranca and df.loc['lideranca', keyword] is not None:
                    df.loc['lideranca', keyword] += 1

# Substituir NaN por 0
df.fillna(0, inplace=True)

# Somar os valores por linha
df['Total'] = df.sum(axis=1)

# Mostrar as três linhas com os maiores valores na coluna 'Total'
top_3 = df.nlargest(3, 'Total')

print('De acordo com o Roadmap da DIO (https://digitalinnovationone.github.io/roadmaps/), temos as seguintes Carreiras:')

print()

carreiras = {
    'Back-End',
    'Front-End',
    'Mobile',
    'Game Development',
    'CRM Systems',
    'Cloud Services',
    'Web 3.0 & AI',
    'Data Analytics',
    'Data Engineering',
    'Infrastructure, DevOps, & Security',
    'Quality Assurance',
    'Leadership'
}

for nome in carreiras:
    print(nome)

print()

print('De acordo com a análise de perfil feita, com base nas palavras-chaves presentes nos arquivos .md individuais; as três carreiras que mais apresentam seus atributos no perfil são:')

print()

for index in top_3.index:
    if index == 'back_end':
        print('Back-End')
    elif index == 'front_end':
        print('Front-End')
    elif index == 'mobile':
        print('Mobile')
    elif index == 'game':
        print('Game Development')
    elif index == 'crm':
        print('CRM Systems')
    elif index == 'cloud':
        print('Cloud Services')
    elif index == 'web_IA':
        print('Web 3.0 & AI')
    elif index == 'data_analytics':
        print('Data Analytics')
    elif index == 'data_engineering':
        print('Data Engineering')
    elif index == 'infra_devops_security':
        print('Infrastructure, DevOps, & Security')
    elif index == 'qualidade':
        print('Quality Assurance')
    elif index == 'lideranca':
        print('Leadership')
    else:
        print(index)  # Este é um fallback caso haja algum índice que não mapeamos.
