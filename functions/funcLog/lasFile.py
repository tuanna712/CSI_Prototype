import lasio
import streamlit as st

def read_las_file(stringio):
    if stringio is not None:
        las = lasio.read(stringio)
        st.write(f"Well name: {las.well.WELL.value}")
        data = las.df().reset_index()
        return data