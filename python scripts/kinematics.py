from pyautogui import *
import time
import os
os.system('clear')

time.sleep(5)       
session =  Point(x=98, y=85)
new = Point(x=98, y=113)
close = Point(x=98, y=188)
calc = Point(x=201, y=86)
vtst = Point(x=230, y=245) #vtst/eck
bimol = Point(x=313, y=257)
save_as = Point(x=109, y=172)
dir = '/home/loki/Research/Ethyl_Propiolate/kisthelp_input_files/'

dict = {
'1' :	'135.43641750',
'2' :	'182.54287595',
'3' :	'124.21319265',
'4' :	'182.50611895',
'5' :	'181.80301005',
'6' :	'19.70227710',
'7' :	'90.05071175',
'8' :	'78.64974055',
'9' :	'154.77164970',
'10' :	'178.75690495',
'11' :	'167.99051710',
'12' :	'20.93836250',
'13' :	'75.98538315',
'14' :	'78.75134740',
'15' :  '134.79815845' #use path 4
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
    typewrite(f'/home/loki/Research/Ethyl_Propiolate/VTST-ECK/TS{state}_VTST-ECK')
    hotkey('enter')

for state in range(13,14):
    click(session)
    click(close)
    hotkey('enter')
    click(session)
    click(new)
    if state<9:         
        calc_tst(dir+'ethyl_propiolate_non_planar_m062.kinp',dir+'OH-radical_m062.kinp',dir+f'TS{state}_PATH.kinp', state) #non_planar
    else:
        calc_tst(dir+'ETHYL_PROPIOLATE_PLANAR_m062x.kinp',dir+'OH-radical_m062.kinp',dir+f'TS{state}_PATH.kinp', state) #planar   