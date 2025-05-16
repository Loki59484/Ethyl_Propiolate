import os
from pprint import *
import numpy as np

ext = ('.kstp')
i=0

dir = '/home/loki/Research/Ethyl_Propiolate/'

vals = {
    "minimum temperature :" : 200,
    "maximum temperature :" : 500,
    "temperature step:" : 25,
    "statistical factor:" : 1
}
os.system("clear")
for files in os.walk(dir, topdown = True):
    for file in files[2]:
        if 'TS' in file and file.endswith(ext):
            source = open(files[0]+'/'+file,'r')
            temp = source.readlines()
            source.close()
            for linenum,line in enumerate(temp):
                if any(x in str(line) for x in ["statistical factor:","minimum temperature :","maximum temperature :",'"temperature step:']):
                    temp[linenum+1] = vals[line.replace('\n','')] 
                    print(temp[linenum+1])
            i+=1
            with open(files[0]+'/'+file,'w') as outputfile:
                outputfile.writelines(str(temp))
print(i)