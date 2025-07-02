#!/bin/bash
trap "echo 'Interrupted by Ctrl+C. Exiting loop.'; exit 1" SIGINT;
find -name "*ircpoint*.gjf" | while read file; do                                                                                              
if grep -Fxq $file "completed_queue.txt";then
	continue
fi
echo $file >> "completed_queue.txt"
g16 < "$file" | tee "${file/.gjf/ccsdt.log}"
    if [ $? -ne 0 ]; then
        echo "Error running g16 on $file. Exiting loop."
        break
    fi                                                                                                                                                             
 done
git add .;git commit -m 'ccsdt ran';git push origin main

