import os
from pprint import *
import numpy as np
dir = '/home/loki/Research/Ethyl_Propiolate/conformers'
ext = ('.log')
i=0
os.system("clear")
dump = []
for files in os.walk(dir, topdown = True):
    for file in files[2]:
        if file.endswith(ext):
            filename = files[0]+'/'+file
            source = open(filename,'r')
            temp = source.readlines()
            for linenum, line in enumerate(reversed(temp)):
                if 'Standard orientation:' in line:
                    start = len(temp)-linenum
                    dump.append(''+file[:-4]+'\n')
                    dump = dump+temp[start:start+4]
                    for nextnum, nextline in enumerate(temp[start+4:]):
                        if "----------------------------\n" in nextline:
                            dump.append(nextline)
                            break
                        else:
                            dump.append(nextline)
                    i+=1
                    break
with open(dir+'/'+'Opt_coord_table.txt', 'w') as output:
    output.writelines(dump)
print(i)