#!/bin/bash
input_file="ccsdts.txt" 
while IFS= read -r line || [[ -n "$line" ]]; do
    if [ -z "$line" ]; then
        continue
    fi
       # Get the part before " : ", which is the log file path.
    log_filepath="${line%% : *}"
    # Get the part after the "=", which is the CCSD(T) value.
    ccsdt_value="${line##*=}"

    kinp_file="${log_filepath/ccsdt.log/.kinp}"
#if [ -f $kinp_file ]; then
#echo $kinp_file
#fi
#done<"$input_file"
sed -i "/^\*POTENTIAL ENERGY (in hartree)$/{n; s/.*/$ccsdt_value/}" "$kinp_file";done<"$input_file"
# The sed command to perform the in-place replacement
#
