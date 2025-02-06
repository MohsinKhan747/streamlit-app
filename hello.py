import streamlit as st
st.write("""
# My first app
Hello *world!*
""")

number = st.slider("Pick a number",0,10)

date = st.date_input("Pick a date")