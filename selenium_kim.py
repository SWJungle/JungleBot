import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=icc&stt_dt=2020-12-23")
time.sleep(3)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
td_first = soup.select('#tab_item_1 > table > tbody > tr > td:nth-child(1)')[0]
print(td_first.text.split())
td_second = soup.select('#tab_item_1 > table > tbody > tr > td:nth-child(2)')[0]
print(td_second.text.split())
td_third = soup.select('#tab_item_1 > table > tbody > tr > td:nth-child(3)')[0]
print(td_third.text.split())