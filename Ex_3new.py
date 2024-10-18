from machine import Pin, ADC, I2C
import time
import math

import hardware_setup
from gui.core.ugui import Screen, ssd
from gui.widgets import Label, Textbox, Button, CloseButton

from gui.core.colors import *
from gui.core.writer import CWriter
import gui.fonts.arial10 as font

import utime as time
from dht import DHT11, InvalidChecksum
import uasyncio as asyncio

async def client(templbl, humidlbl):
    while True:
        time.sleep(2)                           #time between measurements
        pin = Pin(26, Pin.OUT, Pin.PULL_DOWN)   #set pin to ADC0 on pico explorer
        sensor = DHT11(pin)                     #use DHT 11 to configure sensor
        t = (sensor.temperature)                
        h = (sensor.humidity)
        humidlbl.value("Humidity: {}".format(sensor.humidity)+ "%")       #label for humidity on screen
        templbl.value("Temperature: {}".format(sensor.temperature)+ "C")  #label for temperature on screen
        print("Temperature: {}".format(sensor.temperature))
        print("Humidity: {}".format(sensor.humidity))
        await asyncio.sleep_ms(150)

class BaseScreen(Screen):
    def __init__(self):
        super().__init__()
        labels = {'bdcolor' : RED,
                'fgcolor' : WHITE,
                'bgcolor' : DARKGREEN,
                'justify' : Label.CENTRE,
                }
    
        wri = CWriter(ssd, font, GREEN, BLACK)  # verbose = True
        hlbl = Label(wri,4,4,text='                                 ')   #creates space for label
        tlbl = Label(wri,30,1,text='                                ')   #creates space for label
        self.reg_task(client(hlbl, tlbl))

        CloseButton(wri)

def test():

    Screen.change(BaseScreen)
test()
