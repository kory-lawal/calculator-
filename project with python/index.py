import sys
# Function to perform addition
def add(x, y):
    return x + y
# Function to perform multiplication
def multiply(x, y):
    return x * y
# Function to perform subtraction
def subtract(x, y):
    return x - y
# Function to perform dividsion
def divide(x, y):
    try: 
        return x // y
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
        print("Exiting the program")
        return None
while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
    except ValueError:
        print("Error: invaild input")
        continue

    if choice == 5:
        print("Exiting this program")
        break

    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the secord number: "))

    except ValueError:
        print("Error: invaild input")
        continue


    if choice == 1:
        print(f"The result for {x} + {y} = {add(x, y)}")
    elif choice == 2:
        print(f"The result for {x} - {y} = {subtract(x, y)}")
    elif choice == 3:
        print(f"The result for {x} * {y} = {multiply(x, y)}")
    elif choice == 4:
        print(f"The result for {x} // {y} = {divide(x, y)}")
    else:
        print("Error: invaild input")