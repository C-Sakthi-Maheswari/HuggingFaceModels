from transformers import pipeline

# Load the text generation pipeline
story_generator = pipeline("text-generation", model="gpt2")

# Ask user for a story idea
prompt = input("Enter a story idea or opening line: ")

# Generate the story
story = story_generator(prompt, max_length=200, num_return_sequences=1)

# Print the generated story
print("\nGenerated Story:\n")
print(story[0]["generated_text"])
