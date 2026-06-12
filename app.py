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
from src.recommendations import generate_recommendations

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

    st.subheader("Data Cleaning")

    if st.checkbox("Remove Duplicate Rows"):
        duplicates = df.duplicated().sum()
        df = df.drop_duplicates()

        st.success(f"Removed {duplicates} duplicate rows")

    with st.expander(
        "Dataset Preview"
    ):
        st.dataframe(df)

    if df.empty:
        st.error("The uploaded CSV file is empty.")
        st.stop()

    st.success("Dataset uploaded successfully!")


    #Displays dataset dimensions
    rows, cols = get_shape(df)

    st.subheader("Dataset Shape")
    st.write(f"Rows: {rows}")
    st.write(f"Columns: {cols}")

    st.sidebar.title("AI Data Analyst Assistant")

    page = st.sidebar.radio(
        "Navigate",
        ["Overview", "Visualization", "AI Insights"]
    )
    st.sidebar.write(f"Rows: {rows}")
    st.sidebar.write(f"Columns: {cols}")

    if page == "Overview":
        st.subheader("Dataset Cleaning")

        st.write(df.head())
        st.write(df.describe())

            # Show descriptive statistics
        st.subheader("Dataset Statistics")
        st.write(df.describe())

        # Show column Data types
        st.subheader("Data Types")
        st.write(get_dtypes(df))

        # Show missing values count
        st.subheader("Missing values")
        missing_values = get_misssing_values(df)
        st.write(missing_values)

        total_missing = missing_values.sum()
        st.write(f"Total Missing Values: {total_missing}")


        # Data Cleaning by removing missing values
        st.header("Data Cleaning")

        if st.button("Remove Missing Values"):
            df = df.dropna()

            st.success("Missing values removed successfully!")
        st.write(df.head())

        rows, cols = df.shape

        st.write(f"Updated Shape: {rows} rows x {cols} columns")

        if st.checkbox("Drop Missing Values"):
            df = df.dropna()

            st.success("Missing values removed.")

        if st.checkbox("Fill Numeric Missing Values with Mean"):
            numeric_col = df.select_dtypes(include="number").columns

            for col in numeric_col:
                df[col] = df[col].fillna(
                    df[col].mean()
                )
            st.success("Numeric missing values filled.")

        if st.button("Remove Duplicates"):
            df = df.drop_duplicates()

            st.success("Duplicate rows removed!")
            st.write(df.head())


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

    elif page == "Visualization":
        st.subheader("Histogram")
        # Histogram visualization

        numeric_columns=df.select_dtypes(
            include=['int64', 'float64']
        ).columns

        if len(numeric_columns) == 0:
            st.warning("No numeric columns found for analysis.")
            st.stop()
        st.subheader("Histogram")
        st.subheader("Column Explorer")

        numeric_columns = df.select_dtypes(include="number").columns

        selected_column = st.selectbox(
            "Select Numeric Column",
            numeric_columns
        )
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
        


    elif page == "AI Insights":
        st.subheader("AI Insights")
        st.subheader("Column Explorer")

        numeric_columns = df.select_dtypes(include="number").columns

        selected_column = st.selectbox(
            "Select Numeric Column",
            numeric_columns
        )

        insights = generate_insights(df, selected_column)

        for insight in insights:
            st.write(insight)

            st.subheader("AI Generated Summary")

            summary = generate_summary(df, selected_column)

            st.write(summary)


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
            if not ai_question.strip():

                st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner("Analyzing dataset..."):

                response = ask_gemini(
                    df,
                    ai_question
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
            st.subheader("AI Recommendations")

            recommendations = generate_recommendations(df)

            for recommendation in recommendations:
                st.info(recommendation)

    st.markdown("---")
    st.caption("Build using Python, Streamlit, Pandas, and Gemini API")