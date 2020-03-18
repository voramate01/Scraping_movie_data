# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:13:59 2019

@author: VoramatePasharawipas
"""


import requests
from bs4 import BeautifulSoup
import csv
#from time import sleep

# Create a file to write to, add headers row
f = csv.writer(open('impawards.csv', 'a', newline='')) # 'a' to append not overwrite the original file ,,  newline='' to write row without blank row betweeb each row
f.writerow(['Designer', 'Number_of_poster',"Links","Poster_name","Year"])
 

page = requests.get('http://www.impawards.com/designers/index.html')
# Create a BeautifulSoup object 
soup = BeautifulSoup(page.text, 'html.parser')
last_links = soup.find_all("div", attrs={"class":"col-md-4"}, limit=3)
number = len(last_links)
number
    
for i in range(0,number):
            
        Designersss= last_links[i].ul.find_all("li")
        for j in range(0,len(Designersss)):
            #Designer name
            Designer = Designersss[j].find("b").string
            #Poster
            link_to_poster = Designersss[j].a.get("href")
            link_to_poster = "http://www.impawards.com/designers/"+link_to_poster
            newpage = requests.get(link_to_poster) #Go into the link
            newsoup = BeautifulSoup(newpage.text, 'html.parser')
            new_last_links= newsoup.find("center").find_next_sibling("center")
            Postersss=new_last_links.find_all("a")
            #Number of poster of each designer
            Designersss[j].b.decompose()
            Number_of_poster = Designersss[j].get_text()
            #Poster (continue)
            for k in range(0,len(Postersss)):
                
                #Get poster link URL
                Poster=Postersss[k].get("href")
                if Poster[0:5]=='/intl':
                    inter=Poster.split("/")
                    MyPoster="http://www.impawards.com"+"/"+inter[1]+"/"+inter[2]+"/"+inter[3]+"/posters/"+inter[4][:-4]+"jpg"
                    Poster_name = inter[4][:-5]
                    Year = inter[3]
                    
                elif Poster[0:3]=="/tv" : 
                    inter=Poster.split("/")
                    MyPoster="http://www.impawards.com"+"/"+inter[1]+"/posters/"+inter[2][:-4]+"jpg"
                    Poster_name = Poster[4:-5]
                    Year = "na"
                else:
                    MyPoster="http://www.impawards.com"+Poster[0:5]+"/posters"+Poster[5:-4]+"jpg"
                    Poster_name = Poster[6:-5]
                    Year = Poster[1:5]
                
                print(Designer)
                print(MyPoster)
                f.writerow([Designer,Number_of_poster, MyPoster, Poster_name, Year])
           
del f
