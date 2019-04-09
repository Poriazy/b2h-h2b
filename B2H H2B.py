while True:
	user_input = input("please enter a number: need help? type -h\n")

	if 'b' in user_input:
		# calculate hex
		bin_user_input = user_input.replace("0b","")
		print("\t", user_input, "in hex is", hex(int(bin_user_input, 2)))
		user_input=""

	elif 'x' in user_input:
		# calculate bin
		hex_user_input = user_input.replace("0x","")
		print("\t", user_input, "in hex is", bin(int(hex_user_input, 16))[2:])
		user_input=""

	elif user_input == "-h":
		# show help
		print("to convert binary to hexadecimal enter 0b in front of your number like 0b0101")
		print("to convert binary to hexadecimal enter 0x in front of your number like 0x0A")
		print("enter q to exit")
		print("\n")
		user_input=""

	elif user_input == 'q':
		# exit
		exit()
	else: 
		print("woops! please use help")
	
	