#!/bin/bash  
export g16root=/opt
export GAUSS_SCRDIR=~/scratches/g16
source $g16root/g16/bsd/g16.profile 
logfile="completed_queue.txt"
clear
log(){
    echo "$1" >> $logfile
}
echo "Commands Log:">$logfile
readarray -t commands < $1
#echo "${commands[@]}"
cleanup(){
    echo "$1"
}
IFS=' '

for command in "${commands[@]}"; do
    echo "$command"
    sleep 10
    read -ra command_parts <<<  "$command"
    input="${command_parts[2]}"
    output="${command_parts[5]}"
    log "Executing $command"
    eval "$command"
    
    tail_line=$(tail -n 1 "$output")
    if [[ "$tail_line" == *"Normal termination"* ]];then
    log "Executed $command"
    else
    log "Failed $command"
    fi
    sleep 300
done

