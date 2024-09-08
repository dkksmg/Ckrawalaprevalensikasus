import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_embedcode import github_gist
import streamlit.components.v1 as com
import warnings

# Set wide layout
st.set_page_config(
    page_title = 'Ckrawala Buana Prevalansi Kasus',
    page_icon = '✅',
    layout = 'wide'
)

com.html("""
           <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <html>
            <body>
            <div class='tableauPlaceholder' id='viz1725786995283' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;PrevalensiKasus&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PrevalensiKasus&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;PrevalensiKasus&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1725786995283');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1200px';vizElement.style.height='2172px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1200px';vizElement.style.height='2172px';} else { vizElement.style.width='100%';vizElement.style.height='2277px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
            </body>
            </html>
            """
            , height=2700)
