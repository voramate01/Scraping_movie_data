# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:28:02 2019

@author: VoramatePasharawipas
"""

import requests
from bs4 import BeautifulSoup
import csv

# Create a file to write to, add headers row
f = csv.writer(open('Boxofficemojo_news.csv', 'w', newline='' , encoding="utf-8"))
f.writerow(['Date','Article','Content'])


pages = []
for i in range(1, 56):
    url = 'https://www.boxofficemojo.com/news/?view=&page=' + str(i) + '&p=.htm'
    pages.append(url)
    
for item in pages:
    page = requests.get(item)
    # Create a BeautifulSoup object 
    soup = BeautifulSoup(page.text, 'html.parser')
    last_links = soup.find("td", attrs={"colspan": "3"})
    last_links=last_links.find_all('tr')
    
    number_of_article = len(last_links)
    
    for i in range(1,number_of_article):
            
            Date= last_links[i].find_all("td")[0].string
            
            Article =str(last_links[i].find_all("td")[1].string)
            
            insidelink = last_links[i].find_all("td")[1].a.get('href')
            insidelink = 'https://www.boxofficemojo.com'+insidelink 
            pageinside = requests.get(insidelink)
            soupinside = BeautifulSoup(pageinside.text, 'html.parser')
            soupinside = soupinside.find_all("p", attrs={"align":"justify"})
            soupinside = BeautifulSoup(str(soupinside[0:-1]),'lxml').get_text(" ",strip=True).replace(" , ", " ").replace("[ " , "").replace(" ]" , "")
                    
            print(Date)  
            f.writerow([Date,Article,soupinside])
            
del f





