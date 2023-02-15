import pandas as pd
import plotly.express as px
import streamlit as st
from test import coder
import ast

#print(torch.cuda.get_device_name(0))

st.set_page_config(page_title = "Data Analysis", 
                page_icon=":bar_chart:", 
                layout="wide"
)

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

# if st.checkbox("Submit File"):
#     st.write(df)
#     col = st.selectbox("Choose the column :", sorted(df))
#     instr = st.text_input("Enter what you need to find in this data...")
#     answer = st.checkbox("Answer")
#     if answer:
#         print("HI")
#         ans = coder(df, instr, col)
#         print(ans.code_)
#         try:
#             exec(ans.code_)
#         except:
#             tree = ast.parse(ans.code_)
#             exec(compile(tree, filename="<ast>", mode="exec"))
#     else:
#         st.write("Fill all the feilds first!!!")

#-------------------------------------------------------------------------------

    # op = ("Cleaning", "Exploration", "Visualization")

    # st.sidebar.header(":red[Please select here : ]")
    # operation = st.sidebar.selectbox("Select Operation to be performed : ", op)

    # c_op = ("Show all null values", )
    # e_op = ()

    # if st.sidebar.checkbox("Submit"):
    #     st.sidebar.markdown("---")
    #     if operation == "Cleaning":
    #         c_operation = st.sidebar.selectbox("Select Cleaning Operation to be performed : ", c_op)
    #         if st.sidebar.checkbox("Apply"):
    #             print(c_operation)
    #             st.sidebar.markdown("---")
    #             if c_operation == "Show all null values":
    #                 st.subheader("All Missing values : ")
    #                 st.write(df.isnull().sum())
    #     elif operation == "Exploration":
    #         pass

#-------------------------------------------------------------------------------

