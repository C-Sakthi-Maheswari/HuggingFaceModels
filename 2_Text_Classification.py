import streamlit as st
import requests

# Hugging Face API Key (Replace with your own)
API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
HEADERS = {"Authorization": "Bearer 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"}


def classify_text(text):
    """Send text to Hugging Face API for classification."""
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()  # API response with classification results
    else:
        return f"Error: {response.status_code}, {response.json()}"


# Streamlit UI
st.title("Text Classification")

user_input = st.text_area("Enter text for classification", "I love this product!")

if st.button("Classify Text"):
    result = classify_text(user_input)

    if isinstance(result, list):  # Successful response
        label = result[0][0]['label']
        confidence = result[0][0]['score']
        st.write(f"**Prediction:** {label} (Confidence: {confidence:.2f})")
    else:
        st.error(result)  # Show error if API fails
