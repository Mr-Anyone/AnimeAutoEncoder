import os

import tensorflow as tf
import tensorflow.keras as keras

train_path = os.path.join(os.curdir, "Train")
train_data = tf.keras.preprocessing.image_dataset_from_directory(train_path, image_size=(64, 64), shuffle=True,
                                                                 color_mode='rgb', batch_size=1)

valid_path = os.path.join(os.curdir, "Validation")
valid_data = tf.keras.preprocessing.image_dataset_from_directory(valid_path, image_size=(64, 64), shuffle=True,
                                                                 color_mode='rgb', batch_size=1)


def rounded_accuracy(y_true, y_pred):
    return keras.metrics.binary_accuracy(tf.round(y_true), tf.round(y_pred))


def change(x, y):
    return (tf.reshape(x, [64, 64, 3]) / 255, tf.reshape(x, [64, 64, 3]) / 255)


train_data = train_data.map(change)
train_data = train_data.batch(64)

valid_data = valid_data.map(change)
valid_data = valid_data.batch(64)

encoder = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[64, 64, 3]),
    keras.layers.Dense(3000, activation="selu"),
    keras.layers.Dense(1000, activation="selu"),
    keras.layers.Dense(500, activation="selu"),
    keras.layers.Dense(100, activation="selu")
])

decoder = keras.models.Sequential([
    keras.layers.Dense(100, input_shape=[100]),
    keras.layers.Dense(500, activation="selu"),
    keras.layers.Dense(1000, activation="selu"),
    keras.layers.Dense(3000, activation="selu"),
    keras.layers.Dense(64 * 64 * 3, activation="selu"),
    keras.layers.Reshape((64, 64, 3))
])

ae = keras.models.Sequential([encoder, decoder])
ae.compile(loss='mse', metrics=[rounded_accuracy], )

best_model = keras.callbacks.ModelCheckpoint(f"Best Model.h5", save_best_only=True)
Epochs = 1200

history = ae.fit(train_data, epochs=Epochs, validation_data=valid_data, callbacks=[best_model])
