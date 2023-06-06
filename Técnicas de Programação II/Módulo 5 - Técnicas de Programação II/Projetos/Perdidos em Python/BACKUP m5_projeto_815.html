import pandas as pd
import numpy as np
import streamlit as st
import base64
import matplotlib as mp
import plotly.express as px
import plotly.figure_factory as ff
import seaborn as sns

st.sidebar.title('Degree 2022')
st.sidebar.header('Módulo 5 - Técnicas de Programação II | Python')
st.sidebar.subheader('Projeto Final - História das Olimpíadas')

questoes = {'Apresentação': 'O Brasil nas olímpiadas',
            'Questão 1': 'Montagem do Banco',
            'Questão 2': 'Altura x Desempenho',
            'Questão 3': 'Proporção de Medalhas',
            'Questão 4': 'Medalhas x Anos',
            'Questão 5': 'Análise Visual'}

sb = st.sidebar.selectbox('Selecione um Aluno',
                          questoes)

st.title(sb)
st.header(questoes[sb])

if sb == 'Apresentação':
    st.subheader('22 Fevereiro de 2022')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<font size=+4 color=yellow><b>Grupo: Perdidos em Python</b></font>', unsafe_allow_html=True)
    st.markdown(
        '<font face=Verdana><i>Integrantes:</i><br>... José<br>... Rafael<br>... Otto</font>', unsafe_allow_html=True)

if sb == 'Questão 1':
    st.subheader(
        '1. Crie um DataFrame contendo apenas informações sobre atletas brasileiros. Exiba a quantidade de linhas '
        'desse novo DataFrame.')
    st.markdown('<hr>', unsafe_allow_html=True)

    '''
	Para a montagem do banco, fez-se a leitura do arquivo com o uso da biblioteca Pandas e, a priori, apenas se trocou
	todos os 'Nan' por 'Não-Medalhista', indicando que o referido atleta não recebeu medalha. Para tal, fez-se uso do
	método 'fillna', na coluna 'Medal'.
	'''
    '''
	Isso foi feito para facilitar a análise e contagem, sem precisar ficar chamando comandos que incluam os 'NaN' nas
	contagens.
	'''
    df = pd.read_csv('athlete_events.csv')
    br = df[df['Team'] == 'Brazil']
    br['Medal'].fillna('Não-Medalhista', inplace=True)
    br

if sb == 'Questão 2':
    st.subheader(
        '2. Será que existe alguma correlação entre a altura do atleta e seu desempenho, para algum esporte? Faça essa análise separadamente para cada gênero, e conclua.')
    st.markdown('<hr>', unsafe_allow_html=True)

    # apresentação da análise

    '''
	Para a seguinte análise, foi decidido definir desempenho como o simples fato do atleta ter conquistado uma medalha, independente do seu valor, então, além de Não-Medalhista, teremos todos os valores de Bronze, Silver e Bronze sendo convertidos para Medalhista, como podemos ver abaixo.
	'''

    # código
    df = pd.read_csv('athlete_events.csv')
    br = df[df['Team'] == 'Brazil']
    br['Medal'].fillna('Não-Medalhista', inplace=True)
    br_bin = br.copy()
    br_bin.replace({'Bronze': 'Medalhista', 'Silver': 'Medalhista', 'Gold': 'Medalhista'}, inplace=True)
    pd_medal = pd.DataFrame(br_bin['Medal'].value_counts())
    pd_medal

    '''
	Então dividiu-se o DataFrame filtrando para obter apenas as atletas femininas.
	'''

    br_f = br_bin[br_bin['Sex'] == 'F']
    br_f

    '''
	Foram removidas as duplicatas, usando o metodo drop_duplicates, de modo a manter a primeira ocorrência da modalidade (Event) por ano (Year).
	'''

    br_group = br_f.drop_duplicates(
        subset=['Year', 'Event'], keep='first').groupby(
        by=['Sport', 'Medal'], as_index=False).count().sort_values(
        ['Medal', 'Event'], ascending=False).drop(
        columns=['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games', 'Year', 'Season', 'City'])

    br_group

    '''
	Acima pode-se ver os 5 esportes em que se obtiveram mais medalhas.
	'''

    br_f_5 = br_f[(br_f['Sport'] == 'Judo') |
                  (br_f['Sport'] == 'Sailing') |
                  (br_f['Sport'] == 'Football') |
                  (br_f['Sport'] == 'Basketball') |
                  (br_f['Sport'] == 'Volleyball')]

    fig = px.box(x='Sport', y='Height', data_frame=br_f_5, color='Medal', title='Desempenho x Altura (F)',
                 color_discrete_sequence=['Orange', 'Grey'])

    fig.update_yaxes(title='Altura')
    fig.update_xaxes(title='Medalhas')

    fig.update_layout(legend=dict(title='Desempenho'))

    st.plotly_chart(fig, use_container_width=True)

    '''
	Abaixo segue uma análise geral de correlação entre altura e desempenho utilizando-se um mapa de calor. Para tal, pegamos os dummies de altura e medalha, obtendo o mapa abaixo.
	'''

    file_ = open("br_f_mapa_calor.png", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Feminino" width=800 height=400>',
                unsafe_allow_html=True)

    '''
	Agora, o mesmo foi feito para os esportistas masculinos.
	'''

    br_m = br_bin[br_bin['Sex'] == 'M']
    br_m

    '''
	Foram removidas as duplicatas, usando o metodo drop_duplicates, de modo a manter a primeira ocorrência da modalidade (Event) por ano (Year).
	'''

    br_group = br_m.drop_duplicates(
        subset=['Year', 'Event'], keep='first').groupby(
        by=['Sport', 'Medal'], as_index=False).count().sort_values(
        ['Medal', 'Event'], ascending=False).drop(
        columns=['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games', 'Year', 'Season', 'City'])

    br_group

    '''
	Acima pode-se ver os 5 esportes em que se obtiveram mais medalhas.
	'''

    br_m_5 = br_m[(br_m['Sport'] == 'Judo') |
                  (br_m['Sport'] == 'Sailing') |
                  (br_m['Sport'] == 'Athletics') |
                  (br_m['Sport'] == 'Swimming') |
                  (br_m['Sport'] == 'Volleyball')]

    fig = px.box(x='Sport', y='Height', data_frame=br_m_5, color='Medal', title='Desempenho x Altura (F)',
                 color_discrete_sequence=['Orange', 'Grey'])

    fig.update_yaxes(title='Altura')
    fig.update_xaxes(title='Medalhas')

    fig.update_layout(legend=dict(title='Desempenho'))

    st.plotly_chart(fig, use_container_width=True)

    '''
	Abaixo segue uma análise geral de correlação entre altura e desempenho utilizando-se um mapa de calor. Para tal, pegamos os dummies de altura e medalha, obtendo o mapa abaixo.
	'''

    file_ = open("br_m_mapa_calor.png", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Masculino" width=800 height=400>',
                unsafe_allow_html=True)

if sb == 'Questão 3':
    st.subheader('3. Vamos analisar agora as medalhas que nossos atletas trouxeram para casa.')
    st.markdown('<hr>', unsafe_allow_html=True)

    '''
	Para essa questão primeiro se utilizou o banco binário (medalhista e não-medalhista) para determinar quantas medalhas cada esporte trouxe para casa, com o cuidado de remover a duplicatas.
	'''

    df_2 = pd.read_csv('athlete_events.csv')

    br_2 = df_2[df_2['Team'] == 'Brazil']

    br_bin_2 = br_2.copy()

    br_bin_2.replace({'Bronze': 'Medalhista',
                      'Silver': 'Medalhista',
                      'Gold': 'Medalhista'}, inplace=True)

    br_bin_2.sort_values('Year', inplace=True)

    br_bin_2.dropna(subset=['Medal'], inplace=True)

    br_bin_2.drop_duplicates(subset=['Year', 'Event'], keep='first', inplace=True)

    br_bin_2_group = br_bin_2.groupby(
        by=['Sport', 'Medal'], as_index=False).count().sort_values(
        ['Event'], ascending=False)

    br_bin_2_group.drop(
        columns=['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team',
                 'NOC', 'Games', 'Year', 'Season', 'City'], inplace=True)

    br_mean_medal = br_2.sort_values('Year')
    br_mean_medal_1 = br_mean_medal.drop_duplicates(subset=['Year', 'Event'], keep='first')

    br_bin_2_group

    '''
	Então organizou-se este banco de maneira agrupada após filtrar de maneira que contivesse apenas os 6 esportes com mais medalhas, identificados acima.
	'''

    br_6 = br_mean_medal_1[(br_mean_medal_1['Sport'] == 'Judo') |
                           (br_mean_medal_1['Sport'] == 'Sailing') |
                           (br_mean_medal_1['Sport'] == 'Athletics') |
                           (br_mean_medal_1['Sport'] == 'Swimming') |
                           (br_mean_medal_1['Sport'] == 'Volleyball') |
                           (br_mean_medal_1['Sport'] == 'Football')]

    br_6_group = br_6.groupby(by=['Sport', 'Medal'], as_index=False).count()

    br_6_group.drop(columns=['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight',
                             'Team', 'NOC', 'Games', 'Year', 'Season', 'City'], inplace=True)

    br_6_group

    '''
	No gráfico abaixo, um histograma de barras normalizadas em 100%, podemos observar a proporção de medalhas trazidas para casa, bem como a base, isto é, o valor total de medalhas conquistadas no topo.
	'''

    fig = px.histogram(x='Sport', y="Event", data_frame=br_6_group, color='Medal',
                       category_orders={'Medal': ['Bronze', 'Silver', 'Gold']},
                       color_discrete_sequence=['darkorange', 'silver', 'gold'], opacity=0.7,
                       barnorm='percent', text_auto=True, title='Proporção de Medalhas x Esporte')
    fig.update_layout(annotations=[
        {'text': '13                  08                 22                 18                 09                 10',
         'xref': 'x', 'yref': 'y', 'x': 2.5, 'y': 115, 'showarrow': False, 'ax': 0, 'ay': -80,
         'font': dict(family="Nunito", size=16, color="#e67e22")}])

    fig.update_xaxes(title='Esportes')
    fig.update_yaxes(title='Medalhas em %')

    st.plotly_chart(fig, use_container_width=True)

if sb == 'Questão 4':
    st.subheader('4. Para finalizar a história do Brasil, vamos ver a série temporal de medalhas brasileiras.')
    st.markdown('<hr>', unsafe_allow_html=True)

    '''
	No gráfico abaixo podemos observar um histograma de barras com as quantidades de medalhas obtidas a cada 4 anos, proximadamente. Esse gráfico se mostra útil, por em apenas uma visualização ser capaz de informar não apenas a quantidade de melhadas por tipo, como também observar o aumento das vitórias ao longo dos anos.

	OBS.: de acordo com o Data Frame, não há medalhas contabilizadas antes do ano de 1920

	Conclusão: É visível que o Brasil apresenta uma boa crescente, principalmente a partir da metade dos anos 80.
	'''

    df = pd.read_csv('athlete_events.csv')
    br4 = df[df['Team'] == 'Brazil'].copy()
    br4.dropna(subset=['Medal'], inplace=True)
    br_uniq = br4.drop_duplicates(subset=['Year', 'Event'], keep='first').copy()
    br_uniq.sort_values(by='Year').head()

    fig = px.histogram(x='Year', data_frame=br_uniq, color='Medal', nbins=50,
                       category_orders={'Medal': ['Bronze', 'Silver', 'Gold']},
                       color_discrete_sequence=['darkorange', 'silver', 'gold'], opacity=0.7,
                       text_auto=True, title='Série Histórica de Medalhas')

    fig.update_xaxes(title='Anos')
    fig.update_yaxes(title='Medalhas')
    fig.update_layout(legend=dict(title='Medalha'))

    st.plotly_chart(fig, use_container_width=True)

if sb == 'Questão 5':
    st.subheader('5. Agora é com vocês!')
    st.markdown('<hr>', unsafe_allow_html=True)

    '''
	Objetivo Geral da Questão 5: Determinar os destaques do Brasil entre os melhores do mundo.

	Objetivos específicos:

	1. Top5 dos esportes que Brasil tem mais medalhas: determinar em quais esportes o Brasil conquista mais medalhas.
	2. Top5 de Países para cada um destes esportes: determinar quais são os países que conquistaram mais medalhas nestes mesmos esportes identificados no passo 1.
	Objetivo final: verificar se o Brazil está entre os 5 países top, nos mesmos esportes em que tem melhor desempenho. E se sim, em que posição se encontra para cada um.
	'''

    df_5 = pd.read_csv('athlete_events.csv')
    df_5.dropna(subset=['Medal'], inplace=True)

    df_5.sort_values('Year', inplace=True)
    df_5.drop_duplicates(subset=['Year', 'Event'], keep='first', inplace=True)

    df_5_g_medal_esport_pais = df_5.groupby(by=['Team', 'Sport'], as_index=False).count()
    df_5_g_medal_esport_pais.drop(columns=['ID', 'Name', 'Age', 'Height', 'Weight',
                                           'Sex', 'NOC', 'Games', 'Year', 'Season', 'City', 'Event'], inplace=True)
    df_aux = df_5_g_medal_esport_pais.sort_values('Medal', ascending=False)
    df_aux_top_5 = df_aux[((df_aux['Sport'] == 'Football') |
                           (df_aux['Sport'] == 'Volleyball') |
                           (df_aux['Sport'] == 'Basketball') |
                           (df_aux['Sport'] == 'Sailing') |
                           (df_aux['Sport'] == 'Athletics'))]
    df_top_5_volley = df_aux_top_5.sort_values(['Sport', 'Medal'], ascending=False).head()
    df_top_5_volley
    df_top_5_others = df_aux_top_5.sort_values(['Sport', 'Medal'], ascending=False)
    df_top_5_foot = df_top_5_others[df_top_5_others['Sport'] == 'Football'].head()
    df_top_5_foot
    df_top_5_basket = df_top_5_others[df_top_5_others['Sport'] == 'Basketball'].head()
    df_top_5_basket
    df_top_5_sail = df_top_5_others[df_top_5_others['Sport'] == 'Sailing'].head()
    df_top_5_sail
    df_top_5_athl = df_top_5_others[df_top_5_others['Sport'] == 'Athletics'].head()
    df_top_5_athl
    df_5_5 = pd.concat([df_top_5_volley, df_top_5_foot, df_top_5_basket, df_top_5_sail, df_top_5_athl], axis=0)
    df_5_5

    fig = px.histogram(y='Sport', x="Medal", data_frame=df_5_5, color='Team',
                       text_auto=True, title='Top5 do Top5', color_discrete_map={'Brazil': 'yellow'},
                       category_orders={'Sport': ['Athletics', 'Basketball', 'Volleyball', 'Football', 'Sailing']},
                       width=1000, height=500, orientation='h')

    fig.update_yaxes(title='Esportes')
    fig.update_xaxes(title='Medalhas')

    fig.update_layout(legend=dict(title='País'))

    st.plotly_chart(fig, use_container_width=True)

    '''
	Conclusão: O Brasil ainda se coloca entre os Top 5 com 3 esportes, com boas pontuações, ficando em 5o lugar no Veleiro (?), 2o lugar em Volley e 1o Lugar no Futebol, como esperado. Vale pontuar que dois dos esportes que se tem mais medalhas no Brasil, não chegam a figurar entre os 5 melhores países no panorama mundial.
	'''
