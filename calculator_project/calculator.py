

class Calculator:
    def add(self,a,b):
        return a + b
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a/b
    def power(self,a,b):
        return a**b
    
class CalculatorApp:
    def __init__(self):
        self.calculator = Calculator()
        self.history = []

    def show_menu(self):
        print("\nSimple Calulator")
        print("----------------")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. view history")
        print("7. Exit")
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter choice (1-7): ")

            if choice == "7":
                print("Thank you for using calculator!")
                break
            elif choice == "6":
                self.show_history()
                continue
            self.perform_operation(choice)

    def show_history(self):
        if not self.history:
            print("No history yet.")
        else:
            print("\nCalculator History:")
            for item in self.history:
                print(item)

    def perform_operation(self,choice):
            num1,num2 = self.get_number()
            if num1 is None:
                return
            try:

                if choice == "1":
                    result = self.calculator.add(num1,num2)
                    expression = f"{num1} + {num2} = {result}"
                elif choice == "2":
                    result = self.calculator.subtract(num1,num2)
                    expression = f"{num1} - {num2} = {result}"
                elif choice == "3":
                    result = self.calculator.multiply(num1,num2)
                    expression = f"{num1} * {num2} = {result}"
                elif choice == "4":
                    result = self.calculator.divide(num1,num2)
                    expression = f"{num1} / {num2} = {result}"
                elif choice == "5":
                    result = self.calculator.power(num1,num2)
                    expression = f"{num1} ** {num2} = {result}"
                else:
                    print("Invalid choice")
                    return
                print("Result: ", result)
                self.history.append(expression)

            except ZeroDivisionError as e:
                print(e)
        
        

    def get_number(self):
        try:
            num1 = float(input("enter first number :"))
            num2 = float(input("enter second number:"))
            return num1,num2
        except ValueError:
            print("invalid number entered!")
            return None, None



if __name__ == "__main__":
    app=CalculatorApp()
    app.run()


