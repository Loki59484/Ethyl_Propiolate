import os
#script = ["#!/bin/bash \n","export g16root=/opt\n", "export GAUSS_SCRDIR=~/scratches/g16\n", "source $g16root/g16/bsd/g16.profile\n"]
commands = []
dir = '/home/aayush/Research/'
os.system('clear')
ext = ('.gjf')
i=0
for files in os.walk(dir,topdown=True):
    for file in files[2]:
        if file.endswith(ext):
            if 'irc_point' in file:
                input_file = files[0]+'/'+file
                output_file = (files[0]+'/'+file).replace('.gjf','ccsdt.log')
                if os.path.isfile(output_file):  
                    pass
                else:                  
                    commands.append(f"g16 < {input_file} | tee {output_file}" )
                    i+=1
#script.append(f"commands=({final})")

with open(dir+'commands.txt','w') as output: 
    output.write(str(commands).replace(',','\n').replace('[','(').replace(']',')').replace('\"',"").replace('\'',""))
print(i)

