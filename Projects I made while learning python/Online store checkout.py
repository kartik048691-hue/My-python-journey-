# Online store  checkout


purchase_amount = int(input("Enter your purchase amount ; "))
is_member = True
is_coupon  = True
is_first_order = False

if is_member and is_coupon:
	discount = purchase_amount*(20/100)
	final_amount = purchase_amount - discount
	
elif is_member and is_first_order:
	discount= purchase_amount*(15/100)
	final_amount =  purchase_amount-discount
	
elif is_coupon or is_first_order:
	discount = purchase_amount*(10/100)
	final_amount = purchase_amount-discount
	
else:
	discount= 0 
	final_amount = purchase_amount - discount
	
print(f"Original amount {purchase_amount}")
print(f"Discount amount {discount}")
print(f"final amount {final_amount}")