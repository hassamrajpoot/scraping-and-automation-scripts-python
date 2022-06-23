from bs4 import BeautifulSoup as bs
import requests

link = "https://pk1lib.org/s/python"
r = requests.get(link)
data = bs(r.content, "html.parser")
with open('books_details.txt', 'a') as file:
    for book in data.find_all("div", class_=["resItemBox", "resItemBoxBooks", "exactMatch"]):
        book_title = book.h3.a.text
        author = book.find("div", class_="authors")
        author_name = author.a.text
        text1 = "->book title : " + book_title
        file.write(text1 + '\n')
        text2 = "->Author : " + author_name
        file.write(text2 + '\n')
        link_to_next_page = book.h3.a["href"]
        next_page = "https://pk1lib.org{}".format(link_to_next_page)
        data_next_page = requests.get(next_page)
        some_data = bs(data_next_page.content, "html.parser")
        get_link = some_data.find("a", class_=["btn","btn-primary", "dlButton","addDownloadedBook"])
        link_to_download = get_link["href"]
        text3 = "->Download link : "
        text4 = 'https://pk1lib.org'+link_to_download
        file.write(text3 + text4 + '\n')
        file.write('*'*50 + '\n')
