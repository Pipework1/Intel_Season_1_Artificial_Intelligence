import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle

# pd.set_option('display.unicode.east_asian_width', True)
# df = pd.read_csv('./crawling_data/naver_news_titles_20231012.csv')
# print(df.head())
# df.info()
#
# X = df['titles']
# Y = df['category']
#
# encoder = LabelEncoder()
# labeled_y = encoder.fit_transform(Y)
# # print(labeled_y[:3])
# label = encoder.classes_
# # print(label)
#
# with open('./models/encoder.pickle', 'wb') as f:
#     pickle.dump(encoder, f)
#
# onehot_y = to_categorical(labeled_y)
# # print(onehot_y)
#
# okt = Okt()
# for i in range(len(X)):
#     X[i] = okt.morphs(X[i], stem=True)
# print(X)
#
# stopwords = pd.read_csv('./stopwords.csv', index_col=0)
# for j in range(len(X)):
#     words = []
#     for i in range(len(X[j])):
#         if len(X[j][i]) > 1:
#             if X[j][i] not in list(stopwords['stopword']):
#                 words.append(X[j][i])
#     X[j] = ' '.join(words)
# print(X[0])
#
#
# token = Tokenizer()
# token.fit_on_texts(X)
# tokened_x = token.texts_to_sequences(X)
# wordsize = len(token.word_index) + 1
# print(tokened_x[0:3])
# print(wordsize)
#
# with open('./models/news_token.pickle', 'wb') as f:
#     pickle.dump(token, f)
#
# max = 0
# for i in range(len(tokened_x)):
#     if max < len(tokened_x[i]):
#         max = len(tokened_x[i])
# print(max)
#
# x_pad = pad_sequences(tokened_x, max)
# print(x_pad[:3])
#
# X_train, X_test, Y_train, Y_test = train_test_split(
#     x_pad, onehot_y, test_size=0.2)
# print(X_train.shape, Y_train.shape)
# print(X_test.shape, Y_test.shape)
#
# xy = X_train, X_test, Y_train, Y_test
# np.save('./crawling_data/news_data_max_{}_wordsize_{}'.format(max, wordsize), xy)



pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_csv('./crawling_data/crawl001/ArtcsE33NR1Conc1.csv')
print(df.head())
df.info()

X = df['Patent Summary']
Y = df['Result']

encoder = LabelEncoder()
labeled_y = encoder.fit_transform(Y)
# print(labeled_y[:3])
label = encoder.classes_
# print(label)

with open('./models/encoder_KPD_1.pickle', 'wb') as f:
    pickle.dump(encoder, f)

onehot_y = to_categorical(labeled_y)
# print(onehot_y)

okt = Okt()
for i in range(len(X)):
    X[i] = okt.morphs(X[i], stem=True)
print(X)

stopwords = pd.read_csv('./stopwords.csv', index_col=0)
for j in range(len(X)):
    words = []
    for i in range(len(X[j])):
        if len(X[j][i]) > 1:
            if X[j][i] not in list(stopwords['stopword']):
                words.append(X[j][i])
    X[j] = ' '.join(words)
print(X[0])


token = Tokenizer()
token.fit_on_texts(X)
tokened_x = token.texts_to_sequences(X)
wordsize = len(token.word_index) + 1
print(tokened_x[0:3])
print(wordsize)

with open('./models/KPD_Prd_token.pickle', 'wb') as f:
    pickle.dump(token, f)

max = 0
for i in range(len(tokened_x)):
    if max < len(tokened_x[i]):
        max = len(tokened_x[i])
print(max)

x_pad = pad_sequences(tokened_x, max)
print(x_pad[:3])

X_train, X_test, Y_train, Y_test = train_test_split(
    x_pad, onehot_y, test_size=0.2)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

xy = X_train, X_test, Y_train, Y_test
np.save('./crawling_data/crawl001/ArtcsE33NR1Conc1_max_{}_wordsize_{}'.format(max, wordsize), xy)