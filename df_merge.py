import pandas as pd
import glob
import datetime

df = pd.read_csv('D:\Workspace_Python_1\Workspace_PyCharm_1\Intel_Season_1_Artificial_Intelligence\crawling_data/naver_news_titles_20231012.csv', index_col=0)
print(df.head())
# df.to_csv('./test/df_csv.csv')
