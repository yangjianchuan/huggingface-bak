import requests
import gradio as gr
from PIL import Image
from io import BytesIO

def generate_image(prompt, size):
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "prompt": prompt,
        "model": "dall-e-3",
        "size": size,
        "num_images": 1,
    }
    response = requests.post("https://sdcf.dongsiqie.me", headers=headers, json=data)

    # Get image content from the response
    image_content = BytesIO(response.content)
    image = Image.open(image_content)

    # Save image to a file or return it in a suitable format for your context.
    # For this example, I'm going to return the image directly.
    return image

# Create the interface using Gradio
with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# <center>stable-diffusion-xl-base-1.0</center>")
        gr.Markdown("This demo uses the stable-diffusion-xl-base-1.0 API to generate an image from text.")
    with gr.Row():
        size_input = gr.Dropdown(label="Size", choices=["1792x1024", "1024x1024", "1024x1792"], value="1024x1024")
    with gr.Row():
        prompt_input = gr.Textbox(label="Image Description", value="A futuristic cyberpunk-style puppy, neon-lit cityscape background, glowing eyes, mechanized body parts, dynamic pose, vibrant colors, nighttime vibe, sharp focus, digital art.")
    submit_btn = gr.Button("Generate Image", variant='primary')
    image_output = gr.Image(label="Generated Image")
   
    submit_btn.click(fn=generate_image, inputs=[prompt_input, size_input], outputs=image_output)

demo.launch()
