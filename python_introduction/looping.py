#This script create a pattern using nested loops
rows = 5

for i in range(1, rows + 1):
    #print spaces
    for space in range(rows - i):
        print("", end=" ")

    #print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()  # Move to the next line after each row
    
