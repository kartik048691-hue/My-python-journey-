# python compound calculator 
 
 
while principle <= 0:
	principle = float(input("Enter the principle amount; "))
	if principle <= 0:
		print("principle value should not be less than or equal to zero")
		
	else:
		print(f"Your principle amount is {principle}")
		
while rate <= 0:
	rate = float(input("Enter the interest rate; "))
	if rate <= 0:
		print("Interest rate  should not be less than or equal to zero")
		
	else:
		print(f"Your interest rate  is {rate}")
		
				
						
while time <= 0:
	time = float(input("Enter the time; "))
	if time <= 0:
		print("Time should not be less than or equal to zero")
		
	else:
		print(f"Your time period is {time}")	
		
Total_amount = principle * pow((1 + rate/100 ) , time)	
	
	
print(f"Ypur total amount in {time} years will be ${Total_amount: .2f})")
	
	
	