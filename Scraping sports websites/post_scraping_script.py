from mysql.connector import connect
import json
import sys
connection = connect(host='localhost', user='', password='')
cursor = connection.cursor()
try:
    f1 = open('website1_news.json')
except:
    print('scraped data for 24football(website1) not found')
    sys.exit(0)
data1 = json.load(f1)
try:
    f2 = open('website2_news.json')
except:
    print('scraped data for 24rackomet(website2) not found')
    sys.exit(0)
data2 = json.load(f2)
try:
    f3 = open('website3_news.json')
except:
    print('scraped data for supersport(website3) not found')
    sys.exit(0)
data3 = json.load(f3)
cursor.execute("CREATE DATABASE IF NOT EXISTS sports_news")
cursor.execute("USE sports_news")
cursor.execute("SHOW TABLES LIKE 'NEWS'")
table_exists = cursor.fetchone()
if not table_exists:
    mySql_Create_Table_Query = """CREATE TABLE NEWS ( 
                             id int(11) AUTO_INCREMENT,
                             news_heading TEXT ,
                             image_link TEXT,
                             date_published VARCHAR(100),
                             description TEXT,
                             details TEXT ,
                             PRIMARY KEY(id)) """
    cursor.execute(mySql_Create_Table_Query)
    connection.commit()
for news in data1:
    cursor.execute("""
                    INSERT IGNORE INTO NEWS (news_heading, image_link, date_published, description, details)
                    VALUES (%(news_heading)s, %(image_link)s, %(date_published)s, %(description)s, %(details)s)""", news)
connection.commit()
for news in data2:
    cursor.execute("""
                    INSERT IGNORE INTO NEWS (news_heading, image_link, date_published, description, details)
                    VALUES (%(news_heading)s, %(image_link)s, %(date_published)s, %(description)s, %(details)s)""", news)
connection.commit()
for news in data3:
    cursor.execute("""
                    INSERT IGNORE INTO NEWS (news_heading, image_link, date_published, description, details)
                    VALUES (%(news_heading)s, %(image_link)s, %(date_published)s, %(description)s, %(details)s)""", news)
connection.commit()
connection.close()