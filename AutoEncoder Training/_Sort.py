import os
import shutil
from PIL import Image

Train = os.path.join(os.curdir, "Train", "Face")
Validation = os.path.join(os.curdir, "Validation", "Face")

image_dir = os.path.join(os.curdir, "Orginal Image")
save_dir = Train

def open_image(path):
    try:
        img = Image.open(path)
        if img.height > 64:
            return img.resize((64, 64))
        else:
            return None
    except Exception as e:
        print(f"UNKNOWN ERROR {path}, {e}")


def move():
    file_name  = os.listdir(Train)
    print(f"Moved This Amount Of File: {int(len(file_name)*0.1)}")

    for index in range(int(len(file_name)*0.1)):
        name = file_name[index]
        shutil.move(os.path.join(Train, name), os.path.join(Validation, name))



def main():
    imgs = os.listdir(image_dir)

    for index in range(len(imgs)):
        if ".jpg" in imgs[index]:
            a = open_image(os.path.join(image_dir, imgs[index]))
            if a:
                a.save(os.path.join(save_dir, f"Face {index + 902}.jpg"))

    move()



main()
