import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
op = Options()
op.add_argument("--headless")
prefs = {
    'translate_whitelists': {'ur': 'en'},
    'translate': {'enabled': 'true'}
}
op.add_experimental_option('prefs', prefs)
user_name = input('Enter twitter email/username:')
password = input('Enter twitter password:')
link_to_tweet = input('Enter link of the Tweet:')
driver = webdriver.Chrome(options=op)
driver.get('https://twitter.com/login')
time.sleep(5)
driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(user_name)
driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(password)
time.sleep(5)
driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(
    Keys.RETURN)
time.sleep(5)
driver.get(link_to_tweet)
time.sleep(7)
# If your internet connection is slow , set the SCROLL_PAUSE_TIME variable to 7 or 8 or anything you want
SCROLL_PAUSE_TIME = 5
last_height = driver.execute_script("return document.body.scrollHeight")
result = []
while True:
    try:
        wait = WebDriverWait(driver, 10)
        for reply in wait.until(ec.visibility_of_any_elements_located((By.XPATH, "//div[contains(@class, 'css-18t94o4') and contains(@class, 'css-1dbjc4n') and contains(@class, 'r-16y2uox') and contains(@class, 'r-19u6a5r') and contains(@class, 'r-1ny4l3l') and contains(@class, 'r-m2pi6t') and contains(@class, 'r-oyd9sg') and contains(@class, 'r-o7ynqc') and contains(@class, 'r-6416eg')]"))):
            reply.click()
    except selenium.common.exceptions.TimeoutException:
        pass
    except selenium.common.exceptions.WebDriverException:
        pass
    driver.implicitly_wait(5)
    time.sleep(5)
    comments = driver.find_elements_by_xpath(
        "//div[contains(@class, 'css-901oao') and contains(@class, 'r-18jsvk2') and contains(@class, 'r-1qd0xha') and contains(@class, 'r-a023e6') and contains(@class, 'r-16dba41') and contains(@class, 'r-rjixqe') and contains(@class, 'r-bcqeeo') and contains(@class, 'r-bnwqim') and contains(@class, 'r-qvutc0')]")

    for comment in comments:
        try:
            comm = comment.find_element_by_css_selector('span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0').text
            if comm not in result:
                result.append(comm)
        except selenium.common.exceptions.NoSuchElementException as error:
            result.append('')
    driver.implicitly_wait(5)
    time.sleep(3)    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    time.sleep(7)

# Enter the desired file path instead of '/home/hassamrajpoot/Desktop/result.csv'
with open('/home/hassamrajpoot/Desktop/result.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(0, len(result)):
        writer.writerow([i, result[i]])
    file.close()
driver.quit()
print('Success!')
