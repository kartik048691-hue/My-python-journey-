# Driving Licence Eligibility 

age = int(input("Enter your age "))
driving_test = input("Have you passed the driving test (Yes/No) ; ")
learner_license = input("Do you  have a valid learning licence (Yes/No) ; ")

if age >=18 and driving_test =="Yes" and learner_license =="Yes":
	print("Congratulations! You are eligible for driving license")
	
elif age <18:
	print("You must be at least 18 ")
	
elif driving_test == "No":
	print("You need to pass the driving test ")
	
elif  learner_license =="No":
	print("You need a valid learner license")
	
