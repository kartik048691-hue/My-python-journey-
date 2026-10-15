# Password checker

age = int(input("Enter your age  ; "))
password = input("Enter the password ; ")

if age >=18 and password =="python123":
	print("Access granted")
	
elif age <18:
	print("You are too young")
	
else:
	print("Wrong password")
