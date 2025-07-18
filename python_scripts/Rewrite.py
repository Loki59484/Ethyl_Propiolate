import os
from pprint import *
import numpy as np
dir = '/home/loki/Research/Ethyl_Propiolate'
ext = ('.gjf')
i=0
os.system("clear")
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
for files in os.walk(dir, topdown = True):
    for file in files[2]:
        if '_irc_points' in files[0] and 'ts5a' in file and file.endswith(ext):
            hit = file[file.index('nt')+2:file.index('nt')+4]
            print(hit)            
            newname = file.replace(hit,match[hit]).replace('.gjf','new.gjf')
            os.rename(files[0]+'/'+file,files[0]+'/'+newname)
            print(file)
            print(newname)
            i+=1
print(i)