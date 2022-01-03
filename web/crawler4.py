from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='c:\\multicampus\\workspace\\chromedriver.exe')
browser = webdriver.Chrome(service=service)

url = 'http://itempage3.auction.co.kr/DetailView.aspx?itemno=C220859288'
