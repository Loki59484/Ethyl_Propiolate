from pyautogui import *
import time
import os
from pynput import keyboard
os.system('clear')

time.sleep(5)       
session =  Point(x=98, y=85)
new = Point(x=98, y=113)
close = Point(x=98, y=188)
calc = Point(x=201, y=86)
vtst = Point(x=230, y=245) #vtst/eck
bimol = Point(x=313, y=257)
save_as = Point(x=109, y=172)
dir = '/home/loki/Research/kisthelp_input_files/planar/' #planar
#dir = '/home/loki/Research/kisthelp_input_files/non-planar/' #non-planar

dict = {
    '1' : '154.77164970',
    '2'	: '178.75690495',
    '3' : '167.99051710',
    '4'	: '20.93836250',
    '5'	: '75.98538315',
    '6'	: '78.75134740'
    }

def calc_tst(R1,R2,path,state):
    print(f'vtst-eck calculation started for {path}')
    click(calc)
    time.sleep(0.5)
    click(vtst)
    time.sleep(0.5)
    click(bimol)
    time.sleep(0.5)
    typewrite(R1)
    hotkey('enter')
    time.sleep(1.5)
#    hotkey('enter')
    typewrite(R2)
    hotkey('enter')
    time.sleep(1.5)
#    hotkey('enter')
    typewrite(path)
    hotkey('enter')
    time.sleep(6)
    typewrite(dict[str(state)])
    hotkey('enter')
    time.sleep(3)
    click(session)
    click(save_as)
    typewrite(f'/home/loki/Research/VTST-ECK/planar/TS{state}_VTST-ECK')
#    typewrite(f'/home/loki/Research/VTST-ECK/non-planar/TS{state}_VTST-ECK')
    hotkey('enter')

for state in range(5,6):
    if state==10:
        pass
    else:
        click(session)
        click(close)
        hotkey('enter')
        click(session)
        click(new)        
        calc_tst(dir+'ETHYL_PROPIOLATE_PLANAR_m062x.LOG',dir+'OH-radical_m062.out',dir+f'TS{state}_PATH.kinp',state) #planar   
#        calc_tst(dir+'ethyl_propiolate_non_planar_m062.out',dir+'OH-radical_m062.out',dir+f'TS{state}_PATH.kinp',state) #non_planar