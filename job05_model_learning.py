import numpy as np
import tensorflow
import matplotlib.pyplot as plt
from tensorflow.keras.models import *
from tensorflow.keras.layers import *

#####
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow
#####

# X_train, X_test, Y_train, Y_test = np.load(
#     './crawling_data/news_data_max_21_wordsize_13243.npy', allow_pickle=True)
# print(X_train.shape, Y_train.shape)
# print(X_test.shape, Y_test.shape)
#
#
# model = Sequential()
# model.add(Embedding(13243, 300, input_length=21))
# model.add(Conv1D(32, kernel_size=5, padding='same', activation='relu'))
# model.add(MaxPooling1D(pool_size=1))
# model.add(LSTM(128, activation='tanh', return_sequences=True))
# model.add(Dropout(0.3))
# model.add(LSTM(64, activation='tanh', return_sequences=True))
# model.add(Dropout(0.3))
# model.add(LSTM(64, activation='tanh'))
# model.add(Dropout(0.3))
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dense(6, activation='softmax'))
# model.summary()
#
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit_hist = model.fit(X_train, Y_train, batch_size=128, epochs=10, validation_data=(X_test, Y_test))
# model.save('./models/news_category_classification_model_{}.h5'.format(fit_hist.history['val_accuracy'][-1]))
# plt.plot(fit_hist.history['val_accuracy'], label='validation accuracy')
# plt.plot(fit_hist.history['accuracy'], label='accuracy')
# plt.legend()
# plt.show()







X_train, X_test, Y_train, Y_test = np.load(
    './crawling_data/crawl001/ArtcsE33NR1Conc1_max_899_wordsize_8727.npy', allow_pickle=True)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)


model = Sequential()
model.add(Embedding(8727, 300, input_length=899))
model.add(Conv1D(32, kernel_size=5, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=1))
model.add(LSTM(128, activation='tanh', return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(64, activation='tanh', return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(64, activation='tanh'))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.summary()


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
fit_hist = model.fit(X_train, Y_train, batch_size=128, epochs=10, validation_data=(X_test, Y_test))
model.save('./models/ArtcsE33NR1_{}.h5'.format(fit_hist.history['val_accuracy'][-1]))
plt.plot(fit_hist.history['val_accuracy'], label='validation accuracy')
plt.plot(fit_hist.history['accuracy'], label='accuracy')
plt.legend()
plt.show()
