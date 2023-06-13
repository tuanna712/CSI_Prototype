import lasio
import streamlit as st
from io import StringIO

from functions.funcSeis import *


def tab1_main():
    sgy_file_uploader()
    pass

def sgy_file_uploader():
    uploaded_file = st.file_uploader("SGY file uploader", 
                                     type = ['sgy', 'segy'],
                                     accept_multiple_files=False)
    if uploaded_file is not None:
        return StringIO(uploaded_file.getvalue().decode("utf-8"))
