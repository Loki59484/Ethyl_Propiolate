#!/bin/bash
asusctl profile -P Performance
trap "echo 'Interrupted by Ctrl+C. Exiting loop.'; exit 1" SIGINT;
find -name "*irc*ccsdt.gjf" |sort | while read file; do                                                                                              

if grep -Fxq "${file/.gjf/.log}" "completed_queue.txt";then
	continue
fi 

if grep -Fxq "${file/.gjf/.log}" "completed_queue_college.txt";then
	continue
fi

echo "${file/.gjf/.log}" >> "completed_queue.txt"
g16 < "$file" | tee "${file/.gjf/.log}"
    if [ $? -ne 0 ]; then
        echo "Error running g16 on $file. Exiting loop."
        asusctl profile -P Quiet
        find ~/ -type f -name "*.rwf" -mtime +1 -delete
        break
    fi                                                                                                                                                             
echo "Process Completed. Sleeping..."
sleep 3m
done
git add .;git commit -m 'ccsdt ran';git push origin main
find ~/ -type f -name "*.rwf" -mtime +1 -delete
asusctl profile -P Performance

