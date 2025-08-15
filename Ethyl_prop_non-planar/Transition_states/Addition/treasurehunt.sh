
field=$(cat ts1add_irc.log | awk '/Input orientation/ { count=6 }
     count > 0 { count--; if (count == 0) { print $4 } }'
)

for val in $field ; do
for i in $(ls $1 | grep ".gjf"|grep -v "ccsdt" | sort);do
if grep -- "$val" "$1/$i";then
echo $i $(grep -- "$val" "$1/$i")
fi
done
done
