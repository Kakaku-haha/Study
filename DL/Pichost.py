import requests

def upload(path):
    header ={
         "Authorization": "nAbnwIVKgRd7NosIVWeJe8Elv7nH3xKT"
    }
    files = {
        'smfile':open(path,'rb')
    }
    url="https://sm.ms/api/v2/upload"

    response = requests.post(url,files=files,headers=header).json()
    if response['success']:
        print(response['data']['url'])
        return response['data']['url']
    else:
        print("Something Wrong!")
#res = upload("C:/Users/ZH/Downloads/V2P/中国经营报.mp4300.jpg")
#print(res)