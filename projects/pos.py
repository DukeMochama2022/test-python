def display_menu():
    print("=== Menu===")
    print("1. Sell item")
    print("2. Add item")
    print("3. List items")
    print("4. List categories")
    print("5. Calculate total")
    print("6. Process payment")
    print("7. List debtors")
    print("8. Exit")

def sell_item(inventory,cart):
    product_name=input("Enter product name: ")
    if product_name not in inventory:
        print("Product not found!")
        return
    quantity_needed=int(input(f'Enter quantiry needed for {product_name}: '))
    cart.append({'name':product_name,'quantity':quantity_needed})
    print(f'Added {quantity_needed} units of {product_name} to cart')   

def add_item(inventory):
    product_name=input("Enter product name :")
    if product_name in inventory:
        print("Product already exists.")
        return    
    else:
        price=float(input("Enter price for the item:"))
        category=input("Enter category for the item: ")
        inventory[product_name]={"price":price,"category":category}
        print(f"Added {product_name} to inventory")  
def list_items(inventory):
    print('===Inventory===')        
    for product_name, details in inventory.items():
        print(f"{product_name}: ${details['price']},Category:{details['category']}")

def list_categories(inventory):
    categories=set(details['category'] for details in inventory.values())
    print("===Categories===")
    for category in categories:
        print(category)
def calculate_total(inventory,cart):
    total=sum(inventory[item["name"]]["price"] * item["quantity"] for item in cart)  
    print(f"Total: ${total:.2f}")      

def process_payment(sales, cart, debts, inventory):
    if not cart:
        print("Cart is empty. Please add items to the cart first.")
        return
    total = sum(inventory[item["name"]]["price"] * item["quantity"] for item in cart)
    payment = float(input("Enter payment amount: "))
    if payment <= 0:
        print("Payment must be a positive value.")
        return
    
    customer_name = input("Enter customer name: ")
    
    if payment < total:
        debt = total - payment
        debts[customer_name] = debts.get(customer_name, 0) + debt
        print(f"Insufficient payment. Added ${debt:.2f} to {customer_name}'s debt.")
        sale = {"items": cart.copy(), "total": total, "customer_name": customer_name, "debt": debt}
    else:
        change = payment - total
        print(f"Payment successful. Change: ${change:.2f}" if change > 0 else "Payment successful.")
        sale = {"items": cart.copy(), "total": total, "customer_name": customer_name}
    
    sales.append(sale)
    cart.clear()

def list_debtors(debts):
    print("===Debtors===")
    for customer, debt in debts.items():
        print(f"{customer}: ${debt:.2f}")     

def pos_system():
    inventory={
        "apple":{'price':1.00,'category':'fruit'},
        "banana":{'price':0.50,'category':'fruit'},
        "orange":{'price':0.75,'category':'fruit'},
    }

    cart=[]
    sales =[]
    debts={}
    while True:
        display_menu()
        choice=input('Enter your choice!')
        if choice =='1':
            sell_item(inventory,cart)
        elif choice == '2':
            add_item(inventory)    
        elif choice == '3':
            list_items(inventory)
        elif choice == '4':
            list_categories(inventory)
        elif choice == '5':
            calculate_total(inventory,cart)
        elif choice == '6':
            process_payment(sales,cart,debts,inventory)
        elif choice == '7':
            list_debtors(debts)
        elif choice == "8":
            print("Exiting program")   
            break                 
        else:
            print("Invalid choice. Pleasetry again")    
#main program            
pos_system()    

