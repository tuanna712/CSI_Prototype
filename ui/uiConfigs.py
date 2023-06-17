import streamlit as st
from PIL import Image

def pageConfig():
    st.markdown(""" <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
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
    