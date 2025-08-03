import streamlit as st

st.title("My First App")

st.write("Hello How are you")

name=st.text_input("What is your name?")

if name:
    st.success("f Nice to meet you, name ")