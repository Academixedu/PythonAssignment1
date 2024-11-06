# Write a Python program that takes two numbers from the user and performs addition, subtraction, multiplication, and division. Display the results for each operation.
#  Write a Python program to calculate the remainder and the quotient of two numbers. Quotient Should be an Integer
# Given a number, write a program that calculates its square and cube.
# Start with a variable x = 10. Use assignment operators to increment x by 5, multiply it by 3, and subtract 4. Print the final value of x.
# Write a Python program that takes a number from the user and doubles it using the assignment operator.
# Write a Python program to find the bitwise AND, OR, and XOR of two numbers.
# Write a program to left shift a number by 2 positions and right shift it by 3 positions. Display both results.
# Write a Python program that takes a number, adds 7, multiplies it by 3, divides by 2, and prints the result.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

print("\nResults:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")

#

num1 = int(input("Enter the dividend (numerator): "))
num2 = int(input("Enter the divisor (denominator): "))

if num2 != 0:
    quotient = num1 // num2  
    remainder = num1 % num2   

    print("\nResults:")
    print(f"Quotient (integer division): {num1} // {num2} = {quotient}")
    print(f"Remainder: {num1} % {num2} = {remainder}")
else:
    print("Error: Division by zero is not allowed.")

    #

num = float(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("\nResults:")
print(f"Square of {num} = {square}")
print(f"Cube of {num} = {cube}")

#

x = 10

x += 5

x *= 3

x -= 4

print("The final value of x is:", x)

#


num = float(input("Enter a number: "))

num *= 2

print("The doubled value is:", num)

#

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

bitwise_and = num1 & num2
bitwise_or = num1 | num2
bitwise_xor = num1 ^ num2

print("\nResults:")
print(f"Bitwise AND of {num1} and {num2} = {bitwise_and}")
print(f"Bitwise OR of {num1} and {num2} = {bitwise_or}")
print(f"Bitwise XOR of {num1} and {num2} = {bitwise_xor}")

#

number = int(input("Enter a number: "))

left_shifted = number << 2

right_shifted = number >> 3

print("Original number:", number)
print("Left shifted by 2 positions:", left_shifted)
print("Right shifted by 3 positions:", right_shifted)


#

num = float(input("Enter a number: "))
result = ((num + 7) * 3) / 2

print("The result is:", result)