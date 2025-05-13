from pyautogui import *
import time
import os
os.system('clear')

time.sleep(5)       
session =  Point(x=98, y=85)
new = Point(x=98, y=113)
close = Point(x=98, y=188)
data = Point(x=144, y=78)
build_path = Point(x=186, y=177)
home = Point(x=1135, y=435)
drop = Point(x=1218, y=668)
file_type = Point(x=901, y=714)
file_name = Point(x=923, y=641)
calculation = Point(x=215, y=83)
atom = Point(x=227, y=111)


def save(state,point,coordinate):
    if 1<= state <=5:
        if point == 1:
            click(home)
            click(file_name)
            typewrite(f'/home/loki/Research/Ethyl_Propiolate/Ethyl_prop_non-planar/Transition_states/Addition/ts{state}add_irc_points/TS{state}add_IRC_POINT0{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')
        

        elif 1 < point < 10:
            click(file_name)
            typewrite(f'TS{state}add_IRC_POINT0{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')
            
        else:
            click(file_name) 
            typewrite(f'TS{state}add_IRC_POINT{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')
    
    elif 6<= state <=8:
        if point == 1:
            click(home)
            click(file_name)
            typewrite(f'/home/loki/Research/Ethyl_Propiolate/Ethyl_prop_non-planar/Transition_states/Abstraction/ts{state}abs_irc_points/TS{state}abs_IRC_POINT0{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')

        elif 1 < point < 10:
            click(file_name)
            typewrite(f'TS{state}abs_IRC_POINT0{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')
        else:
            click(file_name) 
            typewrite(f'TS{state}abs_IRC_POINT{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')

    
    elif 9<= state <=11:
        if point == 1:
            click(home)
            click(file_name)
            typewrite(f'/home/loki/Research/Ethyl_Propiolate/Ethyl_prop_planar/Transition_states/Addition/ts{state}add_irc_points/TS{state}add_IRC_POINT0{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')
        
        elif 1 < point < 10:
            click(file_name)
            typewrite(f'TS{state}add_IRC_POINT0{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')
            
        else:
            click(file_name) 
            typewrite(f'TS{state}add_IRC_POINT{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')
    
    elif 12<= state <=14:
        if point == 1:
            click(home)
            click(file_name)
            typewrite(f'/home/loki/Research/Ethyl_Propiolate/Ethyl_prop_planar/Transition_states/Abstraction/ts{state}abs_irc_points/TS{state}abs_IRC_POINT0{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')
        
        elif 1 < point < 10:
            click(file_name)
            typewrite(f'TS{state}abs_IRC_POINT0{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')
            
        else:
            click(file_name) 
            typewrite(f'TS{state}abs_IRC_POINT{point}.log')
            hotkey('enter')
            time.sleep(1)
            typewrite(coordinate)
            hotkey('enter')
    
        

for state in range(14,15):
    click(session)
    click(close)
    hotkey('enter')
    click(session)
    click(new)
    click(data)
    click(build_path)
    hotkey('enter')
    typewrite('21')
    hotkey('enter')

    coordinate = ['-1.0', '-0.9', '-0.8', '-0.7', '-0.6', '-0.5', '-0.4', '-0.3', '-0.2', '-0.1', '0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0'] 
    #coordinate.reverse()
    i=0
    for point in range(1,22):
        save(state,point,coordinate[i])
        i+=1

    click(home)
    click(file_name)
    typewrite(f'TS{state}_PATH')
    input('press enter to continue')
    time.sleep(3)