import pandas as pd
import streamlit as st
# import plotly.express as px
from utils import read_df

def build_nota_spotify():
    with st.expander('¹Notas sobre o dataset do Spotify'):
        st.write(
        '''
        <table>
            <tr><th>COLUNA ORGIGINAL</th><th>COLUNA</th><th>DESCRIÇÃO</th></tr>
            <tr><td>track_id</td><td>id</td><td>O Id da música.</td></tr>
            <tr><td>artists</td><td>nome</td><td>Nome do passageiro.</td></tr>
            <tr><td>album_name</td><td>sobreviveu</td><td>Sobreviveu: 0 = Não, 1 = Sim</td></tr>
            <tr><td>track_name</td><td>classe</td><td>Classe do Passageiro: 1 = 1a. classe, 2 = 2a classe, 3 = 3a classe</td></tr>
            <tr><td>popularity</td><td>sexo</td><td>Sexo</td></tr>
            <tr><td>duration_ms</td><td>idade</td><td>Idade em anos</td></tr>
            <tr><td>explicit</td><td>irmaos</td><td># de irmãos/esposa no Titanic.</td></tr>
            <tr><td>danceability</td><td>pais</td><td># de pais/filhos no Titanic.</td></tr>
            <tr><td>energy</td><td>id_passagem</td><td>Número da passagem.</td></tr>
            <tr><td>key</td><td>tarifa</td><td>Tarifa da passagem.</td></tr>
            <tr><td>loudness</td><td>cabine</td><td>Número da cabine</td></tr>
            <tr><td>mode</td><td>cabine</td><td>Número da cabine</td></tr>
            <tr><td>speechiness</td><td>cabine</td><td>Número da cabine</td></tr>
            <tr><td>acousticness</td><td>cabine</td><td>Número da cabine</td></tr>
            <tr><td>instrumentalness</td><td>cabine</td><td>Número da cabine</td></tr>
            <tr><td>liveness</td><td>cabine</td><td>Número da cabine</td></tr>
            <tr><td>valence</td><td>cabine</td><td>Número da cabine</td></tr>
            <tr><td>tempo</td><td>cabine</td><td>Número da cabine</td></tr>
            <tr><td>time_signature</td><td>cabine</td><td>Número da cabine</td></tr>
            <tr><td>track_genre</td><td>cabine</td><td>Número da cabine</td></tr>
        </table>
        <br>
        Notas:<br>
        Pclass: Classe do navio, relacionada à socio-econômica:<br>
        1a classe = Classe Alta<br>
        2a classe = Classe Média<br>
        3a classe = Classe Baixa<br>
        Age: Fracionada se for menor que 1. Se estimada, está no formato xx.5<br>
        Parch: Algumas crianças viajaram com babás, assim este atributo fica zerado para elas (Parch=0).
        ''', unsafe_allow_html=True)

def build_dataframe_section(df:pd.DataFrame):
    st.write('<h2>Dados do Spotify</h2>', unsafe_allow_html=True)
    st.dataframe(df)


def read_spotify_df() -> pd.DataFrame:
    df = read_df('spotfy_tracks_dataset')
    return df

def numerical_cols():
    df = read_spotify_df()
    df = df.select_dtypes(include=["int", "float"]) #df[df.columns[(df.dtypes == 'float64') | (df.dtypes == 'int64')]]
    return df

def string_cols():
    pass

# def __ingest_titanic_data() -> pd.DataFrame:
#     df = read_df('titanic')
#     df.rename(columns={
#         'PassengerId':'id','Name':'nome',
#         'Survived':'sobreviveu_val','Pclass':'classe_val',
#         'Sex':'sexo','Age':'idade','SibSp':'irmaos',
#         'Parch':'pais','Ticket':'id_passagem',
#         'Fare':'tarifa','Cabin':'cabine','Embarked':'embarque'
#     }, inplace=True)
#     return df

# def __transform_titanic_data(df:pd.DataFrame) -> pd.DataFrame:
#     df['sobreviveu'] = df['sobreviveu_val'].map({
#         0: 'Não', 1: 'Sim',
#     })
#     df['classe'] = df['classe_val'].map({
#         1: 'Primeira', 2: 'Segunda', 3: 'Terceira',
#     })
#     df.sort_values(by=['classe_val','idade','id'], inplace=True)
#     return df

# def read_titanic_df() -> pd.DataFrame:
#     return __transform_titanic_data(__ingest_titanic_data())

# def __get_color_sequence_map() -> dict[str,list[str]]:
#     def filter(colors) -> list[str]:
#         #código usado para alternar as cores, para aumentar a diferença da tonalidade
#         return [x for idx, x in enumerate(colors) if idx%2!=0]
#     result = {
#         'Azul (reverso)': filter(px.colors.sequential.Blues_r),
#         'Azul': filter(px.colors.sequential.Blues),
#         'Plasma (reverso)': filter(px.colors.sequential.Plasma_r),
#         'Plasma': filter(px.colors.sequential.Plasma),
#         'Vermelho (reverso)': filter(px.colors.sequential.Reds_r),
#         'Vermelho': filter(px.colors.sequential.Reds),
#     }
#     return result

# def get_color_sequence_names() -> list[str]:
#     return __get_color_sequence_map().keys()

# def get_color_sequence(name) -> list[str]:
#     return __get_color_sequence_map()[name]
