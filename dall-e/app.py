import requests
import gradio as gr

def generate_image(prompt, quality, size, style, api_key, request_url):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "prompt": prompt,
        "model": "dall-e-3",
        "quality": quality,
        "size": size,
        "style": style,
        "num_images": 1,
    }
    response = requests.post(request_url, headers=headers, json=data)
    response_json = response.json()
    
    # Get the URL of the first generated image
    image_url = response_json["data"][0]["url"]
    
    return image_url

# Create the interface using Gradio
with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# <center> OpenAI dall-e-3 API with Gradio </center>")
        gr.Markdown("This demo uses the OpenAI dall-e-3 API to generate an image from text. You get a free session key from https://dongsiqie.me/sess")
    with gr.Row():
        api_key_input = gr.Textbox(label="API Key", type="password")
        request_url_input = gr.Textbox(label="Request URL", value="https://api.openai.com/v1/images/generations")
        quality_input = gr.Dropdown(label="Quality", choices=["standard", "hd"], value="standard")
        size_input = gr.Dropdown(label="Size", choices=["1792x1024", "1024x1024", "1024x1792"], value="1024x1024")
        style_input = gr.Dropdown(label="Style", choices=["vivid", "natural"], value="vivid")
    with gr.Row():
        prompt_input = gr.Textbox(label="Image Description", value="A cute cat.")
    submit_btn = gr.Button("Generate Image", variant='primary')
    image_output = gr.Image(label="Generated Image")
    
    submit_btn.click(fn=generate_image, inputs=[prompt_input, quality_input, size_input, style_input, api_key_input, request_url_input], outputs=image_output)

demo.launch()
