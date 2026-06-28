balance=5000
pin="1234"
count=0
history=[]
attempt=0
while attempt<3:
    
    code=input("enter your pin :")
    if code==pin:
        break
    attempt+=1
    if attempt==3:
        print("card blocked")

if code==pin:
    while(True):
        print("====ATM====")
        print("1.check balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.History")
        print("5.Exit")
        choice=input("enter your choice")
        if choice=="1":
            print("current balance:",balance)
        elif choice=="2":
            Deposit=int(input("enter amount:"))
            balance=balance+Deposit
            history.append(f"Deposit  {Deposit}|Balance {balance}")
            count+=1
            print("successfully add!")
        elif choice=="3":
            withdraw=int(input("enter ammount"))
            if withdraw<=balance:
                
            
                balance=balance-withdraw
                history.append(f"withdraw {withdraw}|Balance {balance}")
                count+=1
                
                print("successfully withdraw")
            else:
                print("insufficient balance") 
        elif choice=="4":
            if len(history)==0:
                
                print("no transaction history")
            else:
                for item in history:
                    print(item)
        elif choice=="5":
            print("thanks for using atm")
            print("total transaction :",count)
                
            break
        else:
            print("invalid choice")
else:
    print("wrong pin!")