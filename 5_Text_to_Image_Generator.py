#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

import streamlit as st
import requests
import io
from PIL import Image

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
HEADERS = {"Authorization": f"Bearer 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"}

st.title("Free AI Image Generator")

# User input
prompt = st.text_input("Enter a prompt for image generation:", "A beautiful Indian woman")

if st.button("Generate Image"):
    with st.spinner("Generating... Please wait..."):
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})

        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content))

            # Resize Image to Fit Within 600px Height (Adjust as needed)
            max_height = 600
            aspect_ratio = image.width / image.height
            new_width = int(max_height * aspect_ratio)
            resized_image = image.resize((new_width, max_height))

            st.image(resized_image, use_column_width=True)  # Display Resized Image
        else:
            st.error("Failed to generate image. Try again with a different prompt.")
