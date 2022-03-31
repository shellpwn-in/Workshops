"""
> 	- 	greater than
< 	- 	less than
!=  -   not equal to
==   -	equal to
>=   -	greater than or equal to
<=	-	less than or equal to
"""


"""
"if" statement checks for statement on RHS and LHS and as an output is boolean data which is True or False.

if value returned by if statement is True then block of code inside "if" will execute, in same way canditions in elif are checked and at last if all condition fails else block is executed
"""

x = 1
y = 2

if x > y:
	print("x is greater than y")
	print("Inside if")
elif x == y:
	print("x is equal to y")
	print("Inside elif")
else:
	print("x is less than y")
	print("Inside else")
