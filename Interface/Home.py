import streamlit as st
from PIL import Image
import pandas as pd
import re
from io import StringIO
import sys


st.set_page_config(
    page_title="Titanic Survivor",
    page_icon= Image.open('figures\logo.png')
)

col1, col2 = st.columns([1,2])  # You can adjust the number of columns as needed

with col1:
    st.image('figures\logo.png', width= 200)

with col2:
    st.header("Supervivencia de Titanic ")
    
st.subheader('Hola')

st.write()
st.info(
    """
    This app helps you find out if a profile would have survived the Titanic disaster. 
    """
)




    