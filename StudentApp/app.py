import streamlit as st
import json

# Definir la función principal de la página, que contiene la lógica de la interfaz de usuario y la interacción modelo-usuario.
def main_page():

    # Usar la barra lateral de Streamlit para mostrar opciones de configuración y recibir entradas del usuario.
    with st.sidebar:
        # Mostrar un logotipo y títulos de secciones utilizando funciones de Streamlit para elementos de UI.
        st.image('dmc_logo.jpg', use_column_width="always")
        st.header(body="Encuesta inicial :memo:")
        st.subheader('Esp. Machine Learning Engineer :robot_face:')
        st.subheader('Docente: José Enrique Mejía Gamarra')

    experience = st.radio("**¿Cuál es tu nivel de experiencia en machine learning y ciencia de datos?**:", 
                            ("Principiante","Intermedio","Avanzado"))

    tools = st.multiselect(
    '**¿Con cuáles de las siguientes herramientas tienes experiencia trabajando?**',
    ['Docker','Github','Apache Airflow','MLFlow','PyCaret','FastAPI','Flask','Django','Streamlit','Shiny','Jenkins','Langchain','GPT'])

    cloud = st.multiselect(
    '**¿En qué nube tienes experiencia trabajando?**',
    ['AWS','GCP','AZURE'])

    course = st.radio("**¿En qué curso desearías profundizar más?**:", 
                            ("Fundamentos de MLE","AutoML","Serving Models","Automatización y Monitoreo","Fundamentos de LLM"))
    
    goals = st.text_input('**¿Cuáles son tus objetivos específicos al inscribirte en esta especialización?**')
    
    send_response = st.button("Enviar respuestas", type="primary")
    
    if send_response:

        user_response = {
            "experience":experience,
            "tools":tools,
            "cloud":cloud,
            "course":course,
            "goals":goals
        }

        with open("user_response.json", 'r') as file:
            data = json.load(file)

        data.append(user_response)

        # Writing JSON data
        with open("user_response.json", 'w') as f:
            json.dump(data, f, indent=4)

# Punto de entrada de la aplicación Stream
if __name__ == "__main__":
    main_page()