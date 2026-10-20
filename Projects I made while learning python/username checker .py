#username checker



name = input("Enter your username ;")


if len(name) <5 or len(name)>12 :
	print("Username must be between 5 and 12 characters")
	
elif name.find(" ")  != -1:
	print("Usename should not contain space") 
	
elif   not name[0].isalpha():
	print("Username first character must be a letter")
	
else:
	name = name.lower()
	print("Username accepted")
	print(f"Your user name is ; {name}")