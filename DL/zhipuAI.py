from zhipuai import ZhipuAI
import requests
import openpyxl
client = ZhipuAI(api_key="b5b3ad5c546069c3a8c956abd98eb386.Ls3qMOr7qQXyXNDO") # 请填写您自己的APIKey
import Pichost
def GLM4V(string,url):
  response = client.chat.completions.create(
      model="glm-4v",  # 填写需要调用的模型名称
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": string
            },
            {
              "type": "image_url",
              "image_url": {
                  "url" : url
              }
            }
          ]
        }
      ]
  )
  return(response.choices[0].message.content)
def Agent(string,url):
  response = client.chat.completions.create(
      model="669493a1337a1b0f0656af2d",  # 填写需要调用的模型名称
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": string
            },
            {
              "type": "image_url",
              "image_url": {
                  "url" : url
              }
            }
          ]
        }
      ]
  )
  return(response.choices[0].message.content)
def GLM(string):
  response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
      messages=[
          {"role": "user", "content":string},
      ],
      stream=True,
      )
  str = ''
  for chunk in response:
      str = str+chunk.choices[0].delta.content
  print(str)

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
        print(fi.status_code)

url =Pichost.upload("C:/Users/ZH/Downloads/V2P/STV新闻透视1150.jpg")
#url ="https://s2.loli.net/2024/07/19/aFYezs6Qkf2hXC1.jpg"
HasFlood="判断图片是否含有洪水暴雨等因素，回答简洁，只返回是或否，只返回是或否，只返回是或否，只返回是或否，只返回是或否，只返回是或否，只返回是或否，只返回是或否"
FloodDepth = "判断图片中洪水的深度，回答简洁，只回答洪水深度，只回答洪水深度，只回答洪水深度，只回答洪水深度，只回答洪水深度，只回答洪水深度，只回答洪水深度，只回答洪水深度"
SignRecognition ="识别图片中的招牌及各种字符，只返回识别的结果，只返回识别的结果，只返回识别的结果，只返回识别的结果，只返回识别的结果，只返回识别的结果，只返回识别的结果"
print(GLM4V(HasFlood,url))
print(GLM4V(FloodDepth,url))
print(GLM4V(SignRecognition,url))



""" 
book = openpyxl.load_workbook("C:/Users/ZH/Downloads/DL/工作簿1.xlsx")
sheet =book.active
for url in sheet['A']:
   if() """