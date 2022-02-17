#! /usr/bin/python3 

#Dictionaries are used to store data values in key:value pairs.

dogs = {'Breed':'German','Size':'big','Colour':'Brown'} #here,Breed is the key and German is the value of the key.
print(dogs)

#printing only keys.
print(dogs.keys())

#printing only values.
print(dogs.values())

#printing value of specific key
print(dogs['Size']) #will return the value of key,'size' if it exist .

#print the items of dictionary in tuples.
print(dogs.items())

#adding a new key-value pair.
dogs['age'] = 5
print(dogs)

#removing a key
dogs.pop('Size','big')
print(dogs)
