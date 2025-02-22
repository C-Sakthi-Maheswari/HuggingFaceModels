from transformers import pipeline

# Load pre-trained text classification model
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Get user input
text = input("Enter your text for classification: ")

# Perform classification
result = classifier(text)[0]

# Display output
print(f"Label: {result['label']} (Confidence: {result['score']:.4f})")
