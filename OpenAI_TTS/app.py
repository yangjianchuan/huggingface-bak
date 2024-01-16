import gradio as gr
import os
import tempfile
from openai import OpenAI
import requests
import json

def create_header(api_key):
    return {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

def tts(text, model, voice, api_key,url,speed):
    if api_key == '':
        raise gr.Error('Please enter your OpenAI API Key')
    else:
        try:
            headers = create_header(api_key)
            url = url
            input_text = text
            query = {
            "model":model,
            "input":input_text,
            "voice":voice,
            "response_format":"mp3",
            "speed":speed,
                    }
            response = requests.post(url=url, data=json.dumps(query), headers=headers)
        except Exception as error:
            # Handle any exception that occurs
            raise gr.Error("An error occurred while generating speech. Please check your API key and try again.")
            print(str(error))

    # Create a temp file to save the audio
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        temp_file.write(response.content)

    # Get the file path of the temp file
    temp_file_path = temp_file.name

    return temp_file_path


with gr.Blocks() as demo:
    gr.Markdown("# <center> OpenAI Text-To-Speech API with Gradio </center>")
    gr.Markdown("This demo uses the OpenAI Text-To-Speech API to generate speech from text. You get free session key from https://dongsiqie.me/sess")
    with gr.Row(variant='panel'):
      api_key = gr.Textbox(type='password', label='OpenAI API Key', placeholder='Enter your API key to access the TTS demo')
      model = gr.Dropdown(choices=['tts-1','tts-1-hd'], label='Model', value='tts-1-hd')
      voice = gr.Dropdown(choices=['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'], label='Voice Options', value='nova')
      url = gr.Textbox(label="URL", placeholder="Enter your URL and then click on the 'Text-To-Speech' button, or simply press the Enter key.", value='https://api.openai.com/v1/audio/speech')
      #新增一个speed，数字滑块从0.25值4，默认是1
      speed = gr.Slider(label="Speed", minimum=0.25, maximum=4, step=0.25, value=1)   


    text = gr.Textbox(label="Input text", placeholder="Enter your text and then click on the 'Text-To-Speech' button, or simply press the Enter key.")
    btn = gr.Button("Text-To-Speech")
    output_audio = gr.Audio(label="Speech Output")
    
    text.submit(fn=tts, inputs=[text, model, voice, api_key,url,speed], outputs=output_audio, api_name="tts_enter_key", concurrency_limit=None)
    btn.click(fn=tts, inputs=[text, model, voice, api_key,url,speed], outputs=output_audio, api_name="tts_button", concurrency_limit=None)

demo.launch()