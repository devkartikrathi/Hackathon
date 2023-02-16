import pandas as pd
import plotly.express as px
import streamlit as st

class cleaning:

    def findnull(df):
        st.write(df.isnull().sum())
    
    def delete_null_row(df):
        df = df.dropna(inplace=True)

    def delete_asked_columns():
        cols = st.selectbox("Choose columnms to delete: ", options = df.columns[0:])
        df = df.drop([cols], axis = 1)
        print(df)

    def remove_duplicate_rows(df):
        df = df.drop_duplicates()
        print(df)

    def fillrows(df):
        options = st.selectbox("Choose with what value you want to replace null values with: ", ('mean', 'median', 'mode'))
        if st.checkbox("Submit"):
            if options == 'mean':
                df = df.fillna(df.mean())
                print(df)
            elif options == 'median':
                df = df.fillna(df.median())
                print(df)
            elif options == 'mode':
                df = df.fillna(df.mode())
                print(df)

class visualisation:

    def show_bar(df):
        """
        Creates a scatterplot of the selected features
        """
        feat_x = st.selectbox("Choose x-axis feature", df.columns[0:])
        feat_y = st.selectbox("Choose y-axis feature", df.columns[0:])
        fig = px.bar(df, x = feat_x, y = feat_y)
        fig.update_layout(margin = dict(l = 20, r = 20, t = 20, b = 10), paper_bgcolor = "LightSteelBlue")
        # fig = plt.figure(figsize = (10, 6))
        st.bar_chart(df, x = feat_x, y = feat_y)

    def show_line(df):
        """
        Creates a lineplot of the selected features
        """
        feat_x = st.selectbox("Choose x-axis feature", df.columns[0:])
        feat_y = st.selectbox("Choose y-axis feature", df.columns[0:])
        fig = px.line(df, x = feat_x, y = feat_y)
        fig.add_scatter(x = feat_x, y = feat_y)
        fig.update_layout(margin = dict(l = 20, r = 20, t = 20, b = 10), paper_bgcolor = "LightSteelBlue")
        fig.show()
    
    def show_scatter(df):
        """
        Creates a scatterplot of the selected features
        """
        feat_x = st.selectbox("Choose x-axis feature", df.columns[0:])
        feat_y = st.selectbox("Choose x-axis feature", df.columns[0:])
        fig = px.scatter(df, x = feat_x, y = feat_y)
        fig.update_layout(margin = dict(l = 20, r = 20, t = 20, b = 10), paper_bgcolor = "LightSteelBlue")
        fig.show()

    def show_pie(df):
        cols = df.columns
        num_col = df.get_numeric_data().columns_list
        cat_cols = list(set(cols) - set(num_col))
        values = list(range(len(set(cols) - set(num_col))))
        options = cat_cols
        value_num = st.selectbox("Choose the numerical value ", df.columns[num_col])
        value = st.selectbox("Choose the value for which you'd like to create a pie chart", options)
        fig = px.pie(df, names = df.loc['value'], values = value_num)
        fig.show()