import streamlit as st
from streamlit_option_menu import option_menu
from home import home_operation
from settings import settings_operation
from document_analysis import document_analysis_operation
from nirf_score_calc import nirf_score_calc

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Document Analysis','Score Calculator', 'Settings'], 
        icons=['house', 'book', 'pen', 'gear'], menu_icon="cast", default_index=1)

if selected == "Home":
    home_operation()
elif selected == "Settings":
    settings_operation()
elif selected == "Document Analysis":
    document_analysis_operation()
elif selected == "Score Calculator":
    nirf_score_calc()