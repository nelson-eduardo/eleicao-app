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