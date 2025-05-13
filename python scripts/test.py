source = open('/home/loki/Research/Ethyl_Propiolate/kisthelp_input_files/TS13_PATH.kinp','r')
temp = source.readlines()
for line in temp:
	if '-420' in line:
		print((float(line.replace('\n',''))+419.3484935)*2625.5)