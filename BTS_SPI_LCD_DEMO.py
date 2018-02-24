# tft24T modified by BehindTheSciences.com
# Credits to  Brian Lavery

#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so.

# A demo of LCD/TFT SCREEN DISPLAY

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from lib_tft24T import TFT24T
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import spidev
from time import sleep

# Raspberry Pi configuration.
#For LCD TFT SCREEN:
DC = 24
RST = 25
LED = 15

#For PEN TOUCH:
#   (nothing)

# Create TFT LCD/TOUCH object:
TFT = TFT24T(spidev.SpiDev(), GPIO, landscape=False)
# If landscape=False or omitted, display defaults to portrait mode
# This demo can work in landscape or portrait


# Initialize display.
TFT.initLCD(DC, RST, LED)
# If rst is omitted then tie rst pin to +3.3V
# If led is omitted then tie led pin to +3.3V

# Get the PIL Draw object to start drawing on the display buffer.
draw = TFT.draw()

while 1:
    TFT.clear((255, 0, 0))

    # Alternatively can clear to a black screen by simply calling:
    TFT.clear()
    print('Loading image...')
    image = Image.open('bl.jpg')

    # Resize the image and rotate it so it's 240x320 pixels.
    image = image.rotate(90,0,1).resize((240, 320))
    # Draw the image on the display hardware.
    print('Drawing image')
    TFT.display(image)
    sleep(3)
    print "Test a long para of text, auto-wrapped into screen lines."
    TFT.clear()
    font=ImageFont.truetype('FreeSans.ttf', 18)
    text1 = \
"""Visit www.behindthesciences.com for more tutorials on Raspberry Pi and Arduinos!"""
    if TFT.is_landscape:
        draw.textwrapped((0,0), text1, 38, 20, font, "lightblue")
    else:
        draw.textwrapped((0,0), text1, 27, 20, font, "lightblue") # a bit narrower for portrait!
    TFT.display()
    sleep(1)

    TFT.clear((90,90,255))
    print "show a font in giant letters"
    font = ImageFont.truetype('FreeSerifItalic.ttf', 40)
    draw.textrotated((100,10), 'BehindTheSciences',90 ,font=font, fill="RED")   # signature !

    TFT.display()
    sleep(2)

#        All colours may be any notation (exc for clear() function):
#        (255,0,0)  =red    (R, G, B) - a tuple
#        0x0000FF   =red    BBGGRR   - note colour order
#        "#FF0000"  =red    RRGGBB   - html style
#        "red"      =red    html colour names, insensitive
