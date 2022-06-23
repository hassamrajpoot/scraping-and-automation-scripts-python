from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import concurrent.futures 
import urllib.parse
options = Options()
options.headless = True
class AmzaonScraper:
    @staticmethod  
    def Scrape_items(url, pages=1):
        if len(url) > 1:
            raise ValueError('One url allowed only, You might wanna use "Scrape_different_category_items" function for multiple urls!')
        elif len(url) == 0:
            raise ValueError('No url provided, One url required!')
        urls = []
        if pages > 1:
            urls.append(url[0])
            driver = webdriver.Chrome(options=options)
            driver.get(url[0])
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='a-section a-text-center s-pagination-container']")))
            except:
                pass
            pages_links = []
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.quit()
            base_link = soup.find('span', class_=['s-pagination-strip']).find('a', class_=['s-pagination-item', 's-pagination-button'])['href']
            for i in range(2, pages+1):
                pages_links.append(urllib.parse.urljoin('https://amazon.com', base_link.strip().replace(base_link[-1], '{}'.format(i))))
            for page_link in pages_links:
                urls.append(page_link)
        elif pages == 1:
            urls = url
        for link in urls:
            driver = webdriver.Chrome(options=options)
            driver.get(link)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20']")))
            except:
                pass
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.quit()
            items = soup.find_all('div', class_=['sg-col-4-of-12', 's-result-item', 's-asin', 'sg-col-4-of-16', 'sg-col', 's-widget-spacing-small', 'sg-col-4-of-20'])
            with open('Products_details.txt', 'a') as file:
                for item in items:
                    try:
                        details_link = urllib.parse.urljoin('https://amazon.com' , item.find('a', class_=['a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])['href'])
                        description = item.find('a', class_=['a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']).find('span').text
                        file.write(description)
                        file.write("\n" + details_link)
                        file.write("\n" + '*'*50 + "\n")
                    except:
                        pass
    @staticmethod
    def Scrape_item_details(urls):
        if len(urls) == 0:
            raise ValueError('No urls provided, Atleast one url required!')
        for url in urls:
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@id='ppd']")))
            except:
                pass
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.quit()
            with open('item_details.txt', 'a') as file:
                try:
                    name = soup.find('span', id='productTitle').text.strip()
                    file.write(name + '\n')
                except:
                    file.write('Product name not found!' + '\n')
                try:
                    price = soup.find('div', id='corePrice_desktop').find('span', class_='a-offscreen').text.strip()
                    file.write(price + '\n')
                except:
                    file.write('Product price not found!' + '\n')
                try:
                    details_container = soup.find('div', id='productOverview_feature_div')
                    for info in details_container.find_all('tr'):
                        file.write(info.text.strip() + '\n')
                    for info in soup.find('div', id='feature-bullets').find_all('span', class_='a-list-item'):
                        file.write(info.text.strip() + '\n')
                except:
                    file.write('Product details not found!' + '\n')
                file.write('*'*50)
                file.write('\n')
    @staticmethod
    def Scrape_different_category_items(urls, pages=1):
        if pages > 1:
            new_urls = []
            global pages_links_extractor
            def pages_links_extractor(url):
                urls = [url]
                driver = webdriver.Chrome(options=options)
                driver.get(url)
                try:
                    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='a-section a-text-center s-pagination-container']")))
                except:
                    pass
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                driver.quit()
                base_link = soup.find('span', class_=['s-pagination-strip']).find('a', class_=['s-pagination-item', 's-pagination-button'])['href']
                for i in range(2, pages+1):
                    urls.append(urllib.parse.urljoin('https://amazon.com', base_link.strip().replace(base_link[-1], '{}'.format(i))))
                return urls
            links = []
            with concurrent.futures.ProcessPoolExecutor() as executer:
                links = executer.map(pages_links_extractor, urls)
            for url in links:
                for link in url:
                    new_urls.append(link)
            urls = new_urls
        elif pages == 1:
            urls = urls
        for link in urls:
            driver = webdriver.Chrome(options=options)
            driver.get(link)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20']")))
            except:
               pass
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.quit()
            items = soup.find_all('div', class_=['sg-col-4-of-12', 's-result-item', 's-asin', 'sg-col-4-of-16', 'sg-col', 's-widget-spacing-small', 'sg-col-4-of-20'])
            with open('Different_category_items_details.txt', 'a') as file:
                for item in items:
                    try:
                        details_link = urllib.parse.urljoin('https://amazon.com' , item.find('a', class_=['a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])['href'])
                        description = item.find('a', class_=['a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']).find('span').text
                        file.write(description)
                        file.write("\n" + details_link)
                        file.write("\n" + '*'*50 + "\n")
                    except:
                        pass

