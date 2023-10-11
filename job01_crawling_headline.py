from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

category = ['Politics','Economic','Social','Culture','World','Science']

df_titles = pd.DataFrame()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60'}

for i in range(len(category)):
    url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}'.format(i)
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    title_tags=soup.select('.sh_text_headline')

    titles = []
    for title_tag in title_tags:
        titles.append(title_tag.text)

    df_section_titles = pd.DataFrame(titles, columns=['title'])
    df_section_titles['category'] = category[i]
    df_titles = pd.concat([df_titles, df_section_titles], axis='rows', ignore_index=True)

print(df_titles)
df_titles.to_csv('./crawling_data/naver_headline_news_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d')), index=False)