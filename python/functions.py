# functions are used to make reuse of specific piece of code

#  function 1
def printing():
	print("I am in function")
	
printing()
print("\n")

#  function 2
def math_operations(x,y):
	addition = x+y
	subraction = x-y
	division = x/y
	multiplication = x*y
	return addition,subraction,division,multiplication
	

add , sub , div , multi = math_operations(10,5)
print(add , sub , div , multi)
add , sub , div , multi = math_operations(15,5)
print(add , sub , div , multi)
add , sub , div , multi = math_operations(26,5)
print(add , sub , div , multi)
