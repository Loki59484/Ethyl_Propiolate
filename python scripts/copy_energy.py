import os
dir  = '/home/loki/Research/Ethyl_Propiolate'
ext =  '.log'
i=0

for files in os.walk(dir, topdown=True):
    for file in files[2]:
        if file.endswith(ext) and '_IRC_POINT' in file:
                target_file = files[0]+'/'+ file 
                ccsdt = files[0]+'/'+ file.lower().replace('.log','ccsdt.log')                
                if os.path.exists(ccsdt):
                    i+=1
                    source = open(ccsdt,'r')
                    source_temp = source.read()
                    source.close()
                    block = ''.join(source_temp[source_temp.index('N-N='):source_temp.index('@')].replace('\n','').replace(' ','')).split('\\')
                    for item in block:
                         if 'CCSD(T)=' in item:
                            _,_,energy1 = item.partition('=')
                    target = open(target_file,'r')
                    temp = target.readlines()
                    target.close()                    
                    for linenum,lines in enumerate(temp):
                        if "Sum of electronic and zero-point Energies" in lines:
                            _,_,energy  = lines.partition('=')  
                            energy = energy.lstrip()
                            print('old = ',temp[linenum])
                            newline =lines.replace(energy,energy1+'\n')
                            temp[linenum] = newline
                            print('new = ',temp[linenum])                          
                    with open(target_file,'w') as output_file:
                        output_file.writelines(temp)

print(i)