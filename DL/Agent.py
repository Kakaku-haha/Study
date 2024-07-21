import json
import requests

def get_access_token(api_key, api_secret):
    url = "https://chatglm.cn/chatglm/assistant-api/v1/get_token"
    data = {
       "api_key":api_key ,
       "api_secret": api_secret
    }
    response = requests.post(url, json=data)
    token_info = response.json()
    return token_info['result']['access_token']





""" def handle_response(data_dict):
    message = data_dict.get("message")
    if len(message) > 0:
        content = message.get("content")
        if len(content) > 0:
            response_type = content.get("type")
            if response_type == "text":
                text = content.get("text", "No text provided")
                return f"{text}"

            elif response_type == "image":
                images = content.get("image", [])
                image_urls = ", ".join(image.get("image_url") for image in images)
                return f"{image_urls}"

            elif response_type == "code":
                return f"{content.get('code')}"

            elif response_type == "execution_output":
                return f"{content.get('content')}"

            elif response_type == "system_error":
                return f"{content.get('content')}"

            elif response_type == "tool_calls":
                return f"{data_dict['tool_calls']}"

            elif response_type == "browser_result":
                content = json.loads(content.get("content", "{}"))
                return f"Browser Result - Title: {content.get('title')} URL: {content.get('url')}"


def send_message(assistant_id, access_token, prompt, file_list=None, conversation_id=None , meta_data=None):
    url = "https://chatglm.cn/chatglm/assistant-api/v1/stream"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "form-data/file_upload"
    }
    data = {
        "assistant_id": assistant_id,
        "prompt": prompt
        }


    if conversation_id:
        data["conversation_id"] = conversation_id
    if file_list:
        data["file_list"] = file_list        
    if meta_data:
        data["meta_data"] = meta_data

    with requests.post(url, json=data, headers=headers) as response:
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith('data:'):
                        data_dict = json.loads(decoded_line[5:])
                        output = handle_response(data_dict)
        else:
            return "Request failed", response.status_code
        print(output) """

def handle_response(data_dict):
    message = data_dict.get("message")
    if len(message) > 0:
        content = message.get("content")
        if len(content) > 0:
            response_type = content.get("type")
            if response_type == "text":
                text = content.get("text", "No text provided")
                return f"{text}"

            elif response_type == "image":
                images = content.get("image", [])
                image_urls = ", ".join(image.get("image_url") for image in images)
                return f"{image_urls}"

            elif response_type == "code":
                return f"{content.get('code')}"

            elif response_type == "execution_output":
                return f"{content.get('content')}"

            elif response_type == "system_error":
                return f"{content.get('content')}"

            elif response_type == "tool_calls":
                return f"{data_dict['tool_calls']}"

            elif response_type == "browser_result":
                content = json.loads(content.get("content", "{}"))
                return f"Browser Result - Title: {content.get('title')} URL: {content.get('url')}"


def send_message(assistant_id, access_token, prompt, conversation_id=None, file_list=None, meta_data=None):
    url = "https://chatglm.cn/chatglm/assistant-api/v1/stream"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "assistant_id": assistant_id,
        "prompt": prompt,
    }


    if conversation_id:
        data["conversation_id"] = conversation_id
    if file_list:
        data["file_list"] = file_list
    if meta_data:
        data["meta_data"] = meta_data

    with requests.post(url, json=data, headers=headers) as response:
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith('data:'):
                        data_dict = json.loads(decoded_line[5:])
                        output = handle_response(data_dict)


        else:
            return "Request failed", response.status_code
        print(output)

def Upload(filePath,access_token):
    url = "https://chatglm.cn/chatglm/assistant-api/v1/stream"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "form-data/file_upload"
    }
    files = {
    'file':open(filePath,'rb')
    }
    with requests.post(url,files=files,headers=headers) as fi:
        print(fi)

# Here you need to replace the API Key and API Secret with your，I provide a test key and secret here
api_key = "b32a00914cb7faf7" 
api_secret = "04e766d35327baada801bde3ca77f8e1" 
token = get_access_token(api_key, api_secret)
assistant_id = "669493a1337a1b0f0656af2d" 
access_token = token
prompt = "你是谁"

result = send_message(assistant_id, access_token,prompt)

Upload("C:/Users/ZH/Desktop/test.txt",access_token)