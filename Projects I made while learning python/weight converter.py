# weight convertor 

weight = float(input("Enter your weight :  "))

unit = (input("Kilogram or Pound  (Type K or L ) : "))

if unit == "K":
	weight = weight * 2.205
	unit = "Lbs"
	print(f"Your weight in pound is {round(weight  , 1 )} {unit}")
	
elif unit == "L":
	weight = weight/2.205
	unit = "Kg"
	print(f"Your weight in Kilogram is {round(weight  , 1)} {unit}") 	
	
else:
	print(f"{unit} is not valid")