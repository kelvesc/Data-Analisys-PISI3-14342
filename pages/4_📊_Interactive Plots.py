import streamlit as st
import pandas as pd
import plotly.express as px

from pages.util.plot_pages_util import read_spotify_df, build_nota_spotify

# Carregar o conjunto de dados
df = read_spotify_df() #pd.read_csv('seu_dataset.csv')  # Substitua 'seu_dataset.csv' pelo nome do seu arquivo CSV

# Definir título do aplicativo
st.title('Gráfico de Dispersão Interativo por Gênero Musical')

build_nota_spotify()

# Verifique se o DataFrame foi carregado corretamente
if df is not None: # and not df.empty:
    # Definir título do aplicativo
    st.title('Gráfico de Dispersão Interativo por Gênero Musical')

    # Selecionar as características para plotagem
    feature1 = st.selectbox('Selecione a característica para o eixo x:', df.select_dtypes(include=['float64', 'int64']).columns)
    feature2 = st.selectbox('Selecione a característica para o eixo y:', df.select_dtypes(include=['float64', 'int64']).columns)

    # Criar o gráfico de dispersão interativo
    fig = px.scatter(df, x=feature1, y=feature2, color='track_genre', title='Gráfico de Dispersão Interativo por Gênero Musical')

    # Exibir o gráfico no aplicativo
    st.plotly_chart(fig)
else:
    st.error("Falha ao carregar o conjunto de dados. Verifique o caminho do arquivo e tente novamente.")