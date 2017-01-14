# -*-coding:utf8 -*-
# Author: yushan
# Time: 2017/1/14
from PIL import Image, ImageDraw, ImageFont
img_path = "img.jpg"
font_type = "C:\Windows\Fonts\Arial.ttf"
font_size = 60


def draw_dig(n):
    text = str(n)
    img = Image.open(img_path)
    w, h = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_type, font_size)
    draw.text((w * 0.9, 0), text, font=font, fill="red")
    img.save("new.jpg", "jpeg")


if __name__ == "__main__":
    draw_dig(3)
