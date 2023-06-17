import pandas as pd
import streamlit as st

from ui import *
from functions import *
img = Image.open("./assets/images/logo.png")
st.set_page_config(# Alternate names: setup_page, page, layout
                layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
                initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
                page_title="Seismic Inversion",  # String or None. Strings get appended with "• Streamlit". 
                page_icon=img,  # String, anything supported by st.image, or None.
                )
# --- LOAD CSS ---
with open("./style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#-Configure-Pages----------------------
# pageConfig()

#-Tabs-Definition----------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Seismic View",
    "Log View",
    "EEI Workbench",
    "Inversion Input",
    "Well Forward Modeling",
    "Seismic Inversion Results",
])

#-Tabs-Custom--------------------------
with tab1:
    # st.header("SEISMIC VIEW")
    tab1_main()
    pass
with tab2:
    # st.header("LOG VIEW")
    tab2_main()
with tab3:
    # st.header("EEI WORKBENCH")
    tab3_main()
    
with tab4:
    # st.header("INVERSION INPUT")
    tab4_main()

with tab5:
    # st.header("FOWARD MODELING AT WELL")
    tab5_main()

with tab6:
    # st.header("SEISMIC INVERSION RESULTS")
    tab6_main()