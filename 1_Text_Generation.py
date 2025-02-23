import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCpgM55OHHlX1mwtFD4DOlwYJw72n8G4mw")

def generate_text(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

st.title("Text Generation")

prompt = st.text_area("Enter your text prompt:")

if st.button("Generate"):
    if prompt:
        result = generate_text(prompt)
        st.write(result)
    else:
        st.warning("Please enter a prompt.")
