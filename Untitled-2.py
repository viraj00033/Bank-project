import pymongo

# MongoDB Connection Setup
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["BankDB"]
    accounts_col = db["accounts"]
    print("MongoDB successfully connected!")
except Exception as e:
    print("Connection error:", e)

class Bank:
    def openAccount(self, x, y, z):
        self.accno = x
        self.balance = y
        self.name = z

    def deposite(self, money):
        self.balance = self.balance + money
        print("Successfully Deposited! New Balance:", self.balance)

    def withdrawl(self, money):
        if money > self.balance:
            print("Insufficient Balance:")
        else:
            self.balance = self.balance - money
            print("Successfully Withdrawn! New Balance:", self.balance)

    def checkBalance(self):
        print("Account No =", self.accno)
        print("Balance =", self.balance)

cust1 = Bank()
cust2 = Bank()
cust3 = Bank()

# Menu loop with error fixed
i = 1
while i == 1:
    print("\n--- BANK MENU ---")
    print("1. Open Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        acc = int(input("Enter Account Number: "))
        bal = int(input("Enter Initial Balance: "))
        name = input("Enter Name: ")
        cust1.openAccount(acc, bal, name)
        
        # MongoDB me account details save karne ke liye
        try:
            accounts_col.insert_one({"accno": acc, "balance": bal, "name": name})
            print("Account data saved to MongoDB!")
        except Exception as e:
            print("Failed to save to database:", e)
            
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        cust1.deposite(amount)
        
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        cust1.withdrawl(amount)
        
    elif choice == 4:
        cust1.checkBalance()
        
    elif choice == 5:
        break
        
    else:
        print("Wrong choice.....")
        
    i = int(input("Press 1 to continue, press any other key to exit: "))|