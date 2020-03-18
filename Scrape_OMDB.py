# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:15:40 2019

@author: VoramatePasharawipas
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import json

#Get list of imdn id 
df = pd.read_csv("title.rating.tsv",sep='\t')
df.head()
df.shape
df.tconst[df.tconst=="tt1000000"].index  #422398
df.iloc[422398,]
df.tconst[422398:422398+2000]


list_imdbid=df.tconst[422398:422398+2000]
type(list_imdbid)

#Craete link for OMDB API Using imdb id
list_imdbid='http://www.omdbapi.com/?i='+list_imdbid+'&apikey=3e46a856'
list_imdbid
list_imdbid=list(list_imdbid)
len(list_imdbid)

list_imdbid[0][26:35]

# Create a file to write to, add headers row
f = csv.writer(open('OMDB_api.csv', 'w', newline='' , encoding="utf-8"))
f.writerow(['IMDB_ID','Info_json_form'])

for item in list_imdbid:
    page = requests.get(item)
    # Create a BeautifulSoup object 
    soup = BeautifulSoup(page.text, 'html.parser')
    soup=str(soup) #Change to string
    json_soup = json.loads(soup) #Change to JSON
    IMDB_ID=item[26:35] # TO get id 
    
    print(IMDB_ID)  
    f.writerow([IMDB_ID,json_soup])
    
del f
    



    
