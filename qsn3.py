#Write a program to skip printing even numbers from 1 to 10.

# Program to skip printing even numbers from 1 to 10
for num in range(1, 11):
    if num % 2 != 0:  # Check if the number is odd
        print(num)
