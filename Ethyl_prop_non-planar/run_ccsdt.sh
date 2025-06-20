#!/bin/bash
trap "echo 'Interrupted by Ctrl+C. Exiting loop.'; exit 1" SIGINT;
''>"completed_queue.txt";
find -name "*ircpoint*.gjf" | while read file; do                                                                                              
echo $file >> "completed_queue.txt"
g16 < "$file" | tee "${file/.gjf/.log}"
    if [ $? -ne 0 ]; then
        echo "Error running g16 on $file. Exiting loop."
        break
    fi                                                                                                                                                             
 done
git add .;git commit -m 'ccsdt ran';git push origin main

