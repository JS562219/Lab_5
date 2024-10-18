from machine import Pin, ADC
import time
import math

import hardware_setup  # Create a display instance
from gui.core.ugui import Screen, ssd
from gui.widgets import Label, Dial, Pointer, CloseButton,Textbox  ,Button

# Now import other modules
from cmath import rect, pi
import uasyncio as asyncio
import time
from gui.core.writer import CWriter

# Font for CWriter
import gui.fonts.arial10 as font
from gui.core.colors import *

adc1 = ADC(Pin(26))  #set ADC pin on explorer
Vin =  65535         #3.3 volts in digital form

A = 1.009249522E-3   #Steinhart constants
B = 2.378405444E-4
C = 2.019202697E-7

R1 = 10000           #known resistor value in ohms
async def client(temp):
    while 1:
        Vout = (adc1.read_u16()/65535)*3.3   #reads adc pin and converts
        R2 = R1*((3.3/Vout)-1)               #calculate R2
        print("R2: ",R2)
        T = (1.0 / (A + B * math.log(R2) + C * math.log(R2) * math.log(R2) * math.log(R2)))   # Calc temperature in celcius 
        F = (T-273.15)*1.8+32   #convert to fahrenheit 
        print("V_out", Vout)
        print("Temp (F)",F)
        temp.value(str(F) + "F")
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
        lbl = Label(wri,2,2,text='                  ')
        self.reg_task(client(lbl))

        CloseButton(wri)

def test():
   
    Screen.change(BaseScreen)
test()






