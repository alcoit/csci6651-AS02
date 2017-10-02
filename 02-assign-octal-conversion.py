
dec=100
input=dec
base=8
output=""
while input is not 0:
	remainder=(input%base)
	print("Remainder is: ", (remainder))
	output = str(remainder)+output #pre-pend to the string
	
	input=(input//base)
	print("Input reduced to: ", (input))

print(output)
print('Decimal {} converts to octal {}.'.format(dec,output))
