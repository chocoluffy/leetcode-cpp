old="$IFS"
IFS='-'
str="$*"
IFS=$old
cp -r template/ "$str"