# banck sistem
# create account
name = input("please enter your name :")
surname = input("please enter your surname:")
age = input("please enter your age:")
ID_number = input("please enter your ID number:")
# banc sisitem
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")


def deposit():
    amount=float(input("enter an amount which you want to be deposited: "))
    if amount < 0:
        print("is not valid amount")
        return 0
    else:
        return amount    


def withdraw(balance):
    amount = float(input("enter the amount to be withdraw:"))
    if amount > balance:
        print("funds are unsufficient")
        return 0
    elif amount < 0:
        print("amount should be more than 0")  
        return 0  
    else:
        return amount    

def main():
    balance= 0
    is_running = True
    
    while is_running:
        print("1. balamce")
        print("2. deposit")
        print("3. withdraw")
        print("4. exit")

        choose = int(input("enter number between 1-4: "))

        if choose == 1:
            show_balance(balance)
        elif choose == 2:
            balance += deposit()    
        elif choose == 3:
            balance -= withdraw(balance)  
        elif choose == 4:
            is_running= False
        else:
            print("that is wrong choise")    
    print("thank you for visiting out bank and choosing us<33")        
if __name__ == '__main__' :
    main()   

 