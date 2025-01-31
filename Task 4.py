# Simple Command-Line Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1/2/3/4): "))
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select a valid option.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print(f"The result of addition is: {add(num1, num2)}")
            elif choice == 2:
                print(f"The result of subtraction is: {subtract(num1, num2)}")
            elif choice == 3:
                print(f"The result of multiplication is: {multiply(num1, num2)}")
            elif choice == 4:
                print(f"The result of division is: {divide(num1, num2)}")
            
            next_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break

        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    calculator()