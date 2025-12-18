class Account:
    def __init__(self,number,name,balance):
        self.__name = name
        self.__number = number
        self.__balance = balance

   
    def deposit(self):
        while True:
            try:
                deposit_amount = int(input("Enter amount to deposit: "))
            except ValueError:
                print("Please enter a valid integer amount.")
                continue
            if deposit_amount < 2:
                print("Minimum amount to be deposited is $2")
                continue
            self.__balance += deposit_amount
            print(f"You have successfully deposited ${deposit_amount} into your account")
            print(f"New balance: ${self.__balance}")
            break
            
    def withdraw(self):
        if self.__balance <= 0:
            print("Cannot withdraw due to insufficient funds")
            return
        while True:
            try:
                withdraw_amount = int(input("Enter amount to withdraw: "))
            except ValueError:
                print("Please enter a valid integer amount.")
                continue
            if withdraw_amount <= 0:
                print("Enter an amount greater than zero.")
                continue
            if withdraw_amount > self.__balance:
                print("You don't have enough funds.")
                continue
            self.__balance -= withdraw_amount
            print(f"${withdraw_amount} has been withdrawn from your account")
            print(f"New balance: ${self.__balance}")
            break

    def return_balance(self):
        print(f"Your balance is ${self.__balance}")
   
    def account_info(self):
        print(f"Account number:{self.__number}")
        print(f"Account name:{self.__name}")
        print(f"Account balance:${self.__balance}")

if __name__ == "__main__":
    import random
    
    name = input("Enter your name: ").strip()
    account_number = random.randint(10000, 99999)
    opening_balance = 50
    
    acc = Account(account_number, name, opening_balance)
    print(f"\nAccount created! Your account number is: {account_number}")
    
    while True:
        print("\n1) Deposit\n2) Withdraw\n3) Balance\n4) Account Info\n5) Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            acc.deposit()
        elif choice == "2":
            acc.withdraw()
        elif choice == "3":
            acc.return_balance()
        elif choice == "4":
            acc.account_info()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")
       