# Number analyzer


number = int(input("enter a number of your choice ; "))

even_counter = 0 
odd_counter = 0

for n in range(1 , number +1):
	if n % 2 ==0:
		print(f" {n} : even")
		even_counter += 1
		
	else:
		print(f" {n} : odd")
		odd_counter += 1
	
print(f"no. of evens :{even_counter} ")
print( f"no. of odds :  {odd_counter}")
		