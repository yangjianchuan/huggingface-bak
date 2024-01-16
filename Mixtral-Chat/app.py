from huggingface_hub import InferenceClient
import gradio as gr

client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")

def format_prompt(message, history):
  prompt = "<s>"
  for user_prompt, bot_response in history:
    prompt += f"[INST] {user_prompt} [/INST]"
    prompt += f" {bot_response}</s> "
  prompt += f"[INST] {message} [/INST]"
  return prompt

def generate(
    prompt, history, temperature=0.2, max_new_tokens=4096, top_p=0.95, repetition_penalty=1.0,
):
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=42,
    )

    formatted_prompt = format_prompt(prompt, history)

    stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    output = ""

    for response in stream:
        output += response.token.text
        yield output
    return output

    
mychatbot = gr.Chatbot(
    avatar_images=["./user.png", "./botm.png"], bubble_full_width=False, show_label=False, show_copy_button=True, likeable=True,)

demo = gr.ChatInterface(fn=generate, 
                        chatbot=mychatbot,
                        title="Tomoniai's Mixtral 8x7b Chat",
                        retry_btn=None,
                        undo_btn=None
                       )

demo.queue().launch(show_api=False)