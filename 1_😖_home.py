from email import header
# from turtle import width
# from turtle import color
from click import style
# from sklearn import exceptions
import streamlit as st

import pandas as pd
# import plotly.graph_objects as go
 


# import plotly.figure_factory as ff

# import plotly.express as px
# from plotly.subplots import make_subplots
# graficos
# import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title="eleicao-geral-App | Nelson Eduardo", page_icon="😋")   


# Zona de definicao dos container para pagina 
header = st.container()
dataset = st.container()
graficos_presidencial = st.container()
graficos_legilativa = st.container()
model_training = st.container()

st.markdown(
"""
<style>
    .main{
       background-color:"#ffff"
    }
</style>

""",
unsafe_allow_html = True

)


div1, div2 = st.columns([22, 3])
with header:
    st.title("BEM VIMDO")
    st.subheader("Este aplicativo foi um estudo pessoal sobre as eleicoes em Angola!!")
# Incio do bloco dataset-importacao dos dataset



with dataset:
    
    # Importacao dos dataset
    fich_excel_eleicao1992 = "dados/eleicao1992.xlsx"
    planilha_presidencial = "presidencial"
    planilha_legilativa = "legilativa"
    
    # st.subheader('Quadro Geral da eleicao presidencial de 1992')
    # st.text("Este quadro representa os numero de votos da eleicao presidencial || fonte CNE")
    
    def importar_datasets(ficheiro, folha):
        try:
            return pd.read_excel(ficheiro, sheet_name=folha)
            
        except:
            st.warning("Aconteceu um erro ao carregar o ficheiro")
        else:
            return pd.read_excel(ficheiro, sheet_name=folha)       
        
    df_presidencial = importar_datasets(fich_excel_eleicao1992, planilha_presidencial)
    df_legilativa = importar_datasets(fich_excel_eleicao1992, planilha_legilativa)
    # df_presidencial = pd.read_excel(fich_excel_eleicao1992, sheet_name=planilha_presidencial)
    # st.dataframe(df_presidencial)    

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

    # st.header("Grafico de pie-eleicao Presidencial")
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
    # st.header("Grafico de Barra-eleicao Presidencial")
    st.plotly_chart(fig)
# fim da zana para criacao de graficos

# variavel eleicao presidencial


def input():
    variavel_nome = st.text_input("Digita qualquer coisa", 'Digite o nome do Cliente')
    return variavel_nome


# valores para os graficos da eleicao presidencial
categoria_presidencial = df_presidencial["Candidatos"]
valores_presidencial =  df_presidencial["votos"]

# variavel eleicao legilativa
# st.dataframe(df_legilativa)
categoria_legilativa = df_legilativa["Partidos"]
valores_legilativa = df_legilativa["Votos"]

# Seccao da eleicao presidencial
with graficos_presidencial:
    st.subheader('Quadro Geral da eleicao presidencial de 1992')
   
    expander = st.expander("MAIS INFORMCAO")
    expander.write("""
    uma analise sobre os dados das  eleicao presidencial em Angola realizada em 1992, 
    onde podemos ver a tabela dos candidados a presidencia e 
    a quatidade de votos conseguido, para uma melhor visaulizacao usamos os graficos de bar e Pie.
     Dados obtidos no site da CNE
    """
     
    )
    
    
    checkboReturn = st.sidebar.checkbox("Filtrar Candidatos")
    st.write("")
    # st.balloons()

    if checkboReturn == True:
        recebe =  st.sidebar.selectbox('Candidatos', df_presidencial ) 
        if recebe == "":
            # st.write("Seleciona um candidados")
            st.dataframe(df_presidencial.loc[df_presidencial['Partidos']== recebe])
        else: 
            # st.write(recebe) 
            st.dataframe(df_presidencial.loc[df_presidencial["Candidatos"]== recebe]) 
            # st.dataframe(df_presidencial)
    else:
        st.dataframe(df_presidencial)
checkboReturn = st.sidebar.checkbox("Mostrar Graficos da eleica legilativa ")
if checkboReturn == True:        
    with graficos_presidencial:        
        with div1:
            
            grafico_pie(categoria_presidencial, valores_presidencial)
        with div2:
            grafico_barra(categoria_presidencial, valores_presidencial) 
    

# Seccao da eleicao legilativa



   
with graficos_legilativa:
    st.subheader('Quadro Geral da eleicao Legilaiva de 1992')
    st.text("uma analise sobre os dados das  eleicao geral em Angola")
    
    checkboReturn = st.sidebar.checkbox("Filtrar Partidos")
    st.write("")
 
    if checkboReturn == True:
        recebe =  st.sidebar.selectbox('Partidos', df_legilativa ) 
        if recebe == "":
            # st.write("Seleciona um candidados")
            st.dataframe(df_legilativa.loc[df_legilativa['Partidos']== recebe])
        else: 
            # st.write(recebe) 
            st.dataframe(df_legilativa.loc[df_legilativa["Partidos"]== recebe]) 
            # st.dataframe(df_presidencial)
    else:
        st.dataframe(df_legilativa) 
        

    # div1
    #     grafico_pie(categoria_legilativa, valores_legilativa)
    # div2    
    # grafico_barra(categoria_legilativa, valores_legilativa)


checkboReturn = st.sidebar.checkbox("Mostrar Graficos da eleica legilativa")
if checkboReturn == True:
    with div1:
        grafico_pie(categoria_legilativa, valores_legilativa)
    with div2:
        # grafico_pie(categoria_legilativa, valores_legilativa)
        
        grafico_barra(categoria_legilativa, valores_legilativa)
