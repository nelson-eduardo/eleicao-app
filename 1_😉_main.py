# Importacao das princnipais bibliotecas

from email import header
# from turtle import color
from click import style
import streamlit as st
import pandas as pd
# criacao de container

# para os quatros campos que teremos 
header = st.container()
dataset = st.container()
feature = st.container()
model_training = st.container()

st.markdown(
""""
<style>
    .main{
       
    }
</style>

""",
unsafe_allow_html = True

)



with header:
    st.title("APlicacao sobre os dados de eleicao geral em Angola 2022")
    st.text("Neste projecto,desenvolvo um projecto de python com a platoforma Streamlit...")

with dataset:
    
    # Importacao dos dataset
    df_Produtos = pd.read_csv('Produtos.csv')
    df_Movimentos = pd.read_csv('Movimentos.csv')
    df_Clientes = pd.read_csv('Clientes.csv')
    
    st.header("Tabela do Dataset Movimentos")
    st.text("Tabela com todos os registos dos movimentos feito no banco")
    st.write(df_Movimentos.head(5))

    st.header("Tabela do Dataset Clientes")
    st.text("Tabela com todos os registos de todos os clientes no banco")

    Total_linhas = int(df_Clientes['RowNumber'].count())
    st.write(Total_linhas)
    sel_col, disp_col = st.columns(2)
    slicerClientes = sel_col.slider("Introduz numero de registo a apresentar", min_value= 0, max_value= Total_linhas , step=1, value=0)
    st.write(df_Clientes.head(slicerClientes))
    
    teste = df_Clientes['Surname']
    st.write( teste )
    variavel_nome = st.text_input("Digita qualquer coisa", 'Digite o nome do Cliente')
    linhaCluna = df_Clientes.loc[df_Clientes['Surname'] == variavel_nome]
    st.write(linhaCluna)

    st.subheader('Legenda para o nosso grafico...!')

    
    
    # teste = pd.DataFrame(df_Movimentos['CustomerId'].value_counts()).head(max1)
    # st.bar_chart(teste)

with feature:
    st.header("APlicacao sobre os dados de eleicao geral em Angola 2022")
    st.text("Neste projecto,desenvolvo um projecto de python com a platoforma Streamlit...")

with model_training:
    st.header("APlicacao sobre os dados de eleicao geral em Angola 2022")
    # st.button("botao para download")
    # st.camera_input("Sorrir! Estas a ser filmado!")
    st.text("Neste projecto,desenvolvo um projecto de python com a platoforma Streamlit...")


# Novos testes
sel_col1, disp_col = st.columns(2)
# max_diph = sel_col.slider("Qual seria o valor para a profundidade", min_value= 10, max_value= 100, step=1, value=0)

bloco_selecao = sel_col.selectbox("Seleciona uma das opcoes",["Homem", "Mulher", "Nenhum"])
# entrada = st.text_input("Digita qualquer coisa", 'categorias')

# st.write(max_diph)
st.write(bloco_selecao)