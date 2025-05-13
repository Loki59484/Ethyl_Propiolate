import os
from pprint import *
import numpy as np
dir = '/home/loki/Research/Ethyl_Propiolate'
ext = ('.gjf')
i=0
prefixes = [
'ts11a',
'ts6a',
'ts7a',
'ts8a',
'ts2a',
'ts4a',
'ts1a' #to be renamed after all processes are completed
]
ind1 = np.arange(1,22)
ind2 = np.flip(ind1)
match = {str(ind1[i]).zfill(2):str(ind2[i]).zfill(2) for i in range(len(ind1))}
os.system("clear")
for files in os.walk(dir, topdown = True):
    for file in files[2]:
        if  file.endswith(ext) and '_irc_points' in files[0] and not any(x in files[0] for x in prefixes):
            point = file[file.index('nt')+2:file.index('nt')+4]
            newname = file.replace(point,match[point])
#            os.rename(files[0]+'/'+file,files[0]+'/'+newname)
            i+=1
            print(file,"<---->",newname)
            break
print(i)