#Salary calculator

basic_salary = int(input("Enter your basic salary ; "))

if basic_salary<=20000:
	HRA=basic_salary*(20/100)
	DA=basic_salary*(10/100)
	
	
elif 50000>=basic_salary>20000:
	HRA=basic_salary*(25/100)
	DA=basic_salary*(15/100)
	
elif basic_salary>50000:
	HRA=basic_salary*(30/100)
	DA=basic_salary*(20/100)
	
gross_salary = basic_salary + HRA + DA
print(f"your salary without bonus is {gross_salary}")


print("Time for bonus")
years_worked_in_company = int(input("Enter the years worked in company ; "))

if years_worked_in_company <2:
	print("No bonus")
	final_salary= gross_salary
	
	
elif 2<=years_worked_in_company <=5:
	bonus=5000
	final_salary = gross_salary + bonus
	
	
elif years_worked_in_company >5:
	bonus = 10000
	final_salary = gross_salary + bonus
	
	
print(f"Your final salary according to your years worked is{final_salary}")

