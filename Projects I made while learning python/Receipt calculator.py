# Receipt Generator

item_name= input("Enter the name of the item ; ")
item_price =  float(input("Enter the price of the item ; "))
quantity = int(input("Enter the quantity ; "))

subtotal= item_price*quantity
print(f"{ subtotal = subtotal:,.2f}")

if subtotal >= 5000:
	discount = subtotal*(15/100)
	final_price = subtotal-discount
	
elif subtotal >= 2000:
	discount= subtotal*(10/100)
	final_price= subtotal-discount
	
else:
	discount = 0
	final_price= subtotal-discount
	
print(f" Discount = {discount :,.2f}")
print(f" Final price = {final_price :,.2f}")
	
