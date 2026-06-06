import streamlit as st

from src.data_loader import load_data
from src.profiler import (
    get_shape,
    get_dtypes,
    get_misssing_values
    
)

st.title("AI Powered Data Analyst Assistant")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type = ["csv"]
)

if uploaded_file:

    df = load_data(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    rows, cols = get_shape(df)

    st.subheader("Dataset Shape")
    st.write(f"Rows: {rows}")
    st.write(f"Columns: {cols}")


    st.subheader("Data Types")
    st.write(get_dtypes(df))

    st.subheader("Missing values")
    st.write(get_misssing_values(df))

