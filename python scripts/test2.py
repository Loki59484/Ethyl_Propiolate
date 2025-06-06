import os
from pprint import *
import numpy as np
dir = '/home/loki/Research/Ethyl_Propiolate/Ethyl_prop_non-planar'
ext = ('.gjf')
i=0
os.system("clear")
dump = []
for files in os.walk(dir, topdown = True):
    for file in files[2]:
        if file.endswith(ext) and 'Transition_states' in files[0] and all([not x in file for x in ['ccsdt','CCSDT','irc','IRC']]):
            print(file)
            filename = files[0]+'/'+file
            source = open(filename,'r')
            temp = source.readlines()
            for linenum, line in enumerate(temp):
                if '6-31+g' in line:
                        print(temp[linenum])
                        temp[linenum]=line.replace('6-31+g','6-311++g(d,p)')
                        print(temp[linenum])
            with open(filename,'w') as f:
                f.writelines(temp)
