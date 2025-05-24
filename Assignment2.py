while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if num2 == 0:
            print("Cannot divide by zero. Please try again.")
        else:
            result = num1 / num2
            print(f"{num1} divided by {num2} is {result}")
            break
    except ValueError: 
        print("Invalid input. Please enter a valid number.")