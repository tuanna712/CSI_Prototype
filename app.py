import pandas as pd
import streamlit as st

from ui import *
from functions import *

#-Configure-Pages----------------------
pageConfig()

#-Tabs-Definition----------------------
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "Seismic View",
    "Log View",
    "EEI Workbench",
    "Inversion Input",
    "Macro-layers",
    "Lambda and Transition Matrix",
    "Auto Regressive Estimation",
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
    st.header("EEI WORKBENCH")
    pass