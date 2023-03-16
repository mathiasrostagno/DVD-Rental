import streamlit as st
from PIL import Image

st.set_page_config(page_title='Mathias Rostagno', layout="wide",page_icon='bar_chart', initial_sidebar_state='expanded')

st.markdown(
     f"""
     <style>
     .stApp {{
         background-image: url("Screenshots/shop.jpg");
         background-attachment: fixed;
         background-size: cover;
         background-color: rgba(255,255,255,0.6);
         background-blend-mode: lighten;
     }}
     </style>
     """,
     unsafe_allow_html=True
 )

shop = Image.open('Screenshots/shop.jpg')
pdfFile = open('Data/dvdrental.sql', 'rb')
st.sidebar.download_button('Download original database', pdfFile, file_name='dvdrental.sql', mime='sql')

st.markdown('# **Project Presentation**')
st.markdown("### Hi, my name is Mathias Rostagno and i'm a Data Analyst")



st.markdown('### Introducing a project that explores the fascinating world of DVD rentals through an interactive '
                'Streamlit app. Leveraging PostgreSQL, Jupyter Notebook, and Tableau, this project aims to provide insights'
                ' and visualizations based on the "dvdrental" database. ')
st.markdown('### To start, the "dvdrental" database is integrated '
                'into the project using PostgreSQL. This allows for seamless querying and manipulation of the database '
                'using Python code. With Jupyter Notebook, various queries are made to extract relevant data from the '
                'database and then exported to CSV format. These CSV files are then uploaded to Google Drive, where they '
                'can be easily accessed by the Tableau visualization tool. ')

st.markdown('### With Tableau, the data is analyzed and '
                'visualized in an interactive and user-friendly way. The visualizations include insights such as the most '
                'rented movies, the most popular rental duration, and the most active rental store. These visualizations '
                'allow for a deep understanding of the patterns and trends within the DVD rental industry. ')

st.markdown('### All of this '
                'analysis is presented in an easy-to-understand Streamlit app. '
                'With this project, I hope to offer a comprehensive and engaging exploration of the "dvdrental" '
                'database, and provide valuable insights into the world of DVD rentals.')
st.markdown('### Although it is possible to directly connect Tableau to a PostgreSQL database like "dvdrental", '
            'for this project i decided to take a more manual approach to demonstrate my technical skills')