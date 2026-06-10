import streamlit as st
# Cursor
st.markdown("""
            <style>
            div[data-baseweb="select] > div {
            cursor: pointer;
            }
            div[role="listbox"] ul li{
            cursor: pointer;
            }
            </style>
            """, unsafe_allow_html=True)

# Import visualization functions
from src.visualizer import create_histogram
from src.visualizer import create_boxplot
from src.visualizer import create_heatmap
from src.insights import generate_insights
from src.narrator import generate_summary
from src.query_engine import answer_question
from src.ai_assistant import ask_gemini
from src.report_generator import generate_report


# Import CSV loader
from src.data_loader import load_data

# Import dataset prifiling functions
from src.profiler import (
    get_shape,
    get_dtypes,
    get_misssing_values   
)

# Application title
st.title("AI Powered Data Analyst Assistant")

#Upload CSV file
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type = ["csv"]
)


#Run analysis only after a file is uploaded
if uploaded_file:

    #Load CSV into DataFrame
    df = load_data(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    #Displays dataset dimensions
    rows, cols = get_shape(df)

    st.subheader("Dataset Shape")
    st.write(f"Rows: {rows}")
    st.write(f"Columns: {cols}")

    # Show descriptive statistics
    st.subheader("Dataset Statistics")
    st.write(df.describe())

    # Show column Data types
    st.subheader("Data Types")
    st.write(get_dtypes(df))

    # Show missing values count
    st.subheader("Missing values")
    st.write(get_misssing_values(df))


    # Find all numeric columns automatically
    numeric_columns = df.select_dtypes(
        include = ['int64', 'float64']
    ).columns

   
    # Column Explorer section
    st.subheader("Column Explorer")

    numeric_columns = df.select_dtypes(include="number").columns

    # Display available numeric columns
    st.write("Numeric Columns Found: ")
    st.write(list(numeric_columns))

    selected_column = st.selectbox(
        "Select Numeric Column",
        numeric_columns
    )

    st.subheader("AI Insights")

    insights = generate_insights(df, selected_column)

    for insight in insights:
        st.write(insight)

        st.subheader("AI Generated Summary")

        summary = generate_summary(df, selected_column)

        st.write(summary)


    # Histogram visualization
    st.subheader("Histogram")
    fig = create_histogram(
        df,
        selected_column
    )
    st.pyplot(fig)


    # Boxplot visualization
    st.subheader("Boxplot")
    box_fig = create_boxplot(
        df,
        selected_column
    )
    st.pyplot(box_fig)

    # Correlation analysis
    st.subheader("Correlation Heatmap")
    heatmap_fig = create_heatmap(df)
    st.pyplot(heatmap_fig)


    st.subheader("Ask Questions About Your Dataset")

    question = st.text_input(
        'Ask a question'
    )

    if question:
        response = answer_question(df, question)

        st.success(response)

    # AI Chat

    st.subheader("AI Data Analyst Chat")

    ai_question = st.text_area(
        "Ask anything about your dataset"
    )

    if st.button("Generate AI Response"):
        with st.spinner("Anlayzing dataset..."):
            response = ask_gemini(
                df, ai_question
            )
        st.success(response)

        report = generate_report(
            selected_column,
            insights,
            summary,
            response
        )

        st.download_button(
            label="Download Analysis Report",
            data=report,
            file_name="analysis_report.txt",
            mime="text/plain"
        )