import os
from pprint import *
import numpy as np
dir = '/home/loki/Research/Ethyl_Propiolate'
ext = ('.log','.out')
i=0
os.system("clear")
dump = []
for files in os.walk(dir, topdown = True):
    for file in files[2]:
        if file.endswith(ext) and all([not x in file for x in ['_IRC','_irc','CCSDT','ccsdt']]):
            filename = files[0]+'/'+file
            source = open(filename,'r')
            temp = source.readlines()
            for linenum, line in enumerate(reversed(temp)):
                if 'S**2 before' in line:
                    print(line)

print(i)