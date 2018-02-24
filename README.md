# ili9341_SPI_TouchScreen_LCD_Raspberry-Pi

![Image](https://github.com/BehindTheSciences/ili9341_SPI_TouchScreen_LCD_Raspberry-Pi/blob/master/ili9341_RPi.jpg)

#Wiring


# Basic Demo
python BTS_SPI_LCD_DEMO.py


# ENABLE SPI1 ON THE RASPBERRY PI
SPI1 is disabled by default and to enable it, enter the following in your /boot/config.txt
#enable spi1 with a single CS line
dtoverlay=spi1-1cs
This will only enable one CS line; you can have up to 3 on the SPI1 bus. For options see /boot/overlays/README

Reboot your Pi and check whether you see SPI1 in /dev/

You should see:

/dev/spidev0.0
/dev/spidev0.1
/dev/spidev1.0

https://behindthesciences.com/electronics/connecting-ili9341-SPI-TouchScreen-lcd-to-a-raspberry-pi-in-python/
