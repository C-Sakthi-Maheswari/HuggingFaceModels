from diffusers import StableDiffusionPipeline
import torch

# Choose model
model_id = "dreamlike-art/dreamlike-diffusion-1.0"

# Load pipeline
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, use_safetensors=False)

# Move model to available device
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

# Get user input
prompt = input("Enter your prompt: ")

# Generate image
image = pipe(prompt).images[0]

# Display & Save the image
image.show()
image.save("generated_image.png")
print("Image saved as generated_image.png")
