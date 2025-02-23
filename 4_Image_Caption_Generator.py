import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure API Key
genai.configure(api_key="AIzaSyCpgM55OHHlX1mwtFD4DOlwYJw72n8G4mw")

def generate_caption(image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(["Describe this image:", image])
    return response.text

st.title("Image Caption Generator")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Convert UploadedFile to PIL Image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        caption = generate_caption(image)  # Pass PIL Image, not UploadedFile
        st.write(f"**Caption:** {caption}")
