import streamlit as st
from PIL import Image

st.set_page_config(page_title='PostgreSQL', layout="wide",page_icon='bar_chart', initial_sidebar_state='expanded')

pdfFile = open('Data/dvdrental.sql', 'rb')
st.sidebar.download_button('Download original database', pdfFile, file_name='dvdrental.sql', mime='sql')
pgadminmain = Image.open('Screenshots/pgadminmain.png')
pgadmintables = Image.open('Screenshots/pgadmintables.png')

st.markdown('# **PostgreSQL**')
st.markdown("### As part of this project, the dvdrental database was downloaded and integrated into "
            "a PostgreSQL database running on a local computer. This allowed for seamless access to the "
            "database's contents using Python code and Jupyter Notebook.")
st.markdown("### The integration process involved setting up a PostgreSQL server on the local computer "
            "and creating a new database within it. The dvdrental database was then imported into this "
            "new database, creating a fully functional database that could be queried and manipulated "
            "using SQL commands.")
st.markdown('### With the database integrated into the PostgreSQL server, it was possible to easily connect to it '
            'using Python code and the psycopg2 library. This allowed for powerful queries to be made against the '
            'database, extracting the data needed for analysis and visualization.')
st.markdown('#### PG Admin DVD Rental Database :')
st.image(pgadminmain, caption='DVD Rental Database')
st.markdown('#### The 15 relationnal tables :')
st.image(pgadmintables, caption='DVD Rental Tables')