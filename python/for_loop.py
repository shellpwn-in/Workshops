#!/bin/python3 

# for loop is a way to repeat process for known number of times
# last value ie 10 here is ignored 
# range is a function which limits you values 

"""
syntax of for loop
for variable in range(start,end,step_size):
    code_here
"""

# For loop with step size 1
# from 0 to 10 (0 inclusive 10 exclusive)
for i in range(10):
    print(i)
print("\n")
# for loop with step size 1 ended

# from 5 to 10
for i in range(5, 10):
    print(i)    


print("\n")

# for loop with step size 2
j=1
for i in range(1,10,2):
    print(i, j)
    j = j + 1
print("\n")
# for loop with step size 2 ended

