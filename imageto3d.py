import torch
from diffusers import StableDiffusion3DPipeline
from PIL import Image

# Load the pre-trained model
model_id = "stabilityai/stable-diffusion-3d"
pipe = StableDiffusion3DPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Ask the user for an image input
image_path = input("Enter the path to your image file: ")

# Load and preprocess the image
image = Image.open(image_path).convert("RGB")

# Generate a 3D model
output_3d = pipe(image)

# Save the output model
output_file = "output_3d.glb"
output_3d.save(output_file)

print(f"3D model saved as {output_file}")


# from diffusers import DiffusionPipeline

# pipe = DiffusionPipeline.from_pretrained("TencentARC/InstantMesh")

# prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
# image = pipe(prompt).images[0]

# ALTERNATIVE:

# import torch
# from PIL import Image
# from shap_e.diffusion.sample import sample_latents
# from shap_e.models.download import load_model
# from shap_e.util.image_util import load_image
# from shap_e.util.notebooks import decode_latent_mesh
# import trimesh

# # Load the image-to-3D model
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model = load_model("image300M")  # Pre-trained image-to-3D model

# # Ask the user for an image input
# image_path = input("Enter the path to your image file: ")
# image = load_image(image_path)

# # Generate 3D latents
# latents = sample_latents(model, image, device=device)

# # Convert to 3D mesh
# mesh = decode_latent_mesh(latents[0])

# # Save the output model as .glb (GLTF format)
# output_file = "output_3d.glb"
# mesh.export(output_file)

# print(f"3D model saved as {output_file}")
