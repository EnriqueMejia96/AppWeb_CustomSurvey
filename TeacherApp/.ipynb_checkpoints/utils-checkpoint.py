import streamlit as st
import plotly.express as px
from collections import Counter
from wordcloud import WordCloud
import pandas as pd
from google.cloud import storage
import json

def join_json():
    # Set up Google Cloud Storage client
    client = storage.Client()

    # The name of your GCS bucket
    bucket_name = 'my-bucket-dmc'

    # The path of the directory in the bucket (omit leading and trailing slashes)
    directory_path = 'CustomSurvey'

    # Initialize an empty list to store the contents of all JSON files
    all_data = []

    # Get the bucket object
    bucket = client.bucket(bucket_name)

    # List all objects in the specified directory
    blobs = bucket.list_blobs(prefix=directory_path + '/')

    # Loop through each file (blob) in the directory
    for blob in blobs:
        # Check if the blob is a JSON file (assuming they end with '.json')
        if blob.name.endswith('.json'):
            # Download the blob's contents as a string
            json_data = blob.download_as_string()

            # Convert the string to a Python dictionary
            data = json.loads(json_data)

            # Append the data to the list
            all_data.append(data)
 
    return all_data


def plot_experience(data):
    # Process the data to count the occurrences of each experience level
    experience_counts = {}
    for item in data:
        experience = item['experience']
        if experience in experience_counts:
            experience_counts[experience] += 1
        else:
            experience_counts[experience] = 1

    # Convert the counts to a format suitable for Plotly Express
    experience_data = [{"Nivel de experiencia": key, "Número de estudiantes": value} for key, value in experience_counts.items()]

    # Create a bar plot with Plotly Express
    fig = px.bar(experience_data, x="Nivel de experiencia", y="Número de estudiantes", title="Nivel de experiencia de estudiantes")

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

def plot_cloud(data):
    cloud_counts = Counter()
    for item in data:
        for cloud in item['cloud']:
            cloud_counts[cloud] += 1

    # Convert the counts to a format suitable for Plotly Express
    cloud_data = [{"Cloud Platform": key, "Número de estudiantes": value} for key, value in cloud_counts.items()]

    # Create a bar plot with Plotly Express
    fig_cloud = px.bar(cloud_data, x="Cloud Platform", y="Número de estudiantes", title="Experiencia en nube")

    # Display the plot in Streamlit
    st.plotly_chart(fig_cloud, use_container_width=True)

def plot_tools(data):
    tools_counts = Counter()
    for item in data:
        for tools in item['tools']:
            tools_counts[tools] += 1

    # Convert the counts to a format suitable for Plotly Express
    tools_data = [{"Herramientas de programación": key, "Número de estudiantes": value} for key, value in tools_counts.items()]

    # Create a bar plot with Plotly Express
    fig_tools = px.bar(tools_data, x="Herramientas de programación", y="Número de estudiantes", title="Experiencia en herramientas")

    # Display the plot in Streamlit
    st.plotly_chart(fig_tools, use_container_width=True)

def plot_course(data):
    courses_counts = {}
    for item in data:
        course = item['course']
        if course in courses_counts:
            courses_counts[course] += 1
        else:
            courses_counts[course] = 1

    # Convert the counts to a format suitable for Plotly Express
    course_data = [{"Cursos de especialización": key, "Número de estudiantes": value} for key, value in courses_counts.items()]

    # Create a bar plot with Plotly Express
    fig = px.bar(course_data, x="Cursos de especialización", y="Número de estudiantes", title="Interés en cursos")

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)


def plot_wordcloud_for_goals(data):
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)

    # Combine all goals into one large string
    text = ' '.join(df['goals'].dropna())
    
    # List of words to exclude
    exclude_words = set(['y', 'e', 'o', 'u', 'a', 'de', 'la', 'el', 'en', 'un', 'una', 'que', 'con', 'por', 'para', 'es', 'lo',
                         'se', 'esta', 'del', 'este', 'las', 'si', 'al', 'favor', 'tiene', 'ya', 'tenemos', 'los', 'como', 
                         'solo', 'gracias', 'hora', 'su', 'pero', 'donde', 'esa', 'hay', 'nos'])
    
    # Filter out the excluded words
    text = ' '.join([word for word in text.split() if word.lower() not in exclude_words])
    
    # Generate and display WordCloud
    wordcloud = WordCloud(background_color='white', width=800, height=400).generate(text)
    st.image(wordcloud.to_array())