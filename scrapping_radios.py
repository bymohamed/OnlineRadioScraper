import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup
import sqlite3

connection = sqlite3.connect('radio_imgs.db')
cursor = connection.cursor()

f = open("stream_urls.txt","r").read().split()
print (f)
i=1
for h in f:
    cursor.execute('DELETE FROM radio_imgs WHERE COLNew = "//";')
    i=i+1


#cursor.execute('ALTER TABLE radio_imgs RENAME COLUMN COLNew TO stream_urls;')


#for link in soup.find_all('div', {"class": "field-content"}):
    #try:
        #if (x != str(link.findChild().attrs['href'])):
           # x = str(link.findChild().attrs['href'])
   # except:
       # pass
    #print ('https://www.tunisie-radio.com'+x)
    #cursor.execute('INSERT INTO radio_imgs VALUES (?, ?, ?)', (i, link.attrs['title'], link.attrs['src']) )
    #i=i+1

connection.commit()
