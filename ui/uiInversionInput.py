import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st
from io import StringIO
from functions.funcLog import *
from PIL import Image

def tab4_main():
    subtab1, subtab2, subtab3, subtab4 = st.tabs([
        "Inversion Input",
        "Macro-layers",
        "Lambda and Transition Matrix",
        "Auto Regressive Estimation",
        ])
    
    with subtab1:
        #Inversion Input
        _top_container_1 = st.container()
        ui_subtab1()
    
    with subtab2:
        #Macro-layers
        _top_container_2 = st.container()
        with _top_container_2:
            st.image(Image.open('./assets/demo_imgs/macrolayers.png'), 
                     use_column_width=False)
        macro_layers_name = ui_subtab2()
    
    with subtab3:
        #Lambda and Transition Matrix
        _top_container_3 = st.container()
        
        ui_subtab3(macro_layers_name)
    
    with subtab4:
        #Auto Regressive Estimation
        _top_container_4 = st.container()
        
        ui_subtab4(macro_layers_name)

#Inversion Input
def ui_subtab1():
    _cols = st.columns(5)
    with _cols[0]:
        inversioninput_uploader('Seismic EEI Loader', _type=['sgy', 'segy'])
        
    with _cols[1]:
        inversioninput_uploader('Well LAS Loader', _type=['las'])
        
    with _cols[2]:
        invin_num_litho = st.number_input('Number of Litho:', key="invin_num_litho", min_value=0, value=3)
        
    with _cols[3]:
        pass
    
    with _cols[4]:
        invin_subtab1_calculate_btn = st.button("Display", key='invin_subtab1_calculate_btn')
        
#Macro-layers
def ui_subtab2():
    _cols = st.columns([2, 6, 2])
    with _cols[0]:
        invin_num_macrolayer = st.number_input('Number of Macro Layers:', key="invin_num_macrolayer", min_value=0, value=3)
    with _cols[1]:
        # Create a list of row names
        macro_layers_name = ['Macro Layer {}'.format(i) for i in range(1, invin_num_macrolayer+1)]
        # Create an empty DataFrame with the specified columns and row names
        df = pd.DataFrame(0, index=macro_layers_name, columns=['Top', 'Top Shift', 'Base', 'Base Shift'])
        # Print the DataFrame
        edited_df = st.data_editor(df)
    with _cols[2]:
        invin_subtab2_apply_btn = st.button("Apply", key='invin_subtab2_apply_btn')
    
    return macro_layers_name

#Lambda and Transition Matrix
def ui_subtab3(macro_layers_name):
    #-----------------------------------
    _col_top = st.columns(2)
    with _col_top[0]:
        container_1 = st.container()
    with _col_top[1]:
        container_2 = st.container()
    #-----------------------------------
    _col = st.columns(4)
    with _col[0]:
        #Selectbox to select the ML for displaying
        invin_lambda_selected_ml = st.selectbox('Macro Layers:', options=macro_layers_name, 
                                   key='invin_lambda_selected_ml')
    with _col[1]:
        #Define Dt value
        invin_dt_value = st.number_input('Dt value', key="invin_dt_value", min_value=0.0, value=0.5, format="%.2f")
        
    #Display the Table and TransitionMatrix
    if invin_lambda_selected_ml is not None:
        with container_1:
            container_1.write(invin_lambda_selected_ml)
            container_1.table(lambda_dataframe(np.array(lambda_MacroLayers[invin_lambda_selected_ml])))

            arr = np.array(transition_matrix[invin_lambda_selected_ml])
            # Create column and index names
            columns = ['Litho {}'.format(i) for i in range(arr.shape[1])]
            index = ['Litho {}'.format(i) for i in range(arr.shape[0])]

            # Create DataFrame
            transition_matrix_df = pd.DataFrame(arr, index=index, columns=columns)
            st.write(invin_lambda_selected_ml)
            edited_transition_matrix_df = st.data_editor(transition_matrix_df, use_container_width=True)
            
        with container_2:
            st.image(Image.open('./assets/demo_imgs/litho_log.png'))
            
#Auto Regressive Estimation
def ui_subtab4(macro_layers_name):
    #DisplayContainer-----------------------------------
    display_container = st.container()
    with display_container:
        st.image(Image.open('./assets/demo_imgs/auto_regr_est.png'), use_column_width=False)
    #OptionsContainer-----------------------------------
    opt_container = st.container()
    with opt_container:
        #ML Selection-----------------------------------
        _cols = st.columns(4)
        with _cols[0]:
            #Selectbox to select the ML for displaying
            invin_ARE_selected_ml = st.selectbox('Macro Layers:', options=macro_layers_name, 
                                    key='invin_ARE_selected_ml')
        #Intercept/Gradient Definition------------------
        with _cols[1]:
            invin_regr_intercept = st.number_input('Intercept', key="invin_regr_intercept", min_value=0.0, value=0.5, format="%.3f")
            invin_regr_gradient = st.number_input('Gradient', key="invin_regr_gradient", min_value=0.0, value=0.5, format="%.3f")
        #Intercept/Gradient Definition------------------
        with _cols[2]:
            st.write("AR order (1,2,3,4..number field)\
                    Display of AR parameters for Por, V-sh, Vp\
                    Cross plot of Por & K-dry\
                    ")
        #Subtab4 Action Button--------------------------
        with _cols[3]:
            invin_subtab4_estimate_btn = st.button("Estimate", key='invin_subtab4_estimate_btn')
            
#File Uploader Function
def inversioninput_uploader(_label, _type):
    uploaded_file = st.file_uploader(label=_label,
                                        type = _type,
                                        accept_multiple_files=False)
    if uploaded_file is not None:
        return StringIO(uploaded_file.getvalue().decode("utf-8"))