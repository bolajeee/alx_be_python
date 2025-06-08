def perform_operation(num1, num2, operation):
    match operation:
        case _ if operation == "add":
            result = num1 + num2
            print(f"The result of adding {num1} and {num2} is: {result}")
        case _ if operation == "subtract":
            result = num1 - num2
            print(f"The result of subtracting {num2} from {num1} is: {result}")
        case _ if operation == "multiply":
            result = num1 * num2
            print(f"The result of multiplying {num1} and {num2} is: {result}")
        case _ if operation == "divide":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                result = None
            else:
                result = num1 / num2
                print(f"The result of dividing {num1} by {num2} is: {result}")

    return result

