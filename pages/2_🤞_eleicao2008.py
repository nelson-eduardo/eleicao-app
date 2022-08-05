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
from st_aggrid import AgGrid

st.set_page_config(page_title="eleicao-geral-App | Nelson Eduardo", page_icon="😋")

# from 1_😖_home import grafico_pie


# para os quatros campos que teremos 
header = st.container()
dataset = st.container()
graficos = st.container()
model_training = st.container()


with header:
    st.title("Analise da eleicao de 2008")
    st.subheader("Este aplicativo foi um estudo pessoal sobre as eleicoes em Angola!!")


with dataset:
    
    # Importacao dos dataset
    fich_excel_eleicao2008 = 'dados/eleicao2008.xlsx'
    planilha_eleicaoGeral = 'eleicaoGeral2008'
   
    
    # st.subheader('Quadro Geral da eleicao presidencial de 1992')
    # st.text("Este quadro representa os numero de votos da eleicao presidencial || fonte CNE")
    
    def importar_datasets(ficheiro, folha):
        try:
            return pd.read_excel(ficheiro, sheet_name=folha)
        except:
            st.warning("Aconteceu um erro ao carregar o ficheiro")
        else:
            return pd.read_excel(ficheiro, sheet_name=folha)       
        
    df_gerala2008 = importar_datasets(fich_excel_eleicao2008, planilha_eleicaoGeral)
# Criacao dos principais graficos
    # graifco de Pie
def grafico_pie(categorias, valores):
    fig = go.Figure(
    go.Pie(
    labels = categorias,
    values = valores,
    hoverinfo = "label+percent",
    textinfo = "value"
    ))

    st.header("Grafico de pie-eleicao Presidencial")
    st.plotly_chart(fig)
    # graifco de barra
def grafico_barra(categoria, valores):
    dict = { 'Candidatos': categoria, 'Votos': valores} 
    df = pd.DataFrame(dict)
    fig = px.bar( 
    df,
    x = "Candidatos",
    y = "Votos",
    # title = "Grafico de barra-eleicao Presidencial",
    # width=800
    )
    st.header("Grafico de Barra-eleicao Presidencial")
    st.plotly_chart(fig)

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
st.dataframe(df_gerala2008)

# AgGrid(df_gerala2008)
#     else: 
        # st.write(recebe) 
     #    st.dataframe(df_presidencial.loc[df_presidencial["Candidatos"]== recebe]) 
        # st.dataframe(df_presidencial)
#     grafico_pie(categoria_presidencial, valores_presidencial) 
#     grafico_barra(categoria_presidencial, valores_presidencial)




