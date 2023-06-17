import streamlit as st
from functions.funcLog import *
from io import StringIO
from PIL import Image

def tab3_main():
    subtab1, subtab2, subtab3 = st.tabs([
                            "EEI Analysis ", 
                            "Bandpass Filter & CI Est",
                            "EEI Application"
                            ])
    with subtab1:
        _top_container_1 = st.container()
        with _top_container_1:
            _top_cols = st.columns(2)
        ui_subtab1_opt()
        with _top_cols[0]:
            st.image(Image.open('./assets/demo_imgs/eeiworkbench_analysis_1.png'))
        with _top_cols[1]:
            st.image(Image.open('./assets/demo_imgs/eeiworkbench_analysis_2.png'))
            
    with subtab2:
        _top_container_2 = st.container()
        with _top_container_2:
            st.image(Image.open('./assets/demo_imgs/eeiworkbench_BandpassFilterCIEst.png'))
        ui_subtab2_opt()
    with subtab3:
        _top_container_3 = st.container()
        with _top_container_3:
            st.image(Image.open('./assets/demo_imgs/eeiworkbench_application.png'))
        ui_subtab3_opt()

def ui_subtab1_opt():
    _cols = st.columns(4)
    with _cols[0]:
        elastic_log = st.selectbox(
                            'Elastic Log Selection:',
                            ('Bulk', 'Shear', 'Vp/Vs', 'AI', 'Lambda', 'SI', 'Density', 'Porosity', 'Saturation', 'Gamma', 'V-shale' ),
                            key="eeiw_selected_elastic_log")
    with _cols[1]:
        pass
    with _cols[2]:
        elastic_log_top = st.number_input('TOP', key="eeiw_elastic_log_top", min_value=0, value=500)
        elastic_log_bottom = st.number_input('BOTTOM', key="eeiw_elastic_log_bottom", min_value=0, value=3000)
    with _cols[3]:
        eeiw_subtab1_estimate_btn = st.button("Estimate", key='eeiw_subtab1_estimate_btn')

def ui_subtab2_opt():
    _cols = st.columns(5)
    with _cols[0]:
        st.write('Regression Line')
        eeiw_regr_intercept = st.number_input('Intercept', key="eeiw_regr_intercept", min_value=0.0, value=0.5, format="%.3f")
        eeiw_regr_gradient = st.number_input('Gradient', key="eeiw_regr_gradient", min_value=0.0, value=0.5, format="%.3f")

    with _cols[1]:
        eeiw_operator_length = st.number_input('Operator Length', key="eeiw_operator_length", min_value=0.0, value=0.5, format="%.3f")
        eeiw_taper_length = st.number_input('Taper Length', key="eeiw_taper_length", min_value=0.0, value=0.5, format="%.3f")
        eeiw_min_freq = st.number_input('Minimum Frequency', key="eeiw_min_freq", min_value=0, value=0)
    
    with _cols[2]:
        eeiw_max_freq = st.number_input('Maximum Frequency', key="eeiw_max_freq", min_value=0, value=0)
        eeiw_freq_smoother = st.number_input('Frequency Smoother', key="eeiw_freq_smoother", min_value=0.0, value=0.5, format="%.2f")
        eeiw_spectrum_threshold = st.number_input('Spectrum Threshold', key="eeiw_spectrum_threshold", min_value=0, value=5)
    
    with _cols[3]:
        eeiw_view_menu = st.selectbox(
                    label='Plot View Menu:',
                    options=(
                            'Log-Log Spectrum', 
                            'Bandpass Filtered True Log vs CI', 
                            'Frequency & Time of CI Operator',
                     ),
                    key="eeiw_view_menu",)
        st.write(f"Selected: {eeiw_view_menu}")
        
    with _cols[4]:
        eeiw_subtab2_calculate_btn = st.button("Calculate", key='eeiw_subtab2_calculate_btn')
        
def ui_subtab3_opt():
    _cols = st.columns(4)
    with _cols[0]:
        seismic_uploader('Input Seismic (A)')
    with _cols[1]:
        seismic_uploader('Input Seismic (B)')
    with _cols[2]:
        eeiw_chi_input = st.number_input('Chi Angle', key="eeiw_chi_input", min_value=0, value=0)
    with _cols[3]:
        eeiw_subtab3_calculate_btn = st.button("Calculate", key='eeiw_subtab3_calculate_btn')
        
def seismic_uploader(_label):
    uploaded_file = st.file_uploader(label=_label,
                                        type = ['sgy', 'segy'],
                                        accept_multiple_files=False)
    if uploaded_file is not None:
        return StringIO(uploaded_file.getvalue().decode("utf-8"))
    pass