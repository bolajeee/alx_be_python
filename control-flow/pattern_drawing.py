# This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).
length = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through each row
while row < length:
    # Use a for loop to print asterisks side by side
    for col in range(length):
        print("*", end="")
    # Move to the next line after printing a row
    print()
    # Increment the row counter
    row += 1