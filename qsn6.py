# Program to skip printing even numbers using a while loop
num = 1
while num <= 10:
    if num % 2 != 0:  # Check if the number is odd
        print(num)
    num += 1
