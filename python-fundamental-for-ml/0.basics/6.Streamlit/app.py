import os

import streamlit as st
from dotenv import load_dotenv
from google import genai


load_dotenv()

st.title("Gemini + Streamlit")

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY is missing. Add it to your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Give me an idea of Gemini API in 1000 words",
)

st.markdown(response.text)