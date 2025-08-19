#!/bin/bash
trap "echo 'Interrupted by Ctrl+C. Exiting loop.'; exit 1" SIGINT;
find -name "*irc*ccsdt.gjf" |sort | while read file; do

if grep -Fxq "${file/.gjf/ccsdt.log}" "completed_queue.txt";then
        continue
fi 

if grep -Fxq "${file/.gjf/ccsdt.log}" "completed_queue_college.txt";then
        continue
fi 

if  [[ "$file" == *"Addition/ts6add_ircpoints"* ]];then

#echo "${file/.gjf/ccsdt.log}" >> "completed_queue_college.txt"
file_c=$(sed 's/%mem=12GB/c\%mem=60GB/g' $file)

g16 < "$file_c" | tee "${file/.gjf/ccsdt.log}"
    if [ $? -ne 0 ]; then
        echo "Error running g16 on $file. Exiting loop."
        break
    fi
git add .;git commit -m 'ccsdt ran';git push origin main
find ~/ -type f -name "*.rwf" -mtime +1 -delete
fi;
done



