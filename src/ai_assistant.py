import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_gemini(df, question):

    sample_data = df.head(5).to_string()

    prompt = f"""
You are an expert data analyst.

Dataset Sample:

{sample_data}

User Question:

{question}

Provide a clear business-focused answer.
"""
    
    model = genai.GenerativeModel(
    "gemini-2.5-flash"
    )

    response = model.generate_content(
        prompt
    )

    return response.text