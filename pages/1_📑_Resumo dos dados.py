import streamlit.components.v1 as components
import streamlit as st
from pages.util.plot_pages_util import read_spotify_df, build_nota_spotify
from pages.util.plot_pages_util import numerical_cols, string_cols
import matplotlib.pyplot as plt
import seaborn as sns


#Data:
#https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
#http://dados.recife.pe.gov.br/dataset/acidentes-de-transito-com-e-sem-vitimas

def build_header():
    text ='<h1>APRESENTAÇÃO DOS DADOS</h1>'+\
    '''
    <p>Aqui seremos apresentados aos dados sem alterações, no formato original obtido.</p>
    '''
    st.write(text, unsafe_allow_html=True)

def build_section_one():
    text = '<h2>"Head" do dataset</h2>'
    st.write(text, unsafe_allow_html=True)

    st.table(df.head())

def build_section_two():
    section_title = '<h2>Formato do dataset</h2>'
    st.write(section_title, unsafe_allow_html=True)

    shape = df.shape
    section_text = f"O dataset em questão possui **{shape[0]} linhas** e **{shape[1]} colunas**."
    st.write(section_text)


def build_section_three():
    section_title = '<h2>Dados nulos no dataset</h2>'
    st.write(section_title, unsafe_allow_html=True)

    st.table(df[df.isnull().any(axis=1)])

def build_section_four():
    section_title = '<h2>Dados duplicados no dataset</h2>'
    st.write(section_title, unsafe_allow_html=True)

    duplicated_lines = df[df.duplicated()]
    section_text = f"Nesse dataset temos **{duplicated_lines.shape[0]}** linhas duplicadas"
    st.write(section_text)
    st.table(duplicated_lines.head())

def build_section_five():
    section_title = '<h2>Distribuição dos dados</h2>'
    st.write(section_title, unsafe_allow_html=True)
    
    table = df.describe().style.background_gradient(cmap="Accent")
    st.table(table)

def build_section_six():
    section_title = '<h2>Matriz de confusão</h2>'
    st.write(section_title, unsafe_allow_html=True)

    # Including numerical colmumns
    corr_mat = df.select_dtypes(include=["int", "float"]).corr()

    # Adjusting figure visuals
    fig = plt.figure(figsize=(20, 20), facecolor='#FFFFFF', edgecolor='black')
    ax = plt.axes()
    ax.set_facecolor('#F2EAC5')
    custom_palette = sns.diverging_palette(220, 20, as_cmap=True)
    sns.heatmap(corr_mat, fmt='.2f', cmap=custom_palette,
                annot=True, center=0, linewidths=0.5,
                cbar_kws={"shrink": .8})
    plt.title('Correlações entre os dados', fontsize=20)
    plt.tick_params(labelsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    st.pyplot(fig)

def build_section_seven():
    section_title = '<h2>Histogramas</h2>'
    st.write(section_title, unsafe_allow_html=True)

    sns.set_style('darkgrid')
    sns.set_theme(rc={"axes.facecolor":"#FFFFFF","figure.facecolor":"#FFFFFF"})
    features = df.select_dtypes(include=['float64', 'int64']).columns
    n_cols = len(features)
    # features.hist(figsize=(20,15), bins=30, xlabelsize=10, ylabelsize=10)
    fig, axes = plt.subplots(nrows=n_cols, ncols=1, figsize=(8, n_cols * 4))

    # Creating a histogram for each numerical column
    for ax, column in zip(axes, features):
        sns.histplot(df[column], ax=ax, kde=True, color='skyblue', bins=10)
        ax.set_title(f'Histograma de {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequência')
    
    fig.tight_layout(pad=3.0)
    st.pyplot(plt)

def build_section_eight():
    pass

def build_section_nine():
    pass

build_header()

df = read_spotify_df()

build_section_one()
build_section_two()
build_section_three()
build_section_four()
build_section_five()
build_section_six()
build_section_seven()
build_section_eight()
build_section_nine()

# build_nota_spotify()