from re import split
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

page = requests

def main() :
    print('check your request..')
    ## webhook url
    webhook_url = "webhook-url"
    moonjicam_url = "https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=icc"
    text = "Jungle Bot Text."
    title, breakfast, lunch, dinner = get_umsik(moonjicam_url)    
    breakfast = " , ".join(breakfast)
    lunch = " , ".join(lunch)
    dinner = " , ".join(dinner)
    messages = ["정글 여러분 오늘도 ~행복한~ 코딩해요. 👨‍💻",
                "메리 크리스마스 Merry Christmas. ❄☃🌞",
                ]
    payload = {
        # "text": title + " (<%s|Click here.>)\n " % moonjicam_url + breakfast + "\n" + lunch + "\n" + dinner  ,
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🍜 " + title, 
                    "emoji": True
                }
            },
            {
			    "type": "divider"
		    },
            {
                "type": "section",
                "text": {
                    # {
                    #     "type": "mrkdwn",
                    #     "text": "*아침*\n" + breakfast +"\n\n*점심*\n" + lunch + "\n\n*저녁*\n" + dinner,
                    # },
                    "type": "mrkdwn",
                    "text": "*[ 아 침 ]*\n - " + breakfast +"\n\n*[ 점 심 ]*\n - " + lunch + "\n\n*[ 저 녁 ]*\n - " + dinner,
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://i.pinimg.com/236x/3f/08/7f/3f087fef430d0fc0c84a9984eec222d1.jpg",
                    "alt_text": "맛없어도 먹어야해!"
                }
            },
            {
			    "type": "divider"
		    },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": messages[0] + "  <"+ moonjicam_url +"|campus link > | <https://sunio00000.github.io/contact|contact me>"
                }
            },
        ]
    }
    
    requests.post(webhook_url, json=payload)
    print('ok. your request sended.')

#scraping   
def get_umsik(url : str):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # browser = webdriver.Chrome(ChromeDriverManager().install())
    # browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver.exe", options=options)
    browser = webdriver.Chrome(options=options)
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
    
