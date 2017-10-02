def demo():
	global value1 #full access of global variable value1
 	value1 = -value1
 	value2 = -20 #a new variable with same name (shadow)
 	print("Inside local scope:", value1, value2, value3)

	value1 = 10
	value2 = 20
	value3 = 30

# first output
print("In the global scope:", value1, value2, value3)

#call demo function
demo() # value1 is changed; value2 and value3 not

print("Back in the global scope", value1, value2, value3) 