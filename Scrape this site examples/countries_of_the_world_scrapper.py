from bs4 import BeautifulSoup as bs
import requests

link = "https://scrapethissite.com/pages/simple/"
raw_data = requests.get(link)
data = bs(raw_data.content, "html.parser")
names = data.find_all("div", class_="col-md-4 country")
with open('', w) as file:
    for name in names:
        country = name.h3.text
        country_info = name.find("div", class_="country-info")
        file.write("Country : " , country.strip(), end="")
        file.write(country_info.text)
        file.write('*' * 50)

#https://scrapethissite.com/pages/simple/
