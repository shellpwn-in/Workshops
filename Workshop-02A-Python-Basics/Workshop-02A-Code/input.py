#! /usr/bin/python3

#In order to give input as user,we use input() function.

name = input('Enter Your Name : ')
print(name) #will print your input stored in the name variable 

age = float(input('Enter Your age : '))
age = int(age)
print(age) #will print value stored in the age variable 

#adding in a sentence 
print("\n")
print("Printing with string concatination")
print("Welcome user, your name is "+name+" and your age is "+ str(age))
print("\n")
print("Printing with .format")
print("Welcome user, your name is {} and your age is {}".format(name,age))
print("\n")
print("Printing with f string")
print(f"Welcome user, your name is {name} and your age is {age}")
print("\n")
#Notice here we have to use str() for age and not for name,that's because age is a integer variable and you cant add vartiables of different datatypes 
print("Data-type of variable name and age")
print(type(name))
print(type(age))
print("\n-")
#we can change data type of an integer variable to string by using str(variable)
print("Changing data type of age from int to string")
print(type(str(age)))







