def number_converter(*args):
	items=len(args)
	base=args[0]
	mylist=['base='+str(base)]
#	print(base)

	for count in range(1, len(args)):
#	for count, thing in enumerate(args): 	#thing is the element referenced by the index
											#count is how many arguments passed to the function
#		args[0] #the new base
#		args[1] #and so on, numbers to convert
#		x=count+1 #we'll skip the calculation for the first paramater, count=0, the base 
		x=count
		dec=args[x]		#decimal to convert, parameters 1, 2, etc
#		print(dec)
		input=dec	#set input to the decimal value to convert
		output=""	#output string based in the given base (first parameter)
		# hex table for conversions with alpha characters
		hex=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

		if input==0:	#no need to convert output=0 when input=0
			output=input
	
		if base > 16 or base < 2:
			print('Wrong base') #calculate 'Wrong base' if base LT 2 or GT 16
			exit() #and exit
			
		if '.' in str(input) or str(input).isalpha():
#			print('NA') #we don't like bogus answers
			mylist.append('NA')
			continue
			
		while input is not 0:
#			print(input)
#			print(base)
			remainder=(input%base) #get the modulus (the remainder)
			
#			print("Remainder is: ", (remainder))
			if remainder > 9: #if remainder is GT 9, convert to alpha
				remainder=hex[remainder]

#			print("Remainder is: ", (remainder))
			output = str(remainder)+output #pre-pend and build the output string 
	
			input=(input//base) #double-division and reduce to prepare for the next calculation 
#			print("Input reduced to: ", (input))

		mylist.append(output)
	print(mylist)
#		print('Decimal {} converts to base {} as {}.'.format(dec,base,output))
		
		
#number_converter(2, 10, 100, 255)
#number_converter(2, 5, 10, 3)
#number_converter(8, 5, 10)
#number_converter(17, 5, 10)
# number_converter(16, 15, 40, 3.5)
number_converter(16, 15, 3.5, 40, 2.5)