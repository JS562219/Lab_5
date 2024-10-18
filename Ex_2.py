from machine import Pin, ADC
from hcsr04 import HCSR04
import time
import math

import hardware_setup  # Create a display instance
from gui.core.ugui import Screen, ssd
from gui.widgets import Label, Dial, Pointer, CloseButton,Textbox  ,Button

# Now import other modules
from cmath import rect, pi
import uasyncio as asyncio
import time

# Font for CWriter
import gui.fonts.arial10 as font
from gui.core.colors import *
from gui.core.writer import CWriter

sensor = HCSR04(trigger_pin = 1, echo_pin = 2)   #set trigger and echo pins
async def client(dist):
    while 1:
        distance = sensor.distance_cm()          #set distance to cm
        print('Distance:',distance)              
        dist.value(str(distance) + "cm")         #read distance value
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
        lbl = Label(wri,4,4,text='                         ')
        self.reg_task(client(lbl))

        CloseButton(wri)

def test():
   
    Screen.change(BaseScreen)
test()
