#!/bin/bash
cd "/home/loki/Research/Ethyl_Propiolate/conformers"
while read id; do 
wget -O "conformer_$id.pcjson" "https://pubchem.ncbi.nlm.nih.gov/rest/pug/conformers/$id/JSON?response_type=save&response_basename=Conformer3D_COMPOUND_CID_12182"; 
obabel conformer_$id.pcjson -O conformer_$id.mol
done < conformerids.txt 
		
python3
import os
os.system("clear")
for files in os.walk("/home/loki/Research/Ethyl_Propiolate/conformers", topdown=True):
	for file in files[2]:
		source = open(files[0]+"/"+file,'r')
		temp = source.readlines()
		temp.remove(temp[0])
		temp.remove(temp[0])
		for item in reversed(["%nprocshared=24\n","%mem=12GB\n","%chk=ethyl_propiolate.chk\n","# opt=(calcfc,tight,noeigentest) freq 6-31+g m062x\n"]):
			temp.insert(0,item)
		with open(files[0]+"/"+file,'w') as output:
			output.writelines(temp)
exit()

