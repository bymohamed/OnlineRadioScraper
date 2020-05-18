import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import sqlite3

connection = sqlite3.connect('radio_imgs.db')
cursor = connection.cursor()

#cursor.execute('CREATE TABLE radio_imgs (id INTEGER PRIMARY KEY, name TEXT, img TEXT)')

url = 'https://www.tunisie-radio.com/'
page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")

i=1
for link in soup.find_all('img', {"typeof": "foaf:Image" , "width": 90}):
    cursor.execute('INSERT INTO radio_imgs VALUES (?, ?, ?)', (i, link.attrs['title'], link.attrs['src']) )
    i=i+1

connection.commit()
