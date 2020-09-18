import os
import shutil
from PIL import Image


def make_folder(path):
    try:
        os.makedirs(path)
    except Exception as e:
        print(f"Already A Folder in {path}, Error Message: {e}")


Save_Train = os.path.join(os.curdir, "Train", "Face")
Save_Validation = os.path.join(os.curdir, "Validation", "Face")
image_dir = os.path.join(os.curdir, "Original Image")

make_folder(Save_Train)
make_folder(Save_Validation)


def open_image(path):
    try:
        img = Image.open(path)
        if img.height > 64:
            return img.resize((64, 64))
        else:
            pass
    except Exception as e:
        print(f"UNKNOWN ERROR {path}, {e}")


def open_images(path):
    files = [os.path.join(path, name) for name in os.listdir(path)]
    count = 0
    for file in files:

        if ".jpg" in file:
            img = open_image(file)
            if img:
                move(file, os.path.join(Save_Train, f"Anime_Face{count}.jpg"))
                count += 1

                break


def move(p1, p2):
    shutil.move(p1, p2)


def main():
    open_image(image_dir)


main()
