stock = {}

while True:
    print("\n Inventory Management System")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Update item quantity")
    print("4. Display inventory")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1" :
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        if name in stock:
            stock[name] += quantity
        else:
            stock[name] = quantity
        print(f"Added {quantity} {name}(s) to the inventory.")

    elif choice == "2" :
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        if name in stock:
            if stock[name] >= quantity:
                stock[name] -= quantity
                print(f"Removed {quantity} {name}(s) to the inventory.")
            else:
                print(f"Not enough {name}(s) in stock to remove {quantity}.")
        else:
            print(f"{name} not found in the inventory.")
            
    elif choice == "3" :
        name = input("Enter item name: ")
        quantity = int(input("Enter new quantity: "))
        if name in stock:
                stock[name] = quantity
                print(f"Updated {name} quantity to {quantity} .")
        else:
            print(f"{name} not found in the inventory.")
                        
    elif choice == "4" :
        print(f"Current Inventory: ")
        for name, quantity in stock.items():
            print(f"{name}: {quantity}")

    elif choice == "5" :
        break
    
    else:
        print("Invalid option. Please choose a valid option.")