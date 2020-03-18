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


##################################################################################
#Download fromm the links we scraped previously
import pandas as pd
import urllib.request
import os 
import shutil


####Download from rottentomato csv file#####
#Define the name of directory 
f_name = "NOTHING/Rottentomato"

# Create the directory name where the images will be saved
base_dir = os.getcwd()
dir_name = (f_name.split('/')[-1]).split('.')[0]
dir_name
dir_path = os.path.join(base_dir, dir_name)

#Create the directory if already not there
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

# Read the csv with links to all the image pages
os.getcwd()
df = pd.read_csv("CSV_File\Rottentomato_rating.csv")
df.columns
links=df.Image

# Function to take an image url and save the image in the given directory
def download_image(url,image_number):
    print("[INFO] downloading {}".format(url))
    name = f"Pic_{image_number}.jpg" #File name that will be saved
    opener=urllib.request.build_opener()#Add header and chage user-agent name so we don't get forbidden by the website
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url,os.path.join(dir_path, name))
    #shutil.copyfileobj(url, name)  #(Doesnt work)
    #os.system("wget -O {0} {1}".format(name, url)) #Send command line order(Doesnt work)
    
    
# Print the number of images
print ("[INFO] Downloading {} images".format(len(links)))
#Download ALL image in URL links list
j=1 
for i in links:
    print (j)
    download_image(i,j)
    j+=1
###############################################################################    
 
####Download from joblo csv file#####
#Define the name of directory 
f_name = "NOTHING/joblo_poster"

# Create the directory name where the images will be saved
base_dir = os.getcwd()
dir_name = (f_name.split('/')[-1]).split('.')[0]
dir_name
dir_path = os.path.join(base_dir, dir_name)

#Create the directory if already not there
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

# Read the csv with links to all the image pages
os.getcwd()
df = pd.read_csv("CSV_File\joblo_poster.csv")
df.columns
links=df.Poster   

# Function to take an image url and save the image in the given directory
def download_image(url,image_number):
    print("[INFO] downloading {}".format(url))
    name = str(url.split('/')[-1])
    name = f"Pic_{image_number}"+name #File name that will be saved
    opener=urllib.request.build_opener()#Add header and chage user-agent name so we don't get forbidden by the website
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url,os.path.join(dir_path, name))
    #shutil.copyfileobj(url, name)  #(Doesnt work)
    #os.system("wget -O {0} {1}".format(name, url)) #Send command line order(Doesnt work)
    
    
# Print the number of images
print ("[INFO] Downloading {} images".format(len(links)))
#Download ALL image in URL links list
j=1 
for i in links:
    print (j)
    download_image(i,j)
    j+=1


links[0]
download_image(links[0])
