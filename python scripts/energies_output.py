# reads .log/.out file and searches for specific keywords and their values. 
#outputs them to a file

#ethyl prop planar - 4 parts - values from each
#ethyl prop non planar - 4 parts - values from each

import os,ntpath,json

dir = 'E:\Research\Ethyl_propiolate'
string = "Sum of electronic"
check = "Normal termination of Gaussian"
Ethyl_prop_planar = {'Sum of electronic and zero-point Energies':{},
          'Sum of electronic and thermal Energies':{},
          'Sum of electronic and thermal Enthalpies':{},
          'Sum of electronic and thermal Free Energies':{},
          'Entropy':{}}
Ethyl_prop_nonplanar = {'Sum of electronic and zero-point Energies':{},
          'Sum of electronic and thermal Energies':{},
          'Sum of electronic and thermal Enthalpies':{},
          'Sum of electronic and thermal Free Energies':{},
          'Entropy':{}}
ext = ('.out', '.LOG')

for files in os.walk(dir, topdown = True):
    for file in files[2]:        
        if file.endswith(ext):  
            source = open(files[0] + "\\" + file,'r')
            temp = source.readlines()
            source.close()
            for lines in temp:
                if check in lines:
                    for linenum,line in enumerate(temp):
                        if string in line:
                            targ,_,val = line.partition('=')
                            targ = str.lstrip(targ)
                            if files[0].find("Ethyl_prop_planar") != -1:
                                Ethyl_prop_planar[targ][ntpath.basename(file)] = val.strip()
                                if targ == 'Sum of electronic and thermal Free Energies':
                                    entropy = temp[linenum+4]
                                    Ethyl_prop_planar['Entropy'][ntpath.basename(file)] = entropy.split()[3]
                            elif files[0].find("Ethyl_prop_non-planar") != -1:
                                Ethyl_prop_nonplanar[targ][ntpath.basename(file)] = val.strip()
                                if targ == 'Sum of electronic and thermal Free Energies':
                                    entropy = temp[linenum+4]
                                    Ethyl_prop_nonplanar['Entropy'][ntpath.basename(file)] = entropy.split()[3]
                                
        else:
            pass

with open('planar.txt','w') as output_file:
    output_file.write(json.dumps(Ethyl_prop_planar))
with open('nonplanar.txt','w') as output_file:
    output_file.write(json.dumps(Ethyl_prop_nonplanar))