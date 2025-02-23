import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCpgM55OHHlX1mwtFD4DOlwYJw72n8G4mw")

def summarize_text(text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Summarize this: {text}")
    return response.text

st.title("Text Summarization")

text = st.text_area("Enter the text you want to summarize:")

if st.button("Summarize"):
    if text:
        summary = summarize_text(text)
        st.write(summary)
    else:
        st.warning("Please enter some text.")
