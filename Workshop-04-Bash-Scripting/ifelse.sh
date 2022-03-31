#!/bin/bash 
echo "what's your age ?"
read age

if [ "$age" = "20" ];then
	echo "Hey there,fellow 20 year old !"
else
	echo "You look like you're 20!"
fi