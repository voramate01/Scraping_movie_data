# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 03:14:47 2019

@author: VoramatePasharawipas
"""


from bs4 import BeautifulSoup
import csv
from selenium import webdriver

# Create a file to write to, add headers row
f = csv.writer(open('Rt_rating.csv', 'w', newline='' , encoding="utf-8"))
f.writerow(['Title','Metascore','Release_date', 'Image'])

####Use Selenium to open web browser
browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
url = "https://www.rottentomatoes.com/browse/cf-dvd-streaming-all/"
browser.get(url) #navigate to page 

#Get the script from the site
innerHTML = browser.execute_script("return document.body.innerHTML")
# execute script to scroll down the page
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")


#Beautiful Soup    
soup = BeautifulSoup(innerHTML, 'html.parser')
last_links = soup.find_all("div", attrs={"class":'mb-movie'})
number_of_movies = len(last_links)
number_of_movies

for i in range(0,number_of_movies):
    Image =last_links[i].div.a.img.get('src')
    Title =last_links[i].find("div", attrs={"class":"movie_info"}).h3.string
    Metascore =last_links[i].find("span",  class_="tMeterScore").get_text(" ", strip=True)
    Release_date = last_links[i].find("p",class_="release-date").get_text(" ")[11:]
    print(Release_date)  
    f.writerow([Title,Metascore,Release_date,Image])
del f

browser.close() # TO close selenium browser that we opened.




#headless driver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True #It does not actually open the driver ,so its faster.
browser = webdriver.Chrome(options=options) #Headless #Sometime Give different result than Normal brwoser with head
browser = webdriver.Chrome()# Head





