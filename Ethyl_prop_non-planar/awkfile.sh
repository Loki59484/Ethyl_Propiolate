\find . \( -name "*.log" -o -name "*.out" \) ! -name "*irc*.log" |sort| \
xargs -I {} awk -F'[ =]+' '
    BEGIN {
        zero_point = ""
        free_energy = ""
	thermal_energy = ""
	thermal_enthalpies = "" 
    }
    /Sum of electronic and zero-point Energies/ {
        zero_point = $NF
    }
    /Sum of electronic and thermal Free Energies/ {
        free_energy = $NF
    }
    /Sum of electronic and thermal Energies/ {
	thermal_energy = $NF
    }
    /Sum of electronic and thermal Enthalpies/ {
        thermal_enthalpies = $NF
    }



    END {
        if (zero_point != "" || free_energy != "" || thermal_energy != "") {
	   split(FILENAME,parts,"/") 
	   filename = parts[length(parts)]
           print filename "," zero_point "," thermal_energy "," thermal_enthalpies "," free_energy
        }
    }' {}
