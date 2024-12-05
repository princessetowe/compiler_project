
def main():
    global balance
    balance = 20000

    while True:
        print("(1) Deposit\n(2) Withdraw\n(3) Exit")
        choice = input("What would you like to do?")

        if choice == "1":
            amount = float(input("Enter amount:"))
            dep(amount)
            print("New Balance:", balance)  
    
        elif choice == "2":
            amount = float(input("Enter amount:"))
            
            if amount > balance:
                print("Insufficient balance")
                
            else:
                wit(amount)
                print("New Balance:", balance)

        elif choice == "3":
            print("Thank you for banking with us")
            print("Balance:", balance)
            break
        
        else:
            print("Invalid input")
            print("Balance:", balance)

def dep(n):
    global balance
    balance += n
    
def wit(n):
    global balance
    balance -= n
    
if __name__ == "__main__":
    main()

