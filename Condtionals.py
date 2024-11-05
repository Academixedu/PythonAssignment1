# Problem: Write a Python program that asks the user for a number and checks whether it is odd or even. Print "Odd" or "Even" accordingly.
# Write a Python program that takes a number as input and prints whether the number is positive, negative, or zero.
# Write a program that takes a student's marks as input and prints their grade based on the following scale:
# 90 and above: A
# 80 to 89: B
# 70 to 79: C
# 60 to 69: D
 # Write a Python program that takes three numbers as input and prints the largest of the three.
# Write a Python program that takes a letter as input and checks whether it is a vowel or a consonant.
#  Write a Python program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input, and then perform the appropriate operation.


number = int(input("Please enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#

def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."
try:
    user_input = float(input("Enter a number: "))
    result = check_number(user_input)
    print(result)
except ValueError:
    print("Invalid input! Please enter a valid number.")

#

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "F"
try:
    student_marks = float(input("Enter the student's marks (0-100): "))
    

    if 0 <= student_marks <= 100:
        grade = calculate_grade(student_marks)
        print(f"The student's grade is: {grade}")
    else:
        print("Please enter marks in the range of 0 to 100.")
except ValueError:
    print("Invalid input! Please enter a valid number.")

#


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "F"

#

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))

    largest = find_largest(number1, number2, number3)
    print(f"The largest number among {number1}, {number2}, and {number3} is: {largest}")
except ValueError:
    print("Please enter valid numbers.")

#

 
def check_letter(letter):
    vowels = 'aeiouAEIOU'
    if letter.isalpha() and len(letter) == 1: 
        if letter in vowels:
            return "vowel"
        else:
            return "consonant"
    else:
        return "Please enter a valid single letter."

user_input = input("Enter a letter: ")
print(f"The letter '{user_input}' is a {result}.")

#

# Function to perform basic arithmetic operations
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Invalid operator. Please use +, -, *, or /."
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    result = calculator(number1, number2, operator)
    print(f"The result of {number1} {operator} {number2} is: {result}")
except ValueError:
    print("Please enter valid numbers.")

 
