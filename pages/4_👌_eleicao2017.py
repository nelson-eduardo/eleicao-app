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


with header:
    st.title("Analise da eleicao de 2017")
    st.subheader("Este aplicativo foi um estudo pessoal sobre as eleicoes em Angola!!")