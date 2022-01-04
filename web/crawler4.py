from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="c:\\Users\\sykim\\multicampus\\workspace\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(service=service, options=options)

url = 'https://lc.multicampus.com/k-digital/#/login'
browser.get( url )

time.sleep(2) # 페이지가 로딩되는 시간을 위해 2초동안 대기
inputs = browser.find_elements(By.CSS_SELECTOR, 'div.input-row-line input')
loginButton = browser.find_element(By.CSS_SELECTOR, 'div.btn-row button.login-btn')

inputs[0].send_keys('여기가 아이디')
inputs[1].send_keys('여기가 패스워드')
loginButton.click()

# 무한 스크롤(작정하고 모든 내용을 전부 스크래핑)
# 초기 높이를 가져오고
last_height = browser.execute_script('return document.body.scrollHeight')
while True:
  # 스크롤을 아래로 내리고
  browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

  # 내용이 로딩되는 동안 잠시 기다려주고
  time.sleep(2)

  # 새로 높이를 재고
  new_height = browser.execute_script('return document.body.scrollHeight')

  # 높이가 이전과 같을 경우 더 이상 내려갈 수 없음
  if new_height == last_height: break

  # 기존의 높이를 새로운 높이로 변경
  last_height = new_height

# 로드된 내용들을 수집
articles = browser.find_elements(By.CSS_SELECTOR, 'div.feedlist span article')
for article in articles:
  for content in article.find_elements(By.CSS_SELECTOR, 'span.feedContentBlk span'):
    print( content.text )