import requests
import re


StruLoc= "北京市海淀区新街口外大街19号"
str = input()
def LocationSearcher(str):
    
    url = "https://restapi.amap.com/v3/geocode/geo?" + "key=4330dc363ad84fb3f9b56c7013d2dafd&address="
    response = requests.get(url+str)
    data=response.json()
    print(data)
    location = data['geocodes'][0]['location']
    return(location)

def search(str):
    api = "https://restapi.amap.com/v3/place/text?key=4330dc363ad84fb3f9b56c7013d2dafd&keywords="
    response = requests.get(api+str)
    
    #findLocation = re.compile(r'(.*)\{\}(.*)'.format(str))  
    for address in response.json()['pois']:
        if re.search(str,address['name']):
            print(address['name'])
#coordinate = LocationSearcher(StruLoc).split(',')
coordinate = LocationSearcher(str).split(',')
search(str)
print("经度："+coordinate[0])
print("纬度："+coordinate[1])