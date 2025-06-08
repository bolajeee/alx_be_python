from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the current date and time
    print("Current date and time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))  # User input for number of days
        future_date = datetime.now() + timedelta(days=days_to_add)  # Calculate the future date
        print("Future date:", future_date.strftime("%Y-%m-%d"))  # Format and print the future date
    except ValueError:
        print("Invalid input. Please enter a valid integer.")  # Handle invalid input

def main():
    display_current_datetime()  # Display the current date and time
    calculate_future_date()  # Calculate and display the future date

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
