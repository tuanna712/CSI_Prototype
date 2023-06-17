import streamlit as st
from functions.funcLog import *
from PIL import Image

#FORWARD-MODELING-AT-WELL------------------------
def tab5_main():
    subtab1, subtab2 = st.tabs(['Forward Modeling at Well - 1', 'Forward Modeling at Well - 2'])
    #Sub-Tab-1-------------------------
    with subtab1:
        _top_container_1 = st.container()
        ui_subtab1()
        with _top_container_1:
            st.image(Image.open('./assets/demo_imgs/well_forward_modeling.png'))
        
    #Sub-Tab-2-------------------------
    with subtab2:
        _top_container_2 = st.container()
        ui_subtab2()
        with _top_container_2:
            st.image(Image.open('./assets/demo_imgs/well_forward_modeling_2.png'))
        
#Forward Modeling at Well - 1 ---------
def ui_subtab1():
    _cols = st.columns(5)
    with _cols[0]:
        fwdMaW_well_selection = st.selectbox(label='Well Selection',
                                             options=['Well Option 1', 'Well Option 2', 'Well Option 3'],
                                             key='fwdMaW_well_selection'
                                             )
    with _cols[1]:
        fwdMaW_seis_selection_1 = st.selectbox(label='Seis Selection 1',
                                             options=['Seis Selection 1', 'Seis Selection 2', 'Seis Selection 3'],
                                             key='fwdMaW_seis_selection_1',
                                             )
        fwdMaW_seis_selection_2 = st.selectbox(label='Seis Selection 2',
                                             options=['Seis Selection 1', 'Seis Selection 2', 'Seis Selection 3'],
                                             key='fwdMaW_seis_selection_2',
                                             )
    with _cols[2]:
        st.write('Parameters for BP Log ( = Get From Color Inversion Subtab + Editable')
    with _cols[3]:
        fwdMaW_matching_criterion = st.radio(label='Matching Criterion', 
                                             options=['BP Log', 'Composite Trace'],
                                             key='fwdMaW_matching_criterion',
                                             )
    with _cols[4]:
        fwdMaW_subtab1_process_btn = st.button("Process", 
                                               key='fwdMaW_subtab1_process_btn',
                                               )


#Forward Modeling at Well - 2 ---------
def ui_subtab2():

    pass