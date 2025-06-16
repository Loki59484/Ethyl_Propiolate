import argparse
import cclib
import periodictable
import os
from tqdm import tqdm
import pprint
def process_file(path,file):       
    data = cclib.io.ccread(path+file)
    outdir = path + file.replace('.log','points/')
    os.makedirs(outdir,exist_ok=True)
    head = ["%nprocshared=24\n","%mem=12GB\n","%chk=ethyl_propiolate_ts1.chk\n","# freq 6-311++g(d,p) m062x\n","\n","Title Card Required\n","\n","0 2\n"]
    for i,coords in enumerate(tqdm(data.atomcoords, desc=f"Processing {file}",unit="point")):
        with open(outdir+file.replace('.log',f'point{i+1:02d}.gjf'),'w') as output:
            output.writelines(head)
            for atomno,xyz in zip(data.atomnos,coords):
                symbol = str(periodictable.elements[atomno])
                output.write(f"{symbol:<2} {xyz[0]:16.8f}{xyz[1]:16.8f}{xyz[2]:16.8f}\n")
def main():
    for files in os.walk(os.getcwd(),topdown=True):
        for file in files[2]:
            if '_irc.log' in file:
                process_file(files[0]+'/',file)

if __name__ == "__main__":
    main()               
