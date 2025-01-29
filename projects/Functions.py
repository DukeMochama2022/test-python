#This project shows the use of functions and object oriented programming
def bank_account(account,name,deposit,branch):
    return{
        'Account':account,
        'Name':name,
        'Deposit':deposit,
        'Branch':branch
    }
    
account=float(input("Enter your account number:"))
name=input("Enter your name: ")
deposit=float(input("Enter amount to deposit: "))
branch=input("Enter your branch:")

customer=bank_account(account,name,deposit,branch)
print(customer)

