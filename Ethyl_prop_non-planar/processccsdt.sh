#!/bin/bash
echo ''> ccsdts.txt
echo ''>ccsdtfiles.txt
# Find directories, loop through them, and then find files within each.
# This approach is less efficient than a single find command but matches your original logic.
find \( -name "*.log*" -o -name "*.log*" \) \( ! -name "*irc*" ! -name "*point*" \) -print0 | while IFS= read -r -d '' file; do
if grep "CCSD" $file;then
	echo $file >> ccsdtfiles.txt
    echo "$file : " $(grep -B 5 "@" "$file"|  tr "\n" " " | tr -d [:space:]|tr "\\" "\n"|grep "CCSD(T)=")>> ccsdts.txt
    #grep -v "CCSD(T)= " | grep "CCSD(T)" | sed 's/ //g'| tr "\\" "\n"| grep "CCSD(T)") 
    #echo $(grep -B 5 "@" "$file"| grep -v "CCSD(T)= ") > ccsdts.txt
    #echo "$file" $(cat ccsdts.txt | tr "\\" "\n"|grep "CCSD(T)" | sed 's/ //g') >> newccsdts.txt
  #  echo $(cat ccsdts.txt | grep "CCSD(T)")
  #cat newccsdts.txt
fi
  done
#echo $(find -name "*ccsdt.log" | sort | xargs -I {} grep -A 1 "CCSD(T)=" {}| grep -v "CCSD(T)= ") >> ccdtss.txt 
