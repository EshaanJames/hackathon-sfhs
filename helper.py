import streamlit as st
import pandas as pd


def helper(name):
    st.title(f"Hey {name} How would you like to help us")
    help_kind = st.selectbox("See available options:", ['Interact ', 'Donate Funds', 'Provide materials'])
    if help_kind == 'Interact ':
        select_subject = st.selectbox("Select the preferred subject you want to teach", ['None', 'Language', 'Archeology', 'Science', 'Python Programming', 'Maths Tricks', 'Doodling'])
        df = pd.read_csv("students_data.csv")
        if st.button("Show Students Data"):
            st.header("Available students are:")
            avail_stud=df[df['Subject interested in'] == select_subject]
            st.table(avail_stud)
    if help_kind == 'Donate Funds':
        funds = st.slider("Select amount of funds you want to donate (in thousands)", 1, 1000, 1)
        transac_medium = st.selectbox("Select mode of payment:", ['Debit Card', 'Credit Card', 'UPI', 'Cheque'])
        if st.button("Confirm Amount"):
            st.success(f"Thank you {name} "
                       f" You want to donate {funds}000 via {transac_medium} "
                       f" The Team will contact you later")
    if help_kind == 'Provide materials':
        materials = st.multiselect("Select the material you want to donate.", ['Stationary', 'Uniforms', 'Projectors', 'Laptops', 'Tablets', 'Computers'])
        material_list = {}
        if 'Stationary' in materials:
            stationary = st.slider("Select amount of stationary kits you want to donate:", 1, 1000, 1)
            material_list['stationary'] = stationary
        if 'Uniforms' in materials:
            uniforms = st.slider("Select amount Uniforms you want to donate:", 1, 1000, 1)
            material_list['uniforms'] = uniforms
        if 'Projectors' in materials:
            projectors = st.slider("Select amount of projectors you want to donate:", 1, 1000, 1)
            material_list['projectors'] = projectors
        if 'Laptops' in materials:
            laptops = st.slider("Select amount of Laptops you want to donate:", 1, 1000, 1)
            material_list['laptops'] = laptops
        if 'Tablets' in materials:
            tablets = st.slider("Select amount of tablets  you want to donate:", 1, 1000, 1)
            material_list['tablets'] = tablets
        if 'Computers' in materials:
            computers = st.slider("Select amount of computers you want to donate:", 1, 1000, 1)
            material_list['computers'] = computers
        if st.button("Confirm Materials"):
            st.success("You want to donate following materials")
            st.header(material_list)
            st.subheader('The Team will contact you')



