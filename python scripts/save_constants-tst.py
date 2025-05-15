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
ktst = Point(x=96, y=89) 
ktunnel = Point(x=168, y=84) 
save_button = Point(x=117, y=145)
data_exit = Point(x=531, y=50)
time.sleep(3)

for correction in corrections:
    dir = f'/home/loki/Research/Ethyl_Propiolate/'
    for state in [5]:
        click(session)
        click(close)
        hotkey('enter')
        click(session)
        click(open)
        typewrite(f'{dir}VTST-{correction}/TS{state}_VTST-{correction}.kstp')
        hotkey('enter')
        click(temp)
        hotkey('tab')
        hotkey('ctrl','a')
        typewrite('200')
        hotkey('enter')
        hotkey('tab')
        hotkey('ctrl','a')
        typewrite('500')
        hotkey('enter')
        hotkey('tab')
        hotkey('ctrl','a')
        typewrite('1')
        hotkey('enter')
        click(k)
        click(datas)
        if correction == 'W':
            click(ktst)#--------------
            click(save_button)
            typewrite(dir+f'TST/Path{state}_k_tst')
            hotkey('enter')
            time.sleep(1)
        else:
            pass
        click(ktunnel)#---------------
        click(save_button)
        typewrite(dir+f'TST-{correction}/Path{state}_k_tst_tunnel')
        hotkey('enter')
        time.sleep(1)
        click(data_exit)