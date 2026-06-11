# AI-Powered Data Analyst Assistant

An interactive Streamlit-based application that helps users analyze CSV datasets, generate visualizations, derive insights, and obtain AI-powered explanations using Google's Gemini API.

## Features Implemented (Day 1 - Day 10)

### Day 1: CSV File Upload
- Upload CSV datasets through the Streamlit interface.
- Load datasets using Pandas.

### Day 2: Dataset Profiling
- Display dataset preview.
- Show dataset shape (rows and columns).
- Display data types.
- Identify missing values.
- Generate descriptive statistics.

### Day 3: Dynamic Column Selection
- Automatically detect numeric columns.
- Allow users to select columns dynamically for analysis.
- Works with different CSV datasets without hardcoding column names.

### Day 4: Data Visualization
- Generate histograms for selected numeric columns.
- Generate boxplots for outlier analysis.
- Display correlation heatmaps.

### Day 5: AI-Based Insights
- Generate basic analytical insights from selected columns.
- Provide statistical summaries.

### Day 6: Business Recommendations
- Offer rule-based recommendations based on dataset characteristics.
- Suggest actions using generated insights.

### Day 7: Report Generation
- Create text-based analysis reports.
- Include insights and summaries in the generated report.

### Day 8: Report Download
- Allow users to download analysis reports as text files.
- Export reports directly from the Streamlit application.

### Day 9: Project Documentation
- Improved GitHub repository structure.
- Added project descriptions and resume-ready content.

### Day 10: Enhanced AI Interaction
- Enable users to ask questions about uploaded datasets.
- Generate AI-powered responses using Gemini API.
- Provide business-focused answers based on dataset samples.

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Google Gemini API
- python-dotenv
- Git & GitHub

---

## Project Structure

```
AI-Data-Analyst-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── src/
    ├── data_loader.py
    ├── profiler.py
    ├── visualizer.py
    ├── recommendations.py
    ├── report_generator.py
    └── ai_assistant.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Data-Analyst-Assistant.git
cd AI-Data-Analyst-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## Skills Demonstrated

- Data Analysis
- Exploratory Data Analysis (EDA)
- Data Visualization
- Prompt Engineering
- Generative AI Integration
- Streamlit Application Development
- Python Programming
- Git Version Control
- Problem Solving
- Report Generation

---

## Future Enhancements

- Data cleaning utilities
- Advanced dashboard metrics
- Dataset filtering options
- Export cleaned datasets
- Streamlit Cloud deployment
- Improved UI/UX

---

## Author

**Deepika**

B.Tech Student | Aspiring Data Analyst
