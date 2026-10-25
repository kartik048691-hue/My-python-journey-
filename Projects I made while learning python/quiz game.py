# quiz game programm

questions =("How many calories in 1 gm of protein" ,
                      "How many heads in bicep" ,
                      "How many heads in triceps" ,
                      "Muscle targetted by leg raises" )
 

options = (("A . 2 " , "B . 3" , "C . 4" , "D . 9") ,
                   ("A .1  " , "B . 2" , "C .3 " , "D . 69") , 
                   ("A . 21  " , "B . 22" , "C . 2" , "D . 3") , 
                   ("A . Shoulder " , "B . Leg" , "C . abs" , "D . back"))

answers = ("C" , "C" , "D" , "C")
guesses = []
score = 0
question_num = 0

for question  in questions:
	print(question)
	for option in options[question_num]:
		print(option)
		
	guess = input("Enter (A , B , C , D):  ").upper()
	guesses.append(guess)
	if guess == answers[question_num]:
			score +=1
			print("CORRECT")
			
	else:
			print("INCORRECT")
			print(f"{answers[question_num]} is the correct answer")
			
	question_num +=1
	
	
print("______RESULT_____")

print("answer :" , end = "")
for answer in answers:
	print(answer , end = " ")
	
print()

print("guesses: " , end= "")
for guess in guesses:
	print(guess , end = " ")
print()



score = int(score / len(questions)*100)
print(f"Your score is : {score}%")