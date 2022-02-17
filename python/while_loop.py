#!/bin/python3

"""
while loop also run as for but difference that in for loop you know number of times you want to run the loop, where as in while loop we give condition till which it will run.
"""

"""
syntax of while loop

condition_variable
while condition:
    code_here
    condition_variable_modification
"""

# while loop that prints from 0 to 10
i = 0
while i < 10:
    print(i)
    i += 1
print("\n")

i = 5
while i < 10:
    print(i)
    i += 1
print("\n")



i=1
while i < 10:
    print(i)
    i += 2

print("\n")


""" for loop ka hi karte while loop se

i = input("Enter a number : ")
i = int(i)  #condition_variable
while i != 0:
    print("Number is",i) #code_here
    i = i - 1            #condition_variable_modification
	
print("while loop ended")
"""
