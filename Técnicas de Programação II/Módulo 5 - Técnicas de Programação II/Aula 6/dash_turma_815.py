# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('./data/alunos_815.csv', sep=';')

st.sidebar.title('Turma 815')
st.sidebar.header("Módulo 5 - Técnicas de programação II")

sb = st.sidebar.selectbox('Selecione um aluno:', df['Nome'])

if sb != '...':
    code_color = df[df['Nome']==sb]['Cor favorita (código)'].values[0]
    cor = df[df['Nome']==sb]['Cor favorita'].values[0]
    
    st.title(sb)
    st.subheader('Informações:')
    st.markdown(f"""<font color="black">Cor favorita: </font><font color="{code_color}">{cor}</font>""",
               unsafe_allow_html=True)
    st.write('Filme Favorito: ', df[df['Nome']==sb]['Filme Favorito'].values[0])
    st.write('Grupo módulo 4: ', df[df['Nome']==sb]['Grupo módulo 4'].values[0])



