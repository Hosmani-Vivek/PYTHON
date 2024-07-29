password=1234
balance=1000
upassword=int(input("enter the password"))
if password==upassword:
    option=int(input("select 1 for withdraw / 2 for deposit"))
    if option==1:
        withdraw=int(input("enter withdraw amount"))
        if withdraw>balance:
             print("balance is low than entered ampount")
        else:
             balance-=withdraw
             print("remaining balance is",balance)
    if option==2:
        deposit=int(input("enter the deposit amount"))
        balance+=deposit
        print("deposit successful")
        print("balance is ", balance)
    else:
         print("wrong options")

else:
    print("password is wrong")

print("thanks for using")
        
