import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"  

headers = {"Authorization": "Bearer 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"}

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load the BLIP model and processor
model_name = "Salesforce/blip-image-captioning-base"
processor = BlipProcessor.from_pretrained(model_name)
model = BlipForConditionalGeneration.from_pretrained(model_name)

# Ask user for image file path
image_path = input("Enter the path of the image: ")

# Open and process the image
image = Image.open(image_path).convert("RGB")
inputs = processor(image, return_tensors="pt")

# Generate caption
output = model.generate(**inputs)
caption = processor.decode(output[0], skip_special_tokens=True)

# Print the caption
print("Generated Caption:", caption)
