# ATM Withdrawal 

Account_balance = float(input("Enter the balance  in your account ; "))
Withdrawal_amount = int(input("Enter the amount you want to withdraw ; "))

if Withdrawal_amount <=0:
	print("Invalid withdrawal amount")
	
elif Withdrawal_amount > Account_balance:
	print("Insufficient balance")
	
elif Withdrawal_amount % 100 != 0:
	print("Amount should be a multiple of 100")
	
else:
	print("Withdrawal successful ")
	print(f"Your amount of {Withdrawal_amount} is successfully withdrawn")
	print(f"Remaining balance is {Account_balance-Withdrawal_amount}")