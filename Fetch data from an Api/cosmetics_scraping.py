from urllib.request import urlopen
import json
url = 'https://restaurant-api.wolt.com/v4/venues/5f562d24b0a912a096425c5d/menu'
response = urlopen(url)

json_data = json.loads(response.read())
with open('/home/hassamrajpoot/Desktop/cosmetics_scraping', 'w') as f:
    for item in json_data['items']:
        f.write("\nname: {}".format(item['name']))
        f.write("\ndescription: {}".format(item['description']))
        f.write("\nprice:{}\n".format(item['baseprice'] / 100))
        f.write("*" * 50)
f.close()

#https://wolt.com/he/isr/tel-aviv/venue/be-pharm-dizengoff?fbclid=IwAR1wlQ2hMqQVxGWeDv-SH5sv-9ofb7Lt9XMqwH8REAe3GmngsTDNbOUGbQU
#used json response of api request to get information of all the items!
