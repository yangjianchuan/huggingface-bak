import gradio as gr
import requests

def check_balance(api_key):
    try:
        assert api_key.startswith(('sk-', 'sess-')), "API Key must start with sk- or sess-"
        url = "https://api.openai.com/dashboard/billing/credit_grants"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        total_granted = data.get('total_granted', 0)
        total_used = data.get('total_used', 0)
        total_available = data.get('total_available', 0)

        return f"Total credit granted: {total_granted} units, total used: {total_used} units, total available: {total_available} units."

    except AssertionError as e:
        return str(e)
    except requests.RequestException as e:
        return f"An error occurred: {e}"

# 接口布局和样式
with gr.Blocks() as iface:
    gr.Markdown("## OpenAI API Key Balance Checker")
    gr.Markdown("Enter your OpenAI API key to check your credit balance. Your key should start with sk- or sess-.")
    gr.Markdown("Get your OpenAI API key: https://dongsiqie-get-openai-sess-api.hf.space")
    api_key_input = gr.Textbox(type='password', label="OpenAI API Key")    
    check_button = gr.Button("Check Balance")
    response_output = gr.Markdown(label="Response")
    check_button.click(check_balance, inputs=api_key_input, outputs=response_output)

iface.launch()
