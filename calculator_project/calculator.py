
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b
def power(a,b):
    return a**b

while True:
    print("\nSimple Calulator")
    print("----------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "6":
        print("Thank you for using calculator!")
        break

    try:
        num1 = float(input("enter first number :"))
        num2 = float(input("enter second number:"))
    except ValueError:
        print("invalid number entered!")
        continue

    if choice == "1":
        print("Result: ", add(num1,num2))
    elif choice == "2":
        print("Result: ", subtract(num1,num2))
    elif choice == "3":
        print("Result: ", multiply(num1,num2))
    elif choice == "4":
        print("Result: ", divide(num1,num2))
    elif choice == "5":
        print("Result: ", power(num1,num2))
    else:
        print("Invalid choice")
