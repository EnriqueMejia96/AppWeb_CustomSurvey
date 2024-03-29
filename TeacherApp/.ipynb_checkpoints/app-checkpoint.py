import streamlit as st
st.set_page_config(layout='wide')
import json
from utils import plot_experience, plot_cloud, plot_tools, plot_course, plot_wordcloud_for_goals, join_json

# Definir la función principal de la página, que contiene la lógica de la interfaz de usuario y la interacción modelo-usuario.
def main_page():
    # Usar la barra lateral de Streamlit para mostrar opciones de configuración y recibir entradas del usuario.
    with st.sidebar:
        # Mostrar un logotipo y títulos de secciones utilizando funciones de Streamlit para elementos de UI.
        st.image('dmc_logo.jpg', use_column_width="always")
        st.header(body="Análisis descriptivo :memo:")
        st.subheader('Esp. Machine Learning Engineer :robot_face:')
        st.subheader('Docente: José Enrique Mejía Gamarra')

    data = join_json()

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            plot_experience(data)

        with col2:
            plot_cloud(data)

    with st.container():
        plot_tools(data)

    with st.container():
        plot_course(data)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('WordCloud :abcd:')
            st.subheader('')
            plot_wordcloud_for_goals(data)
    

# Punto de entrada de la aplicación Stream
if __name__ == "__main__":
    main_page()