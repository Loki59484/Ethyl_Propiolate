import os
from pprint import *
import numpy as np

ext = ('.kstp')
i=0

dir = '/home/loki/Research/Ethyl_Propiolate/'

vals = {
    "minimum temperature :" : '200\n',
    "maximum temperature :" : '500\n',
    "temperature step:" : '25\n',
    "statistical factor:" : '1\n'
}

deg = {
    'sec' : '2\n',
    'pri' : '3\n'
}

os.system("clear")
for files in os.walk(dir, topdown = True):
    for file in files[2]:
        if 'TS' in file and file.endswith(ext) and any(x in file for x in ['7','8','13','14']):
            source = open(files[0]+'/'+file,'r')
            temp = source.readlines()
            source.close()
            for linenum,line in enumerate(temp):
                if "statistical factor:" in line:
                    if any(x in file for x in ['7','13']): 
                        temp[linenum+1] = deg['sec']
                    elif any(x in file for x in ['8','14']):
                        temp[linenum+1] = deg['pri']
                    print(temp[linenum+1])
            i+=1

            with open(files[0]+'/'+file,'w') as outputfile:
                outputfile.writelines(temp)
print(i)