import RPi.GPIO as gpio
import keyboard
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward():
    gpio.output(7, True)
    time.sleep(1)
    gpio.output(7, False)
    
    #print("UP")
    
def reverse(a):
    #gpio.output(11, True)
    #time.sleep(1)
    #gpio.output(11, False)
    #gpio.cleanup()
    print("DOWN")
    
def left(a):
    #gpio.output(13, True)
    #time.sleep(1)
    #gpio.output(13, False)
    #gpio.cleanup()
    print("LEFT")
    
def right(a):
    #gpio.output(15, True)
    #time.sleep(1)
    #gpio.output(15, False)
    #gpio.cleanup()
    print("RIGHT")
    
init()

from pynput.keyboard import Key, Listener

def on_press(key):
    if key == Key.up:
        forward()

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
        
    