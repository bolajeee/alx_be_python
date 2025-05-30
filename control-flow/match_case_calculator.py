# This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division).
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

retry = True


while retry:
    operation = input("Choose the operation (+, -, *, /): ")
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Error: Invalid operation. Please choose +, -, *, or /.")
            retry = input("Do you want to try again? (yes/no):. ").lower()
            if retry == "yes":
                print("Restarting the calculator...")
                # Here you could call the script again or loop back to the start
            else:
                print("Exiting the calculator. Goodbye!")
                break

print("Thank you for using the calculator!")
