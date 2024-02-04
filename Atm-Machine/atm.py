class Account:
    def __init__(self, balance):
        self.balance = balance
       
    def check_balance(self):
        return f"Your account currently has balance of rupess {self.balance}"
    
    def withdraw_cash(self , amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            return f"Withdrawal successful. Remaining Balance: ${self.balance}"
        else:
            return f"Insufficient fund or invalid entered amount"
        
    def deposit_cash(self , amount):
        if amount > 0 :
            self.balance = self.balance + amount
            return f"Successfully deposited and now you balance is ${self.balance}"
        else:
            return 'Invalid deposited amount'


def main():
    account = Account(2000)
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
           check_balance_res = account.check_balance()
           print(check_balance_res)
        elif choice == "2":
           withdraw_res =  account.withdraw_cash(1000)
           print(withdraw_res)
        elif choice == "3":
            deposit_res = account.deposit_cash(3000)
            print(deposit_res)
        elif choice == "4":
            print("Thank you for using our ATM")
            break
        else:
            print('Invalid choice')

if __name__ == "__main__":
    main()            