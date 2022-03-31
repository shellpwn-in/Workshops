#!/bin/bash
a=$(cat wordlist2.txt)
#echo $a 
for i in {"$a"};do
	echo $i
done 	