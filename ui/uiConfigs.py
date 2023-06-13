import streamlit as st
from PIL import Image

def pageConfig():
    img = Image.open("./assets/images/logo.png")
    st.set_page_config(# Alternate names: setup_page, page, layout
                    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
                    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
                    page_title="Seismic Inversion",  # String or None. Strings get appended with "• Streamlit". 
                    page_icon=img,  # String, anything supported by st.image, or None.
                    )
    st.markdown(""" <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style> """, unsafe_allow_html=True
            )
    padding = 0
    st.markdown(f""" <style>
                .reportview-container .main .block-container{{
                    padding-top: {padding}rem;
                    padding-right: {padding}rem;
                    padding-left: {padding}rem;
                    padding-bottom: {padding}rem;
                }} </style> """, unsafe_allow_html=True
                )
    