accounts=[]
class Banka:
    def __init__(self,name,no,balance):
        self.name=name
        self.no=no
        self.balance=balance
    def menu():
        print("1-Create Account")
        print("2-Login Account")
        print("3-Exit")
    def account_menu():
        print("1-deposit")
        print("2-withdraw")
        print("3-show balance")
        print("4-Close Account")
        print("5-Exit")
    def createaccount():
        name=input("Enter your name:")
        no=input("Enter your account number:")
        balance=int(input("Enter your balance:"))
        new_account=Banka(name,no,balance)
        accounts.append(new_account)
        print("Account created successfully!")
    def login():
        no=input("Enter your account number:")
        for account in accounts:
            if account.no==no:
                print("Login successful!")
                while True:
                    Banka.account_menu()
                    choice=int(input("Enter your choice:"))
                    if choice==1:
                        amount=int(input("Enter amount to deposit:"))
                        account.balance+=amount
                        print("Amount deposited successfully!")
                    elif choice==2:
                        amount=int(input("Enter amount to withdraw:"))
                        if amount>account.balance:
                            print("Insufficient balance!")
                        else:
                            account.balance-=amount
                            print("Amount withdrawn successfully!")
                    elif choice==3:
                        print(f"Your balance is: {account.balance}")
                    elif choice==4:
                        accounts.remove(account)
                        print("Account closed successfully!")
                        break
                    elif choice==5:
                        break
                    else:
                        print("Invalid choice!")
                return
        print("Account not found!")

while True:
    Banka.menu()
    choice=int(input("Enter your choice:"))
    if choice==1:
        Banka.createaccount()
    elif choice==2:
        Banka.login()
    elif choice==3:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
