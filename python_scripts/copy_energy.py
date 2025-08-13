import os
dir  = '/home/loki/Research/Ethyl_Propiolate'
ext =  '.kinp'
os.system('clear')
i=0
for files in os.walk(dir, topdown=True):
    for file in files[2]:
        if file.endswith(ext) and '_IRC_POINT' in file or 'irc_point':
                target_file = files[0]+'/'+ file 
                ccsdt = files[0]+'/'+ file.lower().replace('.kinp','ccsdt.log')                
                if os.path.exists(ccsdt):
                    try:
#                        print(files[0]+'/'+file)
#                        print(ccsdt)
                        source = open(ccsdt,'r')
                        source_temp = source.read()
                        source.close()
                        block = ''.join(source_temp[source_temp.index('N-N='):source_temp.index('@')].replace('\n','').replace(' ','')).split('\\')
                        for item in block:
                            if 'CCSD(T)=' in item:
                                _,_,energy = item.partition('=')
                        target = open(target_file,'r')
                        temp = target.readlines()
                        target.close()                    
                        for linenum,lines in enumerate(temp):
                            if "*POTENTIAL ENERGY" in lines:
                                old = temp[linenum+1]
                                temp[linenum+1] = energy+'\n'
                                if old==temp[linenum+1]:
                                    print(files[0]+'/'+file)
                                    print(ccsdt)
                                    print(old)
                                    print(temp[linenum+1])                   
                                    i+=1       
                        with open(target_file,'w') as output_file:
                            output_file.writelines(temp)
                    except ValueError:
                        print(file)
                        print(ccsdt)
print(i)