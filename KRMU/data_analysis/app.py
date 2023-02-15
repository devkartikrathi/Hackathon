import pandas as pd
import plotly.express as px
import streamlit as st
from chat import coder
import ast



#===============================================================

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#===============================================================