import streamlit as st
import students
import pandas as pd
import helper

st.title("SKY System")
st.sidebar.header("We have needy school here. Help them as your will!!!")

name = st.text_input("Enter your Name Here")
if name:
    st.header(f"Hii {name} welcome to our site!!")
user = st.sidebar.selectbox("Select appropriate option:", ['None', 'Student', 'Helper'])
if user == 'Student':
    students.study(name)
if user == 'Helper':
    helper.helper(name)

data = st.sidebar.selectbox("View Dataset of schools:", ['Hide Dataset', 'View Dataset'])
if data == 'View Dataset':
    st.header("View data of rural schools")
    df = pd.read_csv('Untitled spreadsheet - Sheet1 (1).csv')
    with st.beta_expander("View Dataset"):
        st.table(df)
    st.header("View data of urban schools")
    df1 = pd.read_csv('Untitled spreadsheet - Sheet1.csv')
    with st.beta_expander("View Dataset"):
        st.table(df1)
