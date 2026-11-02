#Password strength checker


password = input("Enter a strong password : ")

if len(password)>= 8:
	print("length : Good")
	
else:
	print(" Length : Too short")

has_upper = False		
for letter in password:
	if letter.isupper():
		has_upper = True
if has_upper:
	print("Uppercase : Found")
	
else:
	print("Uppercase not found")
	
has_lower = False
for letter in password:
	if letter.islower():
		has_lower = True
if has_lower:
	print("Lowercase : found")
	
else:
	print("Lowercase : Not found")
	
has_digit = False
for digit in password:
	if digit.isdigit():
		has_digit = True
if has_digit:
	print("Digit = Found")
	
else:
	print("Digit : Not Found")
	
has_special = False

for special in password:
	if not special.isalnum() and not special.isspace():
		has_special = True
		
if has_special:
	print("Special  character : Found")
else:
	print("Special character : not found")
	
score = 0
if len(password)>= 8:
	score += 1
if has_upper:
	score += 1
if has_lower:
	score +=1
if has_digit:
	score+=1
if has_special:
	score +=1
	
if  score ==0 or score == 1 or score ==2:
	print("Weak password")
elif score ==3 or score == 4:
	print("Medium ")
else:
	print("Strong")

print(f" Strength score :  {score}/5") 