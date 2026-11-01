# Battle Arena

class fighter:
	def __init__(self , name , health , attack_power ):
		self.name = name 
		self.health = health
		self.attack_power = attack_power	
		
	def attack(self , target):
		target.health= target.health-self.attack_power
		return target.health , self.attack_power 
		
		
class player(fighter):
	def __init__(self ,name , health , attack_power , score ):
		super().__init__(name , health , attack_power )
		self.score = score
		
	def special_attack(self, target):
		target.health -= 40 
		return target.health 	
		
	
class enemy(fighter):
	pass	
	
player1 = player("Thor" , 100 , 25 , 95 )
enemy1 = enemy("Thanos" , 100 , 20 )

is_playing = True
while is_playing:
	print("Choose one option")
	print("1 - attack , 2 - Check status , 3 - Special attack , 4 - Quit")
	choice = int(input("(1, 2 , 3 ,4) ; "))
	print(choice)
	
	if choice ==1:
			player1.attack(enemy1)
			
			
			print(f"{player1.name} attacks {enemy1.name} for {player1.attack_power} damage! , {enemy1.name} has {enemy1.health}HP remaininng ")
			
			if enemy1.health<=0:
				print(f"{player1.name} wins!")
				break
			
			enemy1.attack(player1)
			
			print(f"{enemy1.name} attacks {player1.name} for {enemy1.attack_power} damage! , {player1.name} has {player1.health} HP remaining ")
		
			if player1.health <=0:
				print(f"{enemy1.name} wins!")
				break
				
	
	elif choice ==2:
		print(f"{player1.name} : {player1.health} HP")
		print(f"{enemy1.name} : {enemy1.health} HP")
	
	elif choice ==3:
			player1.special_attack(enemy1)
			print(f"{player1.name} attacks {enemy1.name} for 40 damage! , {enemy1.name} has {enemy1.health}HP remaininng ")
			
			if enemy1.health<=0:
				print(f"{player1.name} wins!")
				break
			
			enemy1.attack(player1)
			
			print(f"{enemy1.name} attacks {player1.name} for {enemy1.attack_power} damage! , {player1.name} has {player1.health} HP remaining ")
		
			if player1.health <=0:
				print(f"{enemy1.name} wins!")
				break
				
		
	
	
	elif choice ==4:
		is_playing = False