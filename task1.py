

def calculator():
    print("Welcome to the Python Calculator!")

    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        operation = input("Enter the operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
            print(f"The result is: {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"The result is: {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"The result is: {result}")
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result is: {result}")
        else:
            print("Error: Invalid operation. Please try again.")

        continue_calculation = input("Do you want to perform another calculation? (y/n): ")
        if continue_calculation.lower() != "y":
            break

if __name__ == "__main__":
    calculator()
