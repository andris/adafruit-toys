# Metro IO demo
# Welcome to CircuitPython 2.2.0 :)

import board
import time
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
from pulseio import PWMOut
import audioio
import touchio
import simpleio
import random


# One pixel connected internally!
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.08)

# pizeo buzzer
buzzer = PWMOut(board.D5, variable_frequency=True)
buzzer.frequency = 262
OFF = 0
ON = 2**15

# Digital input with pullup on D2, D3, D4, D5, D6
buttons = []
for p in [board.D10, board.A3, board.D9, board.A4, board.D6]:
    button = DigitalInOut(p)
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    buttons.append(button)


# Digital output  on D8, D9, D10, D11, D12
buttonLeds = []
for p in [board.D13, board.A1, board.D12, board.A2, board.D11]:
    buttonLed = DigitalInOut(p)
    buttonLed.direction = Direction.OUTPUT
    buttonLeds.append(buttonLed)

# tones in Hz starting at C4
# tones = [261.626, 293.665 ,329.628, 349.228, 391.995]
tones = [262, 294 ,330, 349, 392]

# zip buttons, buttonLeds, and tones together for convenience
myButtons = []
for button, buttonLed, tone in zip(buttons, buttonLeds, tones):
  myButton = {}
  myButton["button"]=button
  myButton["buttonLed"]=buttonLed
  myButton["tone"]=tone
  myButtons.append(myButton)


######################### HELPERS ##############################


# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

def playTone(speaker, tone):
  speaker.frequency = tone
  speaker.duty_cycle = ON
  time.sleep(.5)
  speaker.duty_cycle = OFF

######################### MAIN LOOP ##############################

i = 0
while True:
  # spin internal neopixel LED around for pretty lights
  dot[0] = wheel(i & 255)

  for myButton in myButtons:
    if not myButton["button"].value:
      myButton["buttonLed"].value = not myButton["buttonLed"].value
      playTone(buzzer, myButton["tone"])
      time.sleep(.5)

  i = (i+1) % 256  # run from 0 to 255
  #time.sleep(0.01) # make bigger to slow down

