# Delivery fee calculator

order_amount =  int(input("Enter your order amount ; "))

is_member= True

if order_amount >= 1000:
	delivery =0
	final_amount = order_amount+delivery
	
elif order_amount <1000:
	delivery = 50 if is_member else 100
	final_amount = order_amount + delivery
	
print(f"order amount = {order_amount}")
print(f"Delivery charges = {delivery}")
print(f"final amount = {final_amount}")