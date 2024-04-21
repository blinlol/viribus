import streamlit as st
import time

st.title("Add picture from cunteen")

file = st.file_uploader("Upload canteen photo")
if file:
    with open(f"bot/data_base/uploaded/{file.name}", "wb") as f:
        f.write(file.getvalue())