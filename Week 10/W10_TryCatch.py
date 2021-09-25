while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("Invalid number. Enter again...")
