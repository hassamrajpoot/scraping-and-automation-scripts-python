#24rackomet
from bs4 import BeautifulSoup
import requests
import json
import sys
base_url = 'https://24rakomet.mk/category/вести'
url_toJoin = 'https://24rakomet.mk/'
raw_data = requests.get(base_url)
NEWS = []
raw_data = BeautifulSoup(raw_data.content, 'html.parser')
try:
    news_boxes = raw_data.find('div', id='1537349799943-b38429f0-6ced').find_all('div', class_='td-block-span12')
except:
    print('data container(s) not found or page source not downloaded correctly!')
    print('Something went wrong , Check your internet connection maybe!')
    print('Quiting ........!')
    sys.exit(0)
for newsbox in news_boxes:
    try:
        details = newsbox.find('div', class_='td-module-thumb').find('a')['href']
        img_link = newsbox.find('div', class_='td-module-thumb').find('a').find('img')['src']
        caption = newsbox.find('div', class_='td-module-thumb').find('a')['title'].strip()
        news = {'news_heading':caption, 'image_link':img_link, 'date_published':'', 'description':'', 'details':details}
        NEWS.append(news)
    except:
        pass
with open('website2_news.json', 'w') as file:
    json.dump(NEWS, file)
    file.close()