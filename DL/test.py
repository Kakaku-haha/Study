from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import openpyxl as op
import random
from selenium_stealth import stealth

from selenium.webdriver import Chrome
import pyautogui

driver = Chrome()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})


def BigImg():
    btn = driver.find_elements(By.XPATH,"//*[@class='card-feed']/div[2]/div[3]/div/ul/li[1]")
    for i in btn:
        i.click()
def PicDownLoad(url,path):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Cookies": "SINAGLOBAL=2489191138537.923.1715332300235; SCF=An94DzJdfhS1Sy3G4jlQDpAkHRfLv0j4XH9XH-lwdHwrcnoje0RQ-YQlHKPByvjxJWlzLEai4XnRsdISW0jNGpQ.; UOR=www.google.com,open.weibo.com,cn.bing.com; ALF=1719969811; SUB=_2A25LWWtDDeRhGeFH6VIZ9CbFzTyIHXVoF-KLrDV8PUJbkNAbLUrZkW1Ne6m8MXo3kAZzPKCtGSajhOO5l1E6fy-F; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhZn1_auFGSCIDQsh5ZmqpB5JpX5KMhUgL.FoM4eo5RShn4So52dJLoI7Uuqg_feh5f; XSRF-TOKEN=zzfympsSbM_I5CG4rRIKYfne; _s_tentry=-; Apache=6629412370911.438.1717745952620; ULV=1717745952693:9:3:3:6629412370911.438.1717745952620:1717491279760; PC_TOKEN=d6f82afbe8; WBPSESS=Rq93_CvEn-lUdoAy1RJUUT4YV4CO_ssIKevfbqIfMRFiNsyGQVgV1jOBuJ6D6nQ_ejaIjjENG8Vt0LcqAreUSPS9iEPXQMbxw4V4to9cNbnB12YoTRpiBXR1U3Xxc46yoXMIKGZszYWen366NbvZTA==",
        "Referer": "https://weibo.com/"
    }

    response  = requests.get(url,headers=headers)
    with open(path,'wb') as f:
        f.write(response.content)


def clickDownLoad():
    time.sleep(2)
    pyautogui.click(500,500,button = 'right')
    time.sleep(2)
    pyautogui.typewrite(['v'])
    time.sleep(3)
    pyautogui.typewrite("hello world!")
    pyautogui.typewrite(['enter'])
    pyautogui.click(518,27,button='left')
    
""" driver.get("https://passport.weibo.com/sso/signin?entry=miniblog&source=miniblog")  # 打开微博登录界面
time.sleep(4) """
driver.implicitly_wait(10)
print("success")

url = "https://s.weibo.com/weibo?q=%E9%95%BF%E6%B2%99%E9%A3%8E%E6%A0%BC&scope=ori&haspic=1&Refer=g"
driver.get(url)
time.sleep(4)

#BigImg()
book = op.load_workbook()
sheet = book.active
Xpath = "//*[@class='main-full']/div/div[@class='card-wrap']"
card = driver.find_elements(By.XPATH,Xpath)#所有推文卡
p = 1
for j in card:
    print(j.text)

    j.find_element(By.XPATH,".//*[@class='content']/div[3]/div/ul/li").click() #查看第一张大图
    pics = j.find_elements(By.XPATH,".//*[@class='choose-pic']/ul/li")
 
    for i in pics:
        i.click()
        time.sleep(random.randint(1,4))
        j.find_element(By.XPATH,".//*[@class='tab']/li[2]/a").click()#查看大图
        clickDownLoad()
        #url = pic.get_attribute("href")
        #sheet.cell(p,1,value=url)
        #print(url)
        #PicDownLoad(url,"C:/Users/20783/Desktop/test{}.jpg".format(p))
        p += 1
    #book.save("C:/Users/ZH/Desktop/test.xlsx")
    time.sleep(3)
    time.sleep(random.randint(1,3))
    j.find_element(By.XPATH,"//*[@class='tab']/li/a").click() #收起
    time.sleep(random.randint(1,3))
    