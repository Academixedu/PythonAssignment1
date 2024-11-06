# Write a Python program to find the sum of the first n natural numbers, where n is provided by the user.
# Write a Python program to print the multiplication table of a number entered by the user, up to 10.
# Write a Python program that prints all even numbers between 1 and n, where n is provided by the user.
# Write a Python program to print numbers from n to 1, where n is provided by the user.


def sum_of_natural_numbers(n):
    return n * (n + 1) // 2
try:
    n = int(input("Enter a positive integer n: "))
    if n < 1:
        print("Please enter a positive integer greater than 0.")
    else:
        total_sum = sum_of_natural_numbers(n)
        print(f"The sum of the first {n} natural numbers is: {total_sum}")
except ValueError:
    print("Please enter a valid integer.")

    #

def multiplication_table(num):
    print(f"Multiplication table for {num}:")
    for i in range(1, 11):  
        result = num * i
        print(f"{num} x {i} = {result}")
try:
    number = int(input("Enter a number to print its multiplication table: "))
    multiplication_table(number)
except ValueError:
    print("Please enter a valid integer.")

    #

def print_even_numbers(n):
    print(f"Even numbers between 1 and {n}:")
    for i in range(2, n + 1, 2): 
        print(i)
try:
    n = int(input("Enter a positive integer n: "))
    if n < 1:
        print("Please enter a positive integer greater than 0.")
    else:
       
        print_even_numbers(n)
except ValueError:
    print("Please enter a valid integer.")

    #

def print_numbers_reverse(n):
    print(f"Numbers from {n} to 1:")
    for i in range(n, 0, -1):  
        print(i)
try:
    n = int(input("Enter a positive integer n: "))
    if n < 1:
        print("Please enter a positive integer greater than 0.")
    else:
       print_numbers_reverse(n)
except ValueError:
    print("Please enter a valid integer.")






    
    
