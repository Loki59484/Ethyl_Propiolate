import os
from pprint import *
import numpy as np
dir = '/home/loki/Research/Ethyl_Propiolate/'
arr = np.arange(200,501,1)
arrr = [str(x) for x in arr if any([x%25==0,x==298])]
i=0
os.system("clear")
for files in os.walk(dir, topdown = True):
    for file in files[2]:
        if 'Path' in file:
            source = open(files[0]+'/'+file,'r')
            temp = source.readlines()
            source.close()
            dump = []
            for line in temp:
                if line[:3] in arrr:
                    dump.append(line[6:])
                    pprint(file)
            with open(files[0]+'/'+file,'w') as outputfile:
                outputfile.writelines(dump)
print(i)