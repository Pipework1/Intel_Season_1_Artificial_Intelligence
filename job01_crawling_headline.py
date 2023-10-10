from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

category = ['Politics','Economic','Social','Culture','World','Science']

df_titles = pd.DataFrame()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'}

for i in range(len(category)):
    url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}'.format(i)
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    title_tags=soup.select('.sh_text_headline')

