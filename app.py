import streamlit as st

from src.visualizer import create_histogram
from src.visualizer import create_boxplot
from src.visualizer import create_heatmap


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

    st.subheader("Dataset Statistics")
    st.write(df.describe())


    st.subheader("Data Types")
    st.write(get_dtypes(df))

    st.subheader("Missing values")
    st.write(get_misssing_values(df))

    numeric_columns = df.select_dtypes(
        include = ['int64', 'float64']
    ).columns

    selected_column = st.selectbox(
        "Select Numeric Column",
        numeric_columns
    )



    st.subheader("Histogram")
    fig = create_histogram(
        df,
        selected_column
    )
    st.pyplot(fig)

    st.subheader("Boxplot")
    box_fig = create_boxplot(
        df,
        selected_column
    )
    st.pyplot(box_fig)

    st.subheader("Correlation Heatmap")
    heatmap_fig = create_heatmap(df)
    st.pyplot(heatmap_fig)


