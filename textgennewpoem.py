from transformers import pipeline

# Load the text generation pipeline with a poetry-friendly model
poetry_generator = pipeline("text-generation", model="gpt2")

# Ask user for a poem prompt
prompt = input("Enter a theme or starting line for your poem: ")

# Generate the poem
poem = poetry_generator(prompt, max_length=100, num_return_sequences=1)

# Print the poem
print("\nGenerated Poem:\n")
print(poem[0]["generated_text"])
