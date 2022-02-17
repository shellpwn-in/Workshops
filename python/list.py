#! /usr/bin/python3

#list are used to stored multiple items in a single variable 

a = ["Apple","Microsoft","Linux","Tata","BMW","Ferrari"] #square brackets are used in list

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

# Printing using a loop
for i in range(len(a)):
    print(a[i])
print("\n")

# Printing using a in a different way
for i in a:
    print(i)
print("\n")

#printing a part of list, like first 2 or first 3 items 
print(a[0:2]) #prints the first two items in the list.
print(a[0:4]) #prints the first four items in the list.
print("\n")

#adding items in list using append and insert 

a.append("Lamborghini") #will add Lamborghini item in list after the last item in list 
print(a)
a.insert(0,'Tesla') #with insert,you can specify the index too,Tesla will be the first here now .
print(a)
print("\n")

#removing items from list 
a.pop(4) #will remove the item with index 4,i.e Tata
print(a)
a.remove("Ferrari") #used to remove the item directly without index,here it Ferrari will be removed.
print(a)





