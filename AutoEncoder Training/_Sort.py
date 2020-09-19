import os
import shutil
from PIL import Image
DIRNAME = "cropped"


def make_folder(path):
    try:
        os.makedirs(path)
    except Exception as e:
        print(f"Already A Folder in {path}, Error Message: {e}")


Save_Train = os.path.join(os.curdir, "Train", "Face")
Save_Validation = os.path.join(os.curdir, "Validation", "Face")
image_dir = os.path.join(os.curdir, "Original Image", DIRNAME)

make_folder(Save_Train)
make_folder(Save_Validation)
make_folder(image_dir)


def open_image(path):
    try:
        img = Image.open(path)
        if img.height > 64:
            return img.resize((64, 64))
        else:
            pass
    except Exception as e:
        print(f"Cannot Open {path}, Error Message: {e}")


def open_images(path):
    files = [os.path.join(path, name) for name in os.listdir(path)]
    count = 0
    for file in files:
        img = open_image(file)
        if img:
            move(file, os.path.join(Save_Train, f"Anime_Face{count}.jpg"))
            count += 1


def move(p1, p2):
    shutil.move(p1, p2)


def make_validation(img_path, move_dir):
    files = [os.path.join(img_path, name) for name in os.listdir(img_path)]
    count = 0
    for index in range(int(len(files) * 0.1)):
        move(files[index], os.path.join(move_dir, f"Face {count} .jpg"))
        count += 1


def remove_dir_files(path):
    files = [os.path.join(path, name) for name in os.listdir(path)]
    for file in files:
        os.remove(file)


def main():
    open_images(image_dir)
    make_validation(Save_Train, Save_Validation)
    remove_dir_files(image_dir)  # Getting rid of unwanted image


main()
