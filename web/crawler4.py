from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path="c:\\multicampus\\workspace\\chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)

url = 'https://www.naver.com'
browser.get( url )
