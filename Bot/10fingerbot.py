from selenium import webdriver
import time
from selenium.webdriver.common.by import By


browser = webdriver.Chrome("D:\\snapchat\\chromedriver.exe") #location of chromedriver.exe
url = "https://10fastfingers.com/typing-test/turkish"
browser.get(url)
browser.maximize_window()
time.sleep(2)

cookies_accept = browser.find_element(By.XPATH , "//*[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']").click()
time.sleep(2)

i = 0

while(i != 400):
    okunan = browser.find_element( By.CLASS_NAME, "highlight")
    answer = browser.find_element(By.XPATH , "//*[@id='inputfield']")  
    answer.send_keys(okunan.text + " ")
    i = i + 1 
    time.sleep(0.11)
