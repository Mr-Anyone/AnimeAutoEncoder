import os
from tkinter import *

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from tensorflow import keras

FILENAME = "Show.png"

sliders = []
mins = []
maxs = []
k = []

row = 1
col = 1
col_count = 5
run = False

def lol():
    pass
config_dir = os.path.join(os.curdir, "Config")

autoencoder = keras.models.load_model(os.path.join(config_dir, "Best Model.h5"), custom_objects={"rounded_accuracy":lol})
decoder = autoencoder.layers[1]


def init():
    global mins, maxs
    with open(os.path.join(config_dir, "Max.txt"), "r") as max:
        with open(os.path.join(config_dir, "Min.txt"), "r") as min:

            for lin in max.readlines():
                maxs.append(float(lin))

            for lin in min.readlines():
                mins.append(float(lin))


def show_img():
    global FILENAME, sliders
    img = []
    for index in range(len(sliders)):
        img.append(sliders[index].get()/10 * (maxs[index] - mins[index]))

    img = np.array([img])
    img = decoder.predict(img).reshape((64, 64, 3))


    plt.imshow(img)
    plt.show()


class SliderWindows:
    def __init__(self, master):
        global row, col
        self.master = master
        self.windows = []
        self.app = 0

        if col_count % 2 == 0:
            self.button = Button(master, text='Show Image', command=show_img).grid(row=0,
                                                                                   column=int(col_count / 2))
        else:
            self.button = Button(master, text='Show Image', command=show_img).grid(row=0,
                                                                                   column=int(col_count / 2) + 1)

        for x in range(100):
            w = Scale(master, from_=0, to=10, length=None, orient=HORIZONTAL)
            w.grid(row=row, column=col)
            sliders.append(w)

            if col == col_count:
                col = 0
                row += 1
            col += 1


def main():
    root = Tk()
    root.title("GUI")
    init()

    app = SliderWindows(root)

    root.mainloop()


main()
