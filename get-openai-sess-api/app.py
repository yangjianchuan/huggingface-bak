import gradio as gr
import requests
import time
import json

def print_log(msg):
    print("[%s]%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))

def make_post_request(api_endpoint, endpoint_path, payload):
    url = f"{api_endpoint}{endpoint_path}"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    try:
        response = requests.post(url, headers=headers, data=payload)
        return response
    except Exception as e:
        print_log(str(e))
        return None

def getapikey(url, username, password):
    if not url or not username or not password:
        return "URL, username, and password are required."
    api_endpoint = f"{url}"
    payload = f"username={username}&password={password}&prompt=login"
    response = make_post_request(api_endpoint, "/api/auth/platform/login", payload)
    return json.loads(response.text)["login_info"]["user"]["session"]["sensitive_id"]

def get_refresh_token(url, username, password):
    if not url or not username or not password:
        return "URL, username, and password are required."
    api_endpoint = f"{url}"
    payload = f"username={username}&password={password}"
    response = make_post_request(api_endpoint, "/api/auth/login2", payload)
    return json.loads(response.text)["refresh_token"]

with gr.Blocks() as iface:
    gr.Markdown("## Get OpenAI API sess Key")
    gr.Markdown("For example, if the address for your pandora-next is `https://dongsiqie-pdrn1.hf.space` and the value of your proxy_api_prefix attribute is aa12345678, then the URL below should be filled in as `https://dongsiqie-pdrn1.hf.space/aa12345678`")
    url_input = gr.Textbox(label="url", value="", placeholder="youUrl/proxy_api_prefix")
    username_input = gr.Textbox(label="username")
    password_input = gr.Textbox(type='password', label="password")    
    get_api_key_button = gr.Button("Get Sess Key")
    get_refresh_token_button = gr.Button("Get Refresh Token")
    response_output = gr.Markdown(label="Response")
    gr.Markdown("You can check the remaining quota for sess-api on this website: https://dongsiqie-openai-credit-grants.hf.space")
    get_api_key_button.click(getapikey, inputs=[url_input, username_input, password_input], outputs=response_output)
    get_refresh_token_button.click(get_refresh_token, inputs=[url_input, username_input, password_input], outputs=response_output)

iface.launch()
