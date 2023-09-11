import streamlit as st
from PIL import Image
import pandas as pd
import re
from io import StringIO
import sys
import pickle
import numpy as np


st.set_page_config(
    page_title="Titanic Survivor",
    # page_icon= Image.open('figures/logo.png')
)

col1, col2 = st.columns([1,2])  # You can adjust the number of columns as needed

with col1:
    # st.image('figures/logo.png', width= 200)
    import os
    st.write(os.getcwd())

with col2:
    st.header("Supervivencia de Titanic ")

st.write()
st.info(
    """
    This app helps you find out if a profile would have survived the Titanic disaster. 
    """
)

@st.cache_data
def _read_model():
    with open(r'model.pkl', 'rb') as model_file:
        return pickle.load(model_file)

model = _read_model()

parameters, result = st.columns([1,1])  # You can adjust the number of columns as needed

with parameters:
    st.subheader('Ingresa los datos del pasajero')
    clas = st.selectbox('Clase:',(1, 2, 3))
    age = int(st.number_input(label = 'Edad:', value = 25))
    sib = int(st.number_input(label = 'Hermanos o conyuges que viajaron en el barco:', value = 0))
    par = int(st.number_input(label = 'Padres o hijos que viajaron en el barco:', value = 0))
    money = st.number_input(label = 'Costo del boleto:', value = 7.5, step = 0.1)
    port = st.selectbox('Puerto de Embarque:',('Cherbourg', 'Queenstown', 'Southampton'))
    sex = st.selectbox('Sexo:',('Hombre', 'Mujer'))

    x = np.array([clas, age, sib, par, money, port == 'Cherbourg', port == 'Queenstown', port == 'Southampton', sex == 'Hombre']).reshape(1,-1)
    
with result:
    st.subheader('Resultado:')
    if st.button('Calcular supervivencia'):
        if(model.predict(x)):
            # st.write('Vive')
            st.image(r'figures\rose.png', width= 300)
        else:
            # st.write('Muere')
            st.image(r'figures\jackWater.jpeg', width= 300)
