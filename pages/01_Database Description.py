import streamlit as st
from PIL import Image

st.set_page_config(page_title='Database', layout="wide",page_icon='bar_chart', initial_sidebar_state='expanded')

pdfFile = open('Data/dvdrental.sql', 'rb')
st.sidebar.download_button('Download original database', pdfFile, file_name='dvdrental.sql', mime='sql')
dataset = Image.open('Screenshots/Database.png')

st.markdown('# **Database Description**')
st.markdown('### The dvdrental database used in this project was originally sourced from Kaggle, a platform '
            'that hosts a wide range of datasets for data science and machine learning projects. The dvdrental '
            'database is a fictive rental database that includes information on DVD rentals, customers, stores, '
            'payments, and more.')

st.markdown('### The database is designed to mimic the operations of a real-world DVD rental business, '
            'with tables and fields that represent various aspects of the business. For example, the "film" table '
            'contains information on the movies available for rent, including the title, description, rating, '
            'and length. Meanwhile, the "customer" table contains information on the customers who rent the movies, '
            'such as their name, address, and contact information.')

st.markdown('### By analyzing this database, it is possible to gain insights into the patterns and trends within '
            'a DVD rental business. For example, one might analyze which movies are most popular, or which stores '
            'are most successful in terms of revenue.')

st.markdown("#### Here is the original structure of the DVD Rental Dataset")

st.image(dataset, caption='DVD Rental Dataset')