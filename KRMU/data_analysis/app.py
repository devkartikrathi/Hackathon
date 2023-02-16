#=======================LIBRARIES===============================

import pandas as pd
import plotly.express as px
import streamlit as st
from chat import coder
import ast
from streamlit_option_menu import option_menu
from da import *

#===================== PAGE CONFIGURATION ==========================

st.set_page_config(page_title = "Data Analysis", 
                page_icon=":bar_chart:", 
                layout="wide"
)

#======================== FILE UPLOAD ==============================

st.header(":red[Data Analysis]")
st.subheader("One stop solution to all your data related problems!!!")

_file = st.file_uploader("Choose a file", type=['csv','xlsx'])

if _file:
    try:
        df=pd.read_csv(_file,sep=",")
    except:
        try:
            df = pd.read_excel(_file)
        except:      
            df=pd.DataFrame()

if st.checkbox("Show Data"):
    st.write(df)

#================== OPTION MENU ============================

page = option_menu(
    None,
    ["Cleaning", "Visualization", "Chat"],
    orientation = "horizontal"
)

#======================= CLEANING =================================

if page == "Cleaning":

    c_op = ("Show all null values", "Remove duplicate rows", "")
    c_operation = st.selectbox("Select Cleaning Operation to be performed : ", c_op)

    if st.checkbox("Apply"):
        st.markdown("---")

        if c_operation == "Show all null values":
            st.subheader("All Missing values : ")
            cleaning.findnull(df)
            op = st.selectbox("Pick operation", ("Remove null valules", "Fill null values"))
            st.button("Submit")
            if op == "Remove null valules":
                cleaning.delete_null_row(df)
                cleaning.findnull(df)
            elif op == "Fill null values":
                cleaning.fillrows(df)
                cleaning.findnull(df)

#=================== VISUALIZATION ================================

elif page == "Visualization":
    pass

#======================= CHAT =============================

elif page == "Chat":

    col = st.selectbox("Choose the column :", sorted(df))
    instr = st.text_input("Enter what you need to find in this data...")
    if st.checkbox("Answer"):
        ans = coder(df, instr, col)
        code = ans._code()
        exec(code)

#=================STREAMLIT DESIGN HIDEING======================

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#===============================================================