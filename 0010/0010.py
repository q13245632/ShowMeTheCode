# -*-coding:utf8 -*-
# author: yushan
# date: 2017-03-02
# 参考廖雪峰的PIL生成验证码教程

import string
import random
from PIL import Image,ImageDraw,ImageFont,ImageColor,ImageFilter

def get_char():
    return random.choice(string.letters)

def get_color():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def get_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB',(width,height),color=(255,255,255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Verdana.ttf', 36)
for i in xrange(width):
    for j in xrange(height):
        draw.point((i,j),fill=get_color())

for k in xrange(4):
    draw.text((60 * k,10),get_char(),fill=get_color2(),font=font)

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')