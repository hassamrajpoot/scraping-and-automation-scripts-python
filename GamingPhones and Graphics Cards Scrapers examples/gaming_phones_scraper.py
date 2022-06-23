from bs4 import BeautifulSoup
import requests


class color:
    BOLD = '\033[1m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[36m'


r = requests.get("https://www.cect-shop.com/en/gaming-phones")
soup = BeautifulSoup(r.content, "html.parser")
all_phones = soup.find_all('div', class_='col-12 col-lg-6 col-xl-4 mb-2')
with open('phones.txt', 'w') as file:
    for phone in all_phones:
        phone_container = phone.find('h2', class_='product-title')
        phone_name = phone_container.a.text
        file.write("Product: {}".format(phone_name) + '\n')
        description_container = phone.find('div', class_='product-description mb-auto')
        phone_description_inner_container = description_container.a.ul
        file.write("Specifications :" + '\n')
        for desc in phone_description_inner_container.find_all('li'):
            file.write(". {}".format(desc.text)  + '\n')
        price_container = phone.find('div', class_='product-info d-flex align-items-end')
        price_inner_container = price_container.find('div', class_='product-price')
        file.write("Price : {}".format( price_inner_container.a.span.text.replace("from", "").strip()) + '\n')
        file.write("-"*50 + '\n')
