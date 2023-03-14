import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title='Google Drive', layout="wide",page_icon='bar_chart', initial_sidebar_state='expanded')
pdfFile = open('Data/dvdrental.sql', 'rb')
st.sidebar.download_button('Download original database', pdfFile, file_name='dvdrental.sql', mime='sql')

googledrive = Image.open('Screenshots/drive.png')
connect = Image.open('Screenshots/connect.png')
tableauconnect = Image.open('Screenshots/tableauconnect.png')
Films = pd.read_csv('Data/Films.csv')
Customers = pd.read_csv('Data/Customers.csv')
Rental = pd.read_csv('Data/Rental.csv')
Staff = pd.read_csv('Data/Rental_staff.csv')

st.markdown('# **Google Drive & Connection to Tableau**')
option = st.selectbox('Select a CSV file to visualize it', ('None', 'Films', 'Customers', 'Rental', 'Staff'))

if option == 'None':
    st.write('')
if option == 'Films':
    st.dataframe(Films)
if option == 'Customers':
    st.dataframe(Customers)
if option == 'Rental':
    st.dataframe(Rental)
if option == 'Staff':
    st.dataframe(Staff)


st.markdown('### The decision to save the CSV files on a Google Drive was made in order to facilitate easy '
            'access and sharing of the files between potential team members. By storing the files on Google Drive, '
            'they could be easily shared with others and accessed from any device with an internet connection.')
st.image(googledrive, caption='Google Drive')
st.markdown("### The process of connecting the CSV files to Tableau was relatively straightforward. "
            "Tableau offers a number of different ways to connect to data sources, including Google Drive. "
            "Once the CSV files were connected to Tableau, they could be easily manipulated and visualized "
            "using Tableau's powerful tools.")
col1, col2 = st.columns([3,1])

with col1:
    st.image(tableauconnect)
with col2:
    st.image(connect)