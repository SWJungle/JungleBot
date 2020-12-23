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
    webhook_url = "https://hooks.slack.com/services/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"
    moonjicam_url = "https://dgucoop.dongguk.edu:44649/store/store.php?w=4&l=2&j=0"
    text = "Jungle Bot First Messsage."
    today = ""
    umsic_menu = ""
    
    payload = {
        # "text": get_umsik(moonjicam_url)[0] + " (<%s|Click here.>)\n " + get_umsik(moonjicam_url)[1]  % moonjicam_url
    }
    
    requests.post(webhook_url, json=payload)
    print('ok. your request sended.')

#scraping   
def get_umsik(moonjicam_url):
    ua = UserAgent()
    header = {'user-agent': ua.chrome}
    response = requests.get(moonjicam_url, verify=False)
    
    time.sleep(3)
    
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    
    td_first = soup.select('#tab_item_1 > table > tbody > tr > td:nth-child(1)')[0]
    print(td_first.text.split())
    td_second = soup.select('#tab_item_1 > table > tbody > tr > td:nth-child(2)')[0]
    print(td_second.text.split())
    td_third = soup.select('#tab_item_1 > table > tbody > tr > td:nth-child(3)')[0]
    print(td_third.text.split())

#! this script using main function.
if __name__ == "__main__" :
    main()
    
