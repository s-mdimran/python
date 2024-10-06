balance = 0
toss = 1
while toss:
    print("Men: 1.Check Balance 2.Deposit, 3.Withdraw 4.Exit")
    choice = int(input("Enter the value 1-4: "))
    if choice ==1:
        print("ur netbalance Rs: ",balance)
    elif choice == 2:
        amt = int(input("Enter the Deposit Amount: "))
        if amt<=0:
            print("Enter valid amount...")
        else:
            balance+=amt
            print("Ut net balance is: ",balance)
    
    elif choice ==3:
        withdraw_amt = int(input("How much do you want withdraw?.."))
        if withdraw_amt<=0:
            print("Enter valid amount: ")
        else:
            if withdraw_amt > balance:
                print("Insufficient funds")
            else:
                balance -= withdraw_amt
                print("Ur Netbalance is Rs:", balance)
    elif choice == 4:
        toss = 0
        print("Thanks for banking withh us....")