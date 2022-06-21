from bs4 import BeautifulSoup as bs
import requests

link = "https://scrapethissite.com/pages/forms/"
raw_data = requests.get(link)
data = bs(raw_data.content, "html.parser")
teams = data.find_all("tr", class_="team")
with open('result.txt', 'w') as file: #File name to write data to
    for team in teams:
        info = team.find_all("td")
        lista = ["=> Team :", "-> Year :", "-> Wins :", "-> Losses :", "-> OT Losses :", "-> Win Percentage :", "-> Goals for :", "-> Goals against :", "-> + / - :"]
        listb = []
        for inf in info:
            text1 = inf.text.strip()
            text2 = text1.replace("\n", "")
            listb.append(text2)
        for i in range(0, 9):
            file.write('\n{}  {}'.format(lista[i] , listb[i]))
        file.write('\n')
        file.write('*' * 50)
