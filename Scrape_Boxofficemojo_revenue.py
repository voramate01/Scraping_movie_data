# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:09:09 2019

@author: VoramatePasharawipas
"""

import requests
from bs4 import BeautifulSoup
import csv

# Create a file to write to, add headers row
f = csv.writer(open('Boxofficemojo_revenue.csv', 'w', newline=''))
f.writerow(['Rank', 'Title','Studio','Worldwide_revenue','Domestic_revenue'
            ,'Domestic_revenue_percent','Oversea_revenue','Oversea_revenue_percent'
            ,'Year'])


pages = []
for i in range(1, 9):
    url = 'https://www.boxofficemojo.com/alltime/world/?pagenum=' + str(i) + '.&p=.htm'
    pages.append(url)


    
for item in pages:
    page = requests.get(item)
    # Create a BeautifulSoup object 
    soup = BeautifulSoup(page.text, 'html.parser')
    last_links = soup.table.next_sibling.next_sibling.find_next('table')
    number_of_movie = len(last_links.find_all("tr"))
    
    for i in range(1,number_of_movie):
            
            Rank= last_links.find_all("tr")[i].find_all("td")[0].string
            Title =last_links.find_all("tr")[i].find_all("td")[1].string
            Studio = last_links.find_all("tr")[i].find_all("td")[2].string
            Worldwide_revenue = last_links.find_all("tr")[i].find_all("td")[3].string
            Domestic_revenue = last_links.find_all("tr")[i].find_all("td")[4].string
            Domestic_revenue_percent = last_links.find_all("tr")[i].find_all("td")[5].string
            Oversea_revenue = last_links.find_all("tr")[i].find_all("td")[6].string
            Oversea_revenue_percent = last_links.find_all("tr")[i].find_all("td")[7].string
            Year = last_links.find_all("tr")[i].find_all("td")[8].string[0:4]# [0:4] is to remove "^" on some rows
            
            print(Year)
        
            f.writerow([Rank, Title,Studio,Worldwide_revenue,Domestic_revenue,Domestic_revenue_percent
                        ,Oversea_revenue,Oversea_revenue_percent,Year])
            
del f

































