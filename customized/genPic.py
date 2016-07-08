#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image, ImageDraw, ImageFont, ImageFilter
import random

# Random letter:
def rndChar():
    return chr(random.randint(65, 90))

# Random color:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# Random color:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# create Font object:
font = ImageFont.truetype('Arial.ttf', 36)
# create Draw object:
draw = ImageDraw.Draw(image)
# Fill each pixel:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# output letter:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# vague:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg');

#	Generate picture