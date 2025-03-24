class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero is not allowed."
        else:
            return a / b

print("\n\n----------------Calculator----------------")
calculator = Calculator()
while True:
    print("\nChoose an option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", calculator.add(num1, num2))
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", calculator.subtract(num1, num2))
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", calculator.multiply(num1, num2))
    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", calculator.divide(num1, num2))
    elif choice == '5':
        print("\n\n\n\nExiting...\nCASIO C-T PLUS")
        break
    else:
        print("Invalid choice. Please choose a valid option.")