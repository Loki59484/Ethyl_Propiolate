import pygetwindow as gw
from pywinauto import * 
from pyautogui import *
import re,time
import os
#0->Point(x=1774, y=387)
os.system('cls')
number = 10 #EDIT
dir=f'D:\Loki\Ethyl_propiolate\Ethyl_prop_non-planar\Transition states\Abstraction\\ts{number}_irc_points'#EDIT WHEN DIR CHANGED
os.makedirs(dir,exist_ok=True)

def file_check(point):
    windows = gw.getAllTitles()
    for title in windows:
            if re.match(fr'G1:M{point}:V1*', title): #EDIT WHEN FILE NAME DIFFERENT 
                if not 'irc_point' in title:
                    return True

time.sleep(5)
for point in range(1,22):
    check = file_check(point)
    print(f'{point}:{check}')
    if check == True:
        try:
            print(f"Saving automation initiated for point {point}")
            hotkey('ctrl','s')


            name = Point(x=1331, y=388)
            click(name)
            hotkey('ctrl','a')
            typewrite(f'ts{number}_irc_point{point}')
            
            path = Point(x=1475, y=148)
            click(path)
            hotkey('ctrl','a')
            typewrite(dir)
            press('enter')

            next_point = Point(x=113, y=41)
            click(next_point)

        except KeyboardInterrupt:
            print('interrupted')
    

    
