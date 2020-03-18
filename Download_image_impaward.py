# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:24:07 2019

@author: VoramatePasharawipas
"""

import pandas as pd
import urllib.request
import os 


#Define the name of directory 
f_name = "Impawards_updated"

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
df = pd.read_csv("impawards_updated.csv")
df.columns
links=df.Links

# Function to take an image url and save the image in the given directory
def download_image(url,image_number):
    print("[INFO] downloading {}".format(url))
    name = f"Pic_{image_number}.jpg" #File name that will be saved
    try:
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url,os.path.join(dir_path, name))
    except Exception as error:
        print ("[~] Error Occured with %s : %s" % (name, error))
        
        
# Print the number of images
print ("[INFO] Downloading {} images".format(len(links)))
#Download ALL image in URL links list
j=7343 
for i in links[7342:]:
    print (j)
    download_image(i,j)
    j+=1
    
