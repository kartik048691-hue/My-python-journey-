# calculator 

operator = input("select the operator ( + , - , * , /)  :  ")

num1 = float(input(" select first number : "))
num2 = float(input("select second number : "))

if operator == "+":
	result = (num1 + num2)
	print(round(result , 3))
	
elif operator == "-":
	result = (num1 - num2)
	print(round(result , 3))

		
elif operator == "*":
	result = (num1 * num2)
	print(round(result , 3 ))

						
elif operator == "/":
	result = (num1 / num2)
	print(round(result  , 3))
	
else:
       print(f"{operator} is not a valid operator ")																	
																		