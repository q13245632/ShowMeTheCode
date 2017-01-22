# -*-coding:utf8 -*-
# author: yushan
# date: 2017-01-22
# summary: 更改图片尺寸大小
import os
import os.path
from PIL import Image


def change_image(imgpath, savepath, width, height):
    img = Image.open(imgpath)
    save_img = img.resize((width, height), Image.ANTIALIAS)
    save_img.save(savepath)

root_dir = "img"
lst_file = os.listdir(root_dir)
for i in lst_file:
    img_path = "img\\" + i
    save_path = "after\\" + i
    width = 500
    height = 500
    change_image(img_path, save_path, width, height)


