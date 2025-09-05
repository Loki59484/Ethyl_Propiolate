#!/bin/bash
echo ''> ccsdts.txt
# Find directories, loop through them, and then find files within each.
# This approach is less efficient than a single find command but matches your original logic.
find -type d \( -name "*irc_points*" -o -name "*ircpoints*" \) -print0 | while IFS= read -r -d '' dir; do
  find "$dir" -maxdepth 1 -type f -name "*ccsdt.log" -print0 | while IFS= read -r -d '' file; do
    echo "$file : " $(grep -B 5 "@" "$file"|  tr "\n" " " | tr -d [:space:]|tr "\\" "\n"|grep "CCSD(T)")>> ccsdts.txt
    #grep -v "CCSD(T)= " | grep "CCSD(T)" | sed 's/ //g'| tr "\\" "\n"| grep "CCSD(T)") 
    #echo $(grep -B 5 "@" "$file"| grep -v "CCSD(T)= ") > ccsdts.txt
    #echo "$file" $(cat ccsdts.txt | tr "\\" "\n"|grep "CCSD(T)" | sed 's/ //g') >> newccsdts.txt
  #  echo $(cat ccsdts.txt | grep "CCSD(T)")
  #cat newccsdts.txt
  done
done
#echo $(find -name "*ccsdt.log" | sort | xargs -I {} grep -A 1 "CCSD(T)=" {}| grep -v "CCSD(T)= ") >> ccdtss.txt 
