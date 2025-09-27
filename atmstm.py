"""ATM STIMULATION USING PYTHON"""
print('Hello guys welcome to the bank portal')

pin = 1234
balance = 1000

print("""
    HEY 
    DO YOU WANT TO LOGIN WITH YOUR ACCOUNT  
       """)
running = True
ent_pin = int(input("Enter Your pin:-"))
while running:
    if (ent_pin == pin):
        print("yahh welcome to the bank portal")
        print("MENU")
        print(""" 
             WHAT DO YOU WANT TO CHECK
            1) CHECK BALANCE
            2) DEPOSITE MONEY
            3) WITHDRAW AMOUNT 
            4) EXIT
            """)
        choice = int (input("enter your choice :"))
        if choice==1:
            print("your account balance is:",balance)
        if choice==2:
            deposite =int(input("Enter how much money do you want to deposite:"))
            balance = balance +deposite
            print("yess ! your account balance is :",balance)
        if choice==3:
            withdraw = int(input("how much money do you want to withdraw : "))
            balance = balance - withdraw
            print("yess ! your account balance is :",balance)
        if choice==4:
            print("Exiting the menu. Goodbye:)")
            running = False         
    else:
        print("Oh your pin is not correct try again")
        running = False
