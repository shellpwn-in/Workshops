#! /usr/bin/python3

#list are used to stored multiple items in a single variable 

a = ["1","2","3","4","5","6"] #square brackets are used in list

#printing a list 
print(a)
print("\n") #used to add a new line 

#printing a value at a certain index,in list index start froms 0
print(a[0]) #prints first item in list 
print(a[1]) #prints second item in list 
print(a[2]) #prints third item in list 
print(a[3]) #prints fourth item in list 
print(a[4]) #prints fifth item in list 
print(a[5]) #prints sixth item in list 
print(a[-1]) # Negative integers can be used to print from right to left,will print first word from right.
print("\n")

#printing a part of list, like first 2 or first 3 items 
print(a[0:2]) #prints the first two items in the list.
print(a[0:4]) #prints the first four items in the list.
print("\n")

#adding items in list using append and insert 

a.append("7") #will add Lamborghini item in list after the last item in list 
print(a)
a.insert(0,'0') #with insert,you can specify the index too,Tesla will be the first here now .
print(a)
print("\n")

#removing items from list 
a.pop(5) #will remove the item '5',if it exist in the list.
print(a)
a.remove("7") #will remove the item '7',if it exist in the list.
print(a)




