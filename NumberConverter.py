#Number Converter

number=int(input('Type a number:\n'))

converter=int(input('Enter 1 to convert the number to binary, 2 to octal, and 3 to hexadecimal:\n'))

if converter == 1:
	number_converted=bin(number)
	print(number_converted)
	
elif converter == 2:
	number_converted=oct(number)
	print(number_converted)
	
elif converter == 3:
	number_converted=hex(number)
	print(number_converted)
	
else:
	print('Invalid option!')
	
