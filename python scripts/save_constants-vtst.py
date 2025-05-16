from pyautogui import *
import time
import os
os.system('clear')
corrections = ['W','ECK'] 

session =  Point(x=98, y=85)
close = Point(x=98, y=188)
open =  Point(x=107, y=136)
temp = Point(x=839, y=120)
k = Point(x=1759, y=218)
datas = Point(x=496, y=176)
kvtst = Point(x=246, y=90)
ktunnel = Point(x=313, y=85)
save_button = Point(x=117, y=145)
data_exit = Point(x=531, y=50)
time.sleep(3)

for correction in corrections:
    dir = f'/home/loki/Research/Ethyl_Propiolate/'
    for state in range(1,16):
        click(session)
        click(close)
        hotkey('enter')
        click(session)
        click(open)
        typewrite(f'{dir}VTST-{correction}/TS{state}_VTST-{correction}.kstp')
        hotkey('enter')
        click(k)
        click(datas)
        click(kvtst)
        click(save_button)
        typewrite(dir+f'VTST/Path{state}_k_vtst')
        hotkey('enter')
        time.sleep(1)
        click(ktunnel)
        click(save_button)
        typewrite(dir+f'VTST-{correction}/Path{state}_k_tunnel')
        hotkey('enter')
        time.sleep(1)
        click(data_exit)
