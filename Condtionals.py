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

# number = input("enter the number")
# result = int(number)
# result1=result%2
# if result1 == 0:
#     print ("Given number is even number")
# else :
#     print("Given number is odd number")

# number = input ("enter the number: ")
# result =int(number)
# if result>0:
#     print("given number is positive")
# elif result<0 :
#     print ("given number is negative")
# else :
#     print ("given number is zero")

# marks=input("enter the student marks :")
# result =int(marks)
# if result>=90 :
#     print("Student grade is A")
# elif result <89 and result>=80 :
#     print("Student grade is B")
# elif result <79 and result>=70 :
#     print("Student grade is C")
# elif result <69 and result>=60 :
#     print("Student grade is D")
# elif result<60 :
#     print("Student grade is F")

# number1 = input("enter the number: ")
# number2 = input("enter the number: ")
# number3 = input("enter the number: ")
# if number3>number2 and number1 :
#     print( number3, "is greater number")
# elif number2>number1 :
#     print( number2, "is greater number")
# else :
#     print( number1, "is greater number")

# letter = input("Enter the letter: ")
# print(letter)
# if letter == "a" :
#     print("the given letter is vowel")
# elif letter == "e" :
#     print("the given letter is vowel")
# elif letter == "i" :
#     print("the given letter is vowel")
# elif letter == "o" :
#     print("the given letter is vowel")
# elif letter == "u" :
#     print("the given letter is vowel")
# else :
#     print ("the given letter is consonant")

number1 = int(input("enter the number: "))
number2 = int (input("enter the number: "))
operator = input("enter the operator: ")
if operator == "+" :
    print(number1 + number2)
elif operator == "-" :
    print(number1 - number2)
elif operator == "*" :
    print(number1 * number2)
elif operator == "/" :
    print(number1 / number2)
else :
    print("User given operator is not supported")
