# 24football
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import json
import sys
base_url = 'https://24fudbal.mk/'
raw_data = requests.get(base_url)
NEWS = []
raw_data = BeautifulSoup(raw_data.content, 'html.parser')
try:
    country_boxes = raw_data.find_all('div', class_='country-wrap')
except:
    print('data container(s) not found or page source not downloaded correctly!')
    print('Something went wrong , Check your internet connection maybe!')
    print('Quiting ........!')
    sys.exit(0)
for country_box in country_boxes:
    try:
        news_boxes = country_box.find_all('div', class_='col-sm-6')
        main_box = news_boxes[0]
        news_link = urljoin(base_url, main_box.find('a')['href'])
        image_link = urljoin(base_url , main_box.find('a').find('img')['src'])
        news_heading = main_box.find('h4').text.strip()
        date_published = main_box.find('p', class_='date-published').text.strip()
        description = main_box.find_all('p')[1].text.strip()
        main_box_news = {'news_heading':news_heading, 'image_link':image_link, 'date_published':date_published, 'description':description, 'details':news_link}
        NEWS.append(main_box_news)
        side_boxes = news_boxes[1].find_all('div', class_='right-article')
        for sidebox in side_boxes:
            news_link_sidebox = urljoin(base_url, sidebox.find_all('div', class_='col-xs-6')[0].find('a')['href'])
            image_link_sidebox = urljoin(base_url, sidebox.find_all('div', class_='col-xs-6')[0].find('a').find('img')['src'])
            date_published_sidebox = sidebox.find_all('div', class_='col-xs-6')[1].find('p', class_='date-published').text.strip()
            news_heading_sidebox = sidebox.find_all('div', class_='col-xs-6')[1].find_all('p')[1].text.strip()
            side_box_news = {'news_heading':news_heading_sidebox, 'image_link':image_link_sidebox, 'date_published':date_published_sidebox, 'description':' ', 'details':news_link_sidebox}
            NEWS.append(side_box_news)
    except:
        pass
with open('website1_news.json', 'w') as file:
    json.dump(NEWS, file)
    file.close()