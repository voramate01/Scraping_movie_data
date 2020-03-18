# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 01:31:57 2019

@author: VoramatePasharawipas
"""

import requests
from bs4 import BeautifulSoup
import csv

# Create a file to write to, add headers row
f = csv.writer(open('joblo_poster.csv', 'w', newline=''))
f.writerow(['Title', 'Poster'])
 

page = requests.get('https://www.joblo.com/movie-posters/archives/ALL/')
# Create a BeautifulSoup object 
soup = BeautifulSoup(page.text, 'html.parser')
last_links = soup.find_all("li", attrs={"class":"vertical"})
number_of_poster = len(last_links)

    
for i in range(0,number_of_poster):
            
        Title= last_links[i].find("div",class_="bottom-poster").a.string
        Poster = last_links[i].div.a.img.get("src")
        Poster = 'https://www.joblo.com'+Poster
        
        print(i)
        f.writerow([Title,Poster])
            
del f


