# -*- coding: utf-8 -*-
"""Exercise_political_parties

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oCTTei6nDv5eHvUNRyhp0cvMtKYDirVT

# Steps in data pre-processinng


1.   Missing value Imputation
2.   Outliers treatment
3.   Dummy value creation
4.   X-y split
5.   Test-train data split
6.   Standardization of Data
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import io

feature_names =  ['party','handicapped-infants', 'water-project-cost-sharing', 
                    'adoption-of-the-budget-resolution', 'physician-fee-freeze',
                    'el-salvador-aid', 'religious-groups-in-schools',
                    'anti-satellite-test-ban', 'aid-to-nicaraguan-contras',
                    'mx-missle', 'immigration', 'synfuels-corporation-cutback',
                    'education-spending', 'superfund-right-to-sue', 'crime',
                    'duty-free-exports', 'export-administration-act-south-africa']
df = pd.read_csv(io.StringIO(uploaded['house-votes-84.data.txt'].decode('utf-8')),na_values=['?'],names=feature_names)

df.head()

df.info()

df.dropna(inplace=True)

df.info()

df.head()

df.replace(('y','n'),(1,0),inplace=True)
df.replace(('democrat','republican'),(1,0),inplace=True)
df.head()

X = df.loc[:,df.columns!='party']
y = df.loc[:,df.columns=='party']
X.info()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state = 0)

"""# Architecture of Network"""

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras.optimizers import Adam,RMSprop

model = Sequential()
model.add(Dense(32,activation='relu',input_dim=16))
model.add(Dropout(0.5))
model.add(Dense(16,activation='relu',input_dim=16))
model.add(Dropout(0.2))
model.add(Dense(1,activation='sigmoid'))

model.summary()

"""# Compilation and Training"""

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

history = model.fit(X_train,y_train,epochs=100,verbose = 0,batch_size=10,validation_data=(X_test,y_test))

score = model.evaluate(X_test,y_test,verbose = 2)
print("Loss: %.2f"%(score[0]*100))
print("Accuracy: %.2f"%(score[1]*100))
print("Training loss: %.2f"%(history.history['loss'][9]*100))
print("Validation loss: %.2f"%(history.history['val_loss'][9]*100))

"""# Evaluation"""

import matplotlib.pyplot as plt

plt.style.use('dark_background')

loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1,len(loss)+1)
plt.title("Training and Validation loss")
plt.plot(epochs,loss,'y',label='Training Loss')
plt.plot(epochs,val_loss,'r',label='Validation Loss')
plt.legend()
plt.show()

acc = history.history['acc']
val_acc = history.history['val_acc']
epochs = range(1,len(loss)+1)
plt.title("Training and Validation Accuracy")
plt.plot(epochs,acc,'y',label='Training Accuracy')
plt.plot(epochs,val_acc,'r',label='Validation Accuracy')
plt.legend()
plt.show()

