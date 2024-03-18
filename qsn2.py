#Write a program to iterate through a list and stop when encountering a specific element.

my_list = [3, 7, 1, 5, 9, 2, 4, 8]

stop_element = 5

for element in my_list:
    if element == stop_element:
        break
    print(element)
