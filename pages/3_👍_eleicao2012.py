from email import header
# from turtle import color
from click import style
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# graficos
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="eleicao-geral-App | Nelson Eduardo", page_icon="😋")

# para os quatros campos que teremos 
header = st.container()
dataset = st.container()
graficos = st.container()
model_training = st.container()
element_name = st.container()

with header:
    st.title("Analise da eleicao de 2012")
    st.subheader("Este aplicativo foi um estudo pessoal sobre as eleicoes em Angola!!")



with dataset:
    
    # Importacao dos dataset
    fich_excel_eleicao2012 = 'dados/eleicao2012.xlsx'
    planilha_eleicaoGeral = 'eleicaoGeral2012'
   
    
    # st.subheader('Quadro Geral da eleicao presidencial de 1992')
    # st.text("Este quadro representa os numero de votos da eleicao presidencial || fonte CNE")
    
    def importar_datasets(ficheiro, folha):
        try:
            return pd.read_excel(ficheiro, sheet_name=folha)
        except:
            st.warning("Aconteceu um erro ao carregar o ficheiro")
        else:
            return pd.read_excel(ficheiro, sheet_name=folha)       
        
    df_gerala2012 = importar_datasets(fich_excel_eleicao2012, planilha_eleicaoGeral)



 # Seccao da eleicao presidencial
with graficos:
    st.subheader('Quadro Geral da eleicao presidencial de 1992')
   
    expander = st.expander("MAIS INFORMCAO")
    expander.write("""
    uma analise sobre os dados das  eleicao presidencial em Angola realizada em 1992, 
    onde podemos ver a tabela dos candidados a presidencia e 
    a quatidade de votos conseguido, para uma melhor visaulizacao usamos os graficos de bar e Pie.
     Dados obtidos no site da CNE
    """
     
    )
#     recebe = multipla_opc(df_presidencial)
#     if recebe == []:
        # st.write("Seleciona um candidados")
st.dataframe(df_gerala2012)


# st.sidebar.[element_name]


# # "with" notation
# with st.sidebar:
#     st.[element_name]

# with st.sidebar:
#     with st.echo():
#         st.write("This code will be printed to the sidebar.")

#     with st.spinner("Loading..."):
#         time.sleep(5)
#     st.success("Done!")