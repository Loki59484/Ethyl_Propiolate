for i in $(seq -f '%02g' 1 1 21); do
for j in $(seq -f '%02g' 1 1 21);do
echo $i
cat "testts1irc/ts1add_irc$i.gjf"
echo $j
cat "./ts1add_ircpoints/ts1add_ircpoint$j.gjf"
read -p "Press enter to continue..."
done
done
