#!/bin/bash
i=0
while [ "$i" -lt 10 ];do
	((i++))
	if [ "$i" == "5" ];then
		continue 
	fi 	
	echo "Number:$i"
done 	
echo 'Broke out of the loop'