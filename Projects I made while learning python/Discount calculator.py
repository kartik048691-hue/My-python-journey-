# Discount Calculator

total_purchase_amount= float(input("Enter the purchase amount ; "))
member = input("Are you a member of our mall (Yes/No) ; ")

if  total_purchase_amount >= 5000 and member == "Yes":
     discount=total_purchase_amount*(20/100)
     final_amount= total_purchase_amount- discount
     
     
elif total_purchase_amount >= 5000 and member == "No":
     discount=total_purchase_amount*(10/100)
     final_amount= total_purchase_amount- discount
     
elif 2000 <= total_purchase_amount<5000  and member == "Yes":
     discount=total_purchase_amount*(10/100)
     final_amount= total_purchase_amount- discount
     
elif 2000<= total_purchase_amount<5000 and member == "No":
     discount=total_purchase_amount*(5/100)
     final_amount= total_purchase_amount- discount
     
elif total_purchase_amount < 2000:
     discount = 0
     final_amount= total_purchase_amount

     
print(f"Your total amount was {total_purchase_amount}")
print(f"your discount was {discount} ")
print(f"The amount you need to pay is {final_amount}")     
