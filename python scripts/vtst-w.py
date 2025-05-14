from pyautogui import *
import time
import os
os.system('clear')

time.sleep(5)       
session =  Point(x=98, y=85)
new = Point(x=98, y=113)
close = Point(x=98, y=188)
calc = Point(x=201, y=86)
vtst = Point(x=237, y=215)
bimol = Point(x=310, y=233)
save_as = Point(x=109, y=172)
dir = '/home/loki/Research/Ethyl_Propiolate/kisthelp_input_files/'


def calc_tst(R1,R2,path,state):
    print(f'vtst-w calculation started for {path}')
    click(calc)
    time.sleep(0.5)
    click(vtst)
    time.sleep( 0.5)
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
    for i in range(0,21):
        hotkey('enter')
    time.sleep(1)
    click(session)
    click(save_as)
    typewrite(f'/home/loki/Research/Ethyl_Propiolate/VTST-W/TS{state}_VTST-W')
    hotkey('enter')

for state in [1,8]:
    click(session)
    click(close)
    hotkey('enter')
    click(session)
    click(new)
    if state<9 or state==15:         
        calc_tst(dir+'ethyl_propiolate_non_planar_m062.kinp',dir+'OH-radical_m062.kinp',dir+f'TS{state}_PATH.kinp', state) #non_planar
    else:
        calc_tst(dir+'ETHYL_PROPIOLATE_PLANAR_m062x.kinp',dir+'OH-radical_m062.kinp',dir+f'TS{state}_PATH.kinp', state) #planar
    time.sleep(3)