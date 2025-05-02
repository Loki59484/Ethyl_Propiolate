import os
from pprint import *
dir = '/home/aayush/Research/Ethyl_propiolate'
ext = ('.png','.kinp','.kstp')
i=0
print('started')
os.system("clear")
for files in os.walk(dir, topdown = True):
    for file in files[2]:
        if len(file) >4 and not file.endswith(ext) and not file[:3] in ['prc','PRC'] and file[0] in ['p','P']:
            if 'Abstraction' in files[0] and not 'abs' in file:
                newname = files[0] + '/' + file[:2]+'abs'+file[2:]
                print(newname)
                os.rename(files[0] + '/'+ file,newname)
                i+=1
            elif 'Addition' in files[0] and not 'add' in file:
                newname = files[0] + '/' + file[:2]+'add'+file[2:]
                print(newname)
                os.rename(files[0] + '/'+ file,newname)
                i+=1
print(i)
