#supersport
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
from bs4 import BeautifulSoup
import time
import sys
import requests
import json
base_url = 'https://supersport.mk/'
driver.get(base_url)
time.sleep(10)
raw_data = driver.page_source
NEWS = []
raw_data = BeautifulSoup(raw_data, 'html.parser')
try:
    news_boxes = raw_data.find('div', id='tdi_31').find_all('div', class_='td_module_16')
except:
    print('data container not found or page source not downloaded correctly!')
    print('Something went wrong , Check your internet connection maybe!')
    print('Quiting ........!')
    sys.exit(0)
for newsbox in news_boxes:
    try:
        details = newsbox.find('div', class_='td-module-thumb').find('a')['href']
        img_link = newsbox.find('div', class_='td-module-thumb').find('img')['src']
        caption =  newsbox.find('div', class_='item-details').find('h3').find('a')['title']
        date_published = newsbox.find('div', class_='item-details').find('span', class_='td-post-date').text.strip()
        news = {'news_heading':caption, 'image_link':img_link, 'date_published':date_published, 'description':'', 'details':details}
        NEWS.append(news)
    except:
        pass
with open('website3_news.json', 'w') as file:
    json.dump(NEWS, file)
    file.close()