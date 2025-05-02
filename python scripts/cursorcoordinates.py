from pynput import keyboard
from pyautogui import *
import time
import os
os.system('clear')
key_pressed = False

def on_press(key): 
    global key_pressed
    try:
        if key.char == 'q':
            key_pressed = True
    except AttributeError:
        pass
def on_release(key):
    global key_pressed
    try:
        if key.char == 'q':
            key_pressed = False
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
print('listening started')

i=0
try:
    while True:
        if key_pressed==True:
            print(f'{i} : {position()}')
            time.sleep(0.2)  # Adjust the sleep time as needed
except KeyboardInterrupt:
    print("Program interrupted.")
finally:
    listener.stop()

print("Exiting...")