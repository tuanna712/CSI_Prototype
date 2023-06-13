import lasio
import streamlit as st
from io import StringIO

from functions.funcLog import *

def tab2_main():
    #Read LAS file from Uploader
    las_stringio = las_file_uploader()
    #Convert LAS file to DataFrame
    las_df = read_las_file(las_stringio)
    #Retrieve Curves List
    if las_df is not None:
        _curves_name = las_df.columns
        #Curves Plotting Selection
        selected_curvs = select_curvs_plotting(_curves_name)
        #Plot selected curves
        if "DEPTH" in _curves_name:
            depth_col = "DEPTH"
        else: 
            depth_col = "DEPT"
        view_curves(data=las_df, curves=selected_curvs, depth_col=depth_col)
    pass

def las_file_uploader():
    uploaded_file = st.file_uploader("LAS file uploader", 
                                     type = ['las'],
                                     accept_multiple_files=False)
    if uploaded_file is not None:
        return StringIO(uploaded_file.getvalue().decode("utf-8"))

def select_curvs_plotting(_curves_name):
    _curves_name = _curves_name.tolist()
    if "DEPTH" in _curves_name:
        _curves_name.remove("DEPTH")
    if "DEPT" in _curves_name:
        _curves_name.remove("DEPT")
    options = st.multiselect(
                            'Select curves fot plotting',
                            _curves_name,
                            )
    return options