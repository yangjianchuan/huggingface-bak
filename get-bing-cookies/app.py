import gradio as gr
import requests
import uuid
import json

# 函数执行API调用，并返回所需的结果
def call_api(url, cookies=None):
    url = f"{url}"  # 接口地址
    data = {"cookies": cookies if cookies else ''}  # post参数

    response = requests.post(url, json=data)  # 发送POST请求

    # 检查请求是否成功
    if response.status_code == 200:
        response_json = response.json()  # 将响应解析为JSON
        
        if cookies is None or 'KievRPSSecAuth' not in cookies:
            result_cookies = response_json["result"]["cookies"]
            result_cookies += ';KievRPSSecAuth=' + str(uuid.uuid4())
            return result_cookies  # 返回 Result.cookies 的值，包含 KievRPSSecAuth
        else:
            return response_json["result"]["cookies"]  # 返回 Result.cookies 的值
        
    else:
        return "请求失败，HTTP状态码：" + str(response.status_code)



with gr.Blocks() as iface:
    gr.Markdown("## 帮助你获取bing的cookie")
    gr.Markdown("帮助你过机器人验证，返回验证后的cookies")
    url_input = gr.Dropdown(choices=['https://dongsiqie-pass.hf.space','https://zklcdc-pass.hf.space'],label="请选择验证服务器",value="https://dongsiqie-pass.hf.space")
    cookies_input = gr.Textbox(label="你的cookies，可以不填",placeholder="在此处输入你的cookies，可以不填")    
    button = gr.Button("点击获取cookies")
    response_output = gr.Textbox(label="验证后的cookies")
    gr.Markdown("如果cookie中包含`cct`，说明验证成功。使用方法：在go-proxy-bingai项目中，点击右上角的齿轮，点【设置】，点击【完整 Cookie】，然后将验证后的cookies的cookies填写到【Cookies】中，然后刷新网页。")
    button.click(call_api, inputs=[url_input,cookies_input], outputs=response_output)
    
iface.launch()
