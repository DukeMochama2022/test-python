accounts={}

def create_account():
    try:
        account_number=int(input("Enter your account number"))
        if account_number not in accounts:
            name=input('Enter your name:')
            initial_deposit=float(input('Enter initial deposit amount:'))
            accounts[account_number]={'name':name,'balance':initial_deposit}
            print("Account created successfully.")
        else:
            print("Account already exists.")    

    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def deposit():
    try:
        account_number=int(input('Enter your account number'))
        if account_number in accounts:
            amount=float(input('Enter amount:'))
            accounts[account_number]['balance']+=amount
            print('Deposit was successiful. Account balance is:',accounts[account_number]['balance'])
        else:
            print('Account not found')
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def widthdraw():
    try:
        account_number=int(input('Enter your account number:'))
        if account_number in accounts:
            amount=float(input("Enter amount to withdraw:"))
            if accounts[account_number]['balance']>=amount:
                accounts[account_number]['balance']-=amount
                print('Widthraw was successiful!')
            else:
                print('Insufficient balance.')
        else:
            print('Account not found.')
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")    

def transfer():
    try:
        from_account=int(input('Enter your account number.'))
        to_account=int(input('Enter recipients account number'))

        if from_account in accounts and to_account in accounts:
            amount=float(input('Enter amount to transfer:'))
            if accounts[from_account]['balance']>=amount:
                accounts[from_account]['balance']-=amount
                accounts[to_account]['balance']+=amount
                print('Tranfer successiful')
                print("New balance is :",accounts[from_account]['balance'])
            else:
                print('Insufficient balance.')
        else:
            print('Account Not Found')
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def check_balance():
    try:
        account_number=int(input("Enter your account number:"))
        if account_number in accounts:
            account_balance=accounts[account_number]['balance']
            print('Your balance is: ', account_balance)
        else:
            print("Invalid Account.")   
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")    

def account_details():
    try:

        account_number=int(input("Enter account number:"))
        if account_number  in accounts:
            account=accounts[account_number]
            print('\nAccount Details')
            print(f'Account Number : {account_number}')
            print(f"Account name : {account['name']}")
            print(f"Balance : {account['balance']}")
        else:
            print("Invalid Account Number.")    
    except ValueError:
        print("Invalid input. Please enter a valid account number.") 

while True:
    print('\n Bank Management system')                    
    print('1. Create Account')                    
    print('2. Deposit')                    
    print('3. Withdraw')                    
    print('4. Transfer')
    print('5. Balance')
    print('6. Details')
    print('7. Exit')

    choice=input("Enter your choice:")

    if choice=='1':
        create_account()

    elif choice == '2':
        deposit()

    elif choice =='3':
        widthdraw()

    elif choice == '4':
        transfer()

    elif choice == '5':
        check_balance()

    elif choice == '6':
        account_details() 

    elif choice == '7':
        print('Exiting program')
        break    
    else:
        print("Invalid choice. Please try again")


                