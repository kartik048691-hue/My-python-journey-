# Movie ticket calculator

age = int(input("Enter your age ; "))
ticket = int(input("Enter the no. of ticket you want ; "))

if age <=5:
	print("Ticket is free for you ")
	total = 0
	print(f"Your total is {total}$ ; ")
	
elif 5<age<=17:
	print("Price is 120$ per ticket")
	total= ticket*120
	print(f"Your total is {total}$ ")
	
	
elif 18<=age<=59:
	print("Price is 200$ per ticket")
	total= ticket*200
	print(f"Your total is { total}$ ")
	
elif age >=60:
	print("Price is 150$ per ticket")
	total  = ticket*150
	print(f"Your total is { total}$ ")
	
	
if total >= 500:
	discount= (total*(10/100))
	final = total - discount
	print(f"Your final price after discount is {final}$ ")
	
else:
	print(f"Your final price is {total}$ ")
