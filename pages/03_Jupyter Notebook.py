import streamlit as st
from PIL import Image

st.set_page_config(page_title='Jupyter Notebook', layout="wide",page_icon='bar_chart', initial_sidebar_state='expanded')

pdfFile = open('Data/dvdrental.sql', 'rb')
st.sidebar.download_button('Download original database', pdfFile, file_name='dvdrental.sql', mime='sql')
jupyterimports = Image.open('Screenshots/imports.png')
jupyterfilmquery = Image.open('Screenshots/sql_query_film.png')
jupyterfilms = Image.open('Screenshots/film.png')
jupytercustomers = Image.open('Screenshots/customers.png')
jupyterrental = Image.open('Screenshots/rental.png')

st.markdown('# **Jupyter Notebook**')
st.markdown('### In addition to integrating the dvdrental database into a local PostgreSQL database, this project '
            'also made use of IPython and SQLAlchemy to facilitate data analysis and manipulation.')
st.markdown('### IPython, an enhanced interactive Python shell, was used to execute Python code and interactively '
            'explore the data within the Jupyter Notebook environment. With IPython, it was possible to quickly '
            'test and iterate on queries, allowing for a more efficient and streamlined analysis process.')
st.markdown('### Meanwhile, SQLAlchemy was used to interact with the PostgreSQL database directly from Python '
            'code, providing a powerful and flexible way to query and manipulate the database. By using SQLAlchemy, '
            'it was possible to create complex SQL queries and then execute them seamlessly within the Python '
            'environment.')
st.markdown('### Overall, the combination of PostgreSQL, IPython, and SQLAlchemy provided a robust platform for '
            'data analysis and exploration, enabling the creation of insightful visualizations and uncovering '
            'meaningful insights within the "dvdrental" database.')

st.image(jupyterimports, use_column_width='auto')

st.markdown('### To prepare for the analysis and visualization of the dvdrental database using Tableau, '
            'this project involved exporting tables created from general queries on the database to CSV files. '
            'These CSV files were then saved on a Google Drive, before being imported into Tableau.')

st.markdown('#### Here is a query to build a Film table :')
st.image(jupyterfilmquery, use_column_width='auto', caption='Film Query')

st.markdown('#### Here are queries exports to csv files :')
st.image(jupyterfilms, use_column_width='auto', caption='Film to CSV')
st.image(jupytercustomers, use_column_width='auto', caption='Customers to CSV')
st.image(jupyterrental, use_column_width='auto', caption ='Rental to CSV')

