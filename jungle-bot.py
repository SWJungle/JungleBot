from re import split
import requests
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

page = requests

def main() :
    print('check your request..')
    ## webhook url
    webhook_url = "WEBHOOK-URL"
    moonjicam_url = "https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=icc"
    text = "Jungle Bot Text."
    title, breakfast, lunch, dinner = get_umsik(moonjicam_url)    
    breakfast = " ".join(breakfast)
    lunch = " ".join(lunch)
    dinner = " ".join(dinner)
    print(type(breakfast), type(lunch), type(dinner))
    payload = {
        # "text": title + " (<%s|Click here.>)\n " % moonjicam_url + breakfast + "\n" + lunch + "\n" + dinner  ,
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🍚" + title,
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "오늘의 식단이에요. 개선 사항이 있으면 말씀해주세요 😁<*"+ moonjicam_url +"|this is a link> | <https://sunio00000.github.io/contact|contact me>*"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "plain_text",
                        "text": breakfast,
                        "emoji": True
                    },
                    {
                        "type": "plain_text",
                        "text": lunch,
                        "emoji": True
                    },
                    {
                        "type": "plain_text",
                        "text": dinner,
                        "emoji": True
                    },
                ]
            },
        ]
    }
    
    requests.post(webhook_url, json=payload)
    print('ok. your request sended.')

#scraping   
def get_umsik(url : str):
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.select_one('#tab_item_1 > h3').text
    td_first = soup.select('#tab_item_1 > table > tbody > tr > td:nth-child(1)')[0]
    td_second = soup.select('#tab_item_1 > table > tbody > tr > td:nth-child(2)')[0]
    td_third = soup.select('#tab_item_1 > table > tbody > tr > td:nth-child(3)')[0]
    return (title, td_first.text.split(), td_second.text.split(), td_third.text.split())

#! this script using main function.
if __name__ == "__main__" :
    main()
    
