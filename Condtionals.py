# Problem: Write a Python program that asks the user for a number and checks whether it is odd or even. Print "Odd" or "Even" accordingly.
# Write a Python program that takes a number as input and prints whether the number is positive, negative, or zero.
# Write a program that takes a student's marks as input and prints their grade based on the following scale:
# 90 and above: A
# 80 to 89: B
# 70 to 79: C
# 60 to 69: D
# Below 60: F
# Write a Python program that takes three numbers as input and prints the largest of the three.
# Write a Python program that takes a letter as input and checks whether it is a vowel or a consonant.
#  Write a Python program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input, and then perform the appropriate operation.



#6
num1 =  float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

print("Result:", result)