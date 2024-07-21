import selenium
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

options = webdriver.ChromeOptions()

prefs = {
    'profile.default_content_setting_values':{
        'notifications':2
    }
}
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(options=options)
#driver.get("https://passport.weibo.com/sso/signin?entry=wapsso&source=wapsso&url=https%3A%2F%2Fm.weibo.cn%2Fdetail%2F5054926065763963")
#time.sleep(5)

url = "https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E9%95%BF%E6%B2%99%E6%9A%B4%E9%9B%A8"
driver.get(url)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div/ul/li[7]/span").click()
time.sleep(3)
CardWrap = driver.find_elements(By.CLASS_NAME,'card-wrap')
""" 
for card in CardWrap:
    print(card.text) """

width,height=pyautogui.size()
def ClickDownLoad():
    pyautogui.click(500,500,button='right')
    time.sleep(2)
    pyautogui.typewrite(['v'])
    time.sleep(3)
    pyautogui.typewrite(['enter'])
    time.sleep(4)
    
    

def closePic():
    pyautogui.click(width/2-50,190,button='left')

def NextRight():
    pyautogui.click(width/2-50,590,button='left')

def getPicNum():
    lis = driver.find_elements(By.XPATH,"//li")
    i=0
    for j in lis:
        i+=1 
    print(i)
    return i

def PicDownloader(num):
    i = 1
    while i<num:
        ClickDownLoad()
        NextRight()
        i +=1
    pyautogui.click(640,240,button='left')
    pyautogui.click(640,240,button='left')
    time.sleep(20)
    ClickDownLoad()
    closePic()

driver.find_element(By.CLASS_NAME,'weibo-text').click()
time.sleep(5)
ImgBox = driver.find_element(By.XPATH,"//*[@class ='m-auto-list']/li")
ImgBox.click()
time.sleep(3)
iteNum = getPicNum()
PicDownloader(iteNum)
#url = ImgBox.get_attribute("src")
time.sleep(3)
driver.find_element(By.CLASS_NAME,'nav-left').click()   


