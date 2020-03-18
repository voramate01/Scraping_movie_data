# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:33:59 2019

@author: VoramatePasharawipas
"""
import pandas as pd
import urllib.request
import os 

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
df = pd.read_csv("joblo_poster.csv")
df.columns
links=df.Poster   

# Function to take an image url and save the image in the given directory
def download_image(url,image_number):
    print("[INFO] downloading {}".format(url))
    name = str(url.split('/')[-1])
    name = f"Pic_{image_number}"+name #File name that will be saved
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url,os.path.join(dir_path, name))
    
# Print the number of images
print ("[INFO] Downloading {} images".format(len(links)))
#Download ALL image in URL links list
j=1 
for i in links:
    print (j)
    download_image(i,j)
    j+=1