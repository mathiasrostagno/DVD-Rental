import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='Tableau', layout="wide",page_icon='bar_chart', initial_sidebar_state='expanded')
pdfFile = open('Data/dvdrental.sql', 'rb')
st.sidebar.download_button('Download original database', pdfFile, file_name='dvdrental.sql', mime='sql')

st.markdown('# **Tableau**')
st.markdown('### And... Voilà !')
def main():
    html_temp = """
    <div class='tableauPlaceholder' id='viz1678816386454' style='position: relative'><noscript><a href='#'><img 
            alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DV&#47;DVDRental_16774909422350&#47;
            Customerrentalcat&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  
            style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
        <param name='embed_code_version' value='3' /> <param name='site_root' value='' />
        <param name='name' value='DVDRental_16774909422350&#47;Customerrentalcat' />
        <param name='tabs' value='yes' /><param name='toolbar' value='yes' />
        <param name='static_image' 
            value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DV&#47;
            DVDRental_16774909422350&#47;Customerrentalcat&#47;1.png' /> 
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='fr-FR' /></object></div>                
    <script type='text/javascript'>                    
    var divElement = document.getElementById('viz1678816386454');                    
    var vizElement = divElement.getElementsByTagName('object')[0];                    
    if ( divElement.offsetWidth > 800 ) 
        { vizElement.style.minWidth='1200px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='700px';
        vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} 
    else if ( divElement.offsetWidth > 500 ) 
        { vizElement.style.minWidth='420px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='610px';
        vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} 
    else 
        { vizElement.style.width='100%';vizElement.style.minHeight='1100px';
        vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     
    var scriptElement = document.createElement('script');                    
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
    vizElement.parentNode.insertBefore(scriptElement, vizElement);                
    
    </script>"""
    components.html(html_temp, width=1200, height=750, scrolling=True)

if __name__ == "__main__":
    main()

st.markdown('### The dashboard is designed to provide an easy-to-understand overview of customer rental behavior. '
            'It consists of two different charts, each providing a different view of the data, and three tables.')
st.markdown('### It provides a powerful tool for analyzing and understanding customer rental behavior in '
            'the "dvdrental" database. By providing an easy-to-use interface for exploring the data, '
            'the dashboard helps to uncover insights that might have been difficult to identify through other means.')


