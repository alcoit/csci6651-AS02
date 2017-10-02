
dec=255
input=dec
base=20
output=""
hex=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
if base > 16:
		print('Wrong base')
		exit()
while input is not 0:
	remainder=(input%base)
	if remainder > 9:
		remainder=hex[remainder]
	print("Remainder is: ", (remainder))
	output = str(remainder)+output #pre-pend to the string
	
	input=(input//base)
	print("Input reduced to: ", (input))

print(output)
print('Decimal {} converts to base {} as {}.'.format(dec,base,output))
