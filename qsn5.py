'''Write a program to print multiplication tables from 1 to 5, but stop after the first table is printed for each
number.'''

# Program to print multiplication tables from 1 to 5, stopping after the first table is printed for each number
for i in range(1, 6):  # Loop through numbers from 1 to 5
    print(f"Multiplication Table for {i}:")
    for j in range(1, 11):  # Loop through numbers from 1 to 10
        print(f"{i} x {j} = {i * j}")
    print()  # Print a blank line after each table
