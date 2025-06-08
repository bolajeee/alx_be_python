# This function performs basic arithmetic operations based on the provided operation type.
def perform_operation(num1, num2, operation):
    result = None  # Default to None in case of error or unsupported operation

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
            elif num2 != 0:  # This is where we use `elif`
                result = num1 / num2
                print(f"The result of dividing {num1} by {num2} is: {result}")
        case _:
            print(f"Error: Unsupported operation '{operation}'")

    return result
