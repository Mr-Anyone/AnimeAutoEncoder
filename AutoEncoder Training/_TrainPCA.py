from joblib import dump
from sklearn.decomposition import PCA
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np

def lol():
    pass

train_path = os.path.join(os.curdir, "Train")
train_data = tf.keras.preprocessing.image_dataset_from_directory(train_path, image_size=(64, 64), shuffle=True, color_mode='rgb', batch_size=1)

pca = PCA(n_components=0.99)
X = []
count = 0
for item in train_data.take(20000):
    X.append(item[0].numpy().reshape((64*64*3))/255)
    count += 1

ae = keras.models.load_model('Best Model.h5', custom_objects={"rounded_accuracy" : lol})
encoder = ae.layers[0]

X = encoder.predict(np.array(X))
print("Start Training")
pca.fit(np.array(X))
dump(pca, 'Trained .joblib')