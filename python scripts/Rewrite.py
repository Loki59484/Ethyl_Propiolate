import os
from pprint import *
dir = '/home/loki/Research/Ethyl_Propiolate'
ext = ('.png','.kinp','.kstp')
i=0
prefixes = [
'ts11',
'ts6',
'ts7',
'ts8',
'ts2',
'ts4'
]
print('started')
os.system("clear")
for files in os.walk(dir, topdown = True):
    for file in files[2]:
        if '_irc_points' in files[0] and not any(x in files[0] for x in prefixes):
            print(file)