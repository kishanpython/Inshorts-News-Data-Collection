# -*- coding: utf-8 -*-
"""
Created on THU Oct 1 10:26:20 2020

@author: Kishan-Win10
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import time
from datetime import date

today = date.today()
startTime = time.time()

# News Types
seed_urls = ['https://inshorts.com/en/read/technology',
             'https://inshorts.com/en/read/sports',
             'https://inshorts.com/en/read/world',
             'https://inshorts.com/en/read/politics',
             'https://inshorts.com/en/read/entertainment',
             'https://inshorts.com/en/read/automobile',
             'https://inshorts.com/en/read/science',
             'https://inshorts.com/en/read/world']


news_data = []

# Collecting data
for url in seed_urls:
    news_category = url.split('/')[-1]
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    news_articles = [{'news_headline': headline.find('span', 
                                                        attrs={"itemprop": "headline"}).string,
                        'news_article': article.find('div', 
                                                    attrs={"itemprop": "articleBody"}).string,
                        'news_category': news_category}
                        
                        for headline, article in 
                            zip(soup.find_all('div', 
                                            class_=["news-card-title news-right-box"]),
                                soup.find_all('div', 
                                            class_=["news-card-content news-right-box"]))
                    ]
    news_data.extend(news_articles)

# Creating dataframe     
df =  pd.DataFrame(news_data)
df = df[['news_headline', 'news_article', 'news_category']] 

# To save the file
d2 = today.strftime("%B %d, %Y")
s = d2.split(',')[0]
a = s[0:3]
b = s[-2:]
file_save = 'output/' + 'inshort' + '_' + b + '_' + a + '_' + str(int(startTime)) + '.csv' 
df.to_csv(file_save)
print('file_save')
