import streamlit as st
from functions.funcLog import *
from PIL import Image

def tab6_main():
    _top_container = st.container()
    
    ui_opts()
    
    with _top_container:
        st.image(Image.open('./assets/demo_imgs/inversionResult.png'))
        pass

def ui_opts():
    _cols = st.columns([7,3])
    with _cols[0]:
        invresult_elastic_log = st.selectbox(label='Elastic Log Selection',
                                            options=['Origin Seismic Section',
                                                    'Best Porosity, Best V-shale, with variances (check mark)',
                                                    'Best Vp, Best Vs, Best Density with variances (check mark)',
                                                    'Sand Probability',
                                                    ],
                                            key='invresult_elastic_log',
                                            )
    with _cols[1]:
        invresult_process_btn = st.button("Process", key='invresult_process_btn')
        
    pass
