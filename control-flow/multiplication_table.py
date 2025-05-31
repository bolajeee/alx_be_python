# This program generates a multiplication table for a given number.
number = input("Enter a number to see its multiplication table: ")

for i in range(1, 11):
    result = i * int(number)
    print(f"{number} x {i} = {result}")

print("Multiplication table completed.")