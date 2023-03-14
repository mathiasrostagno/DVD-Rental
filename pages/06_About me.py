import streamlit as st
import streamlit.components.v1 as components
from Constantes import *
from PIL import Image


st.set_page_config(page_title='Mathias Rostagno\'s portfolio' ,layout="wide",page_icon='bar_chart', initial_sidebar_state='expanded')

st.subheader('Mathias Rostagno - Data Analyst')
Certification = Image.open('Data/Certification.png')
st.image(Certification, caption='Professional Certification')

with st.sidebar:
    components.html(embed_component['linkedin'], height=215)

st.sidebar.write('📧: mathias.rostagno@gmail.com')
pdfFile = open('Data/Mathias_Rostagno_Resume.pdf', 'rb')
st.sidebar.download_button('download resume', pdfFile, file_name='Mathias_Rostagno_Resume.pdf',mime='pdf')