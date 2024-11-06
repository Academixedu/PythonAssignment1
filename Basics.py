# Please Answer the Below Questions and Give Your Explanation in One Line After Completing the Assignment
 # Write a Python program that assigns your name and age to two different variables. Then, reassign the age variable with a new value.
 # Assign the value of x = 10. Reassign it to x + 5 and print the result.
# Take a number from the user as input. The input is a string by default. Convert it into an integer and print the result.
# Assign a float value to a variable, then cast it to an integer. Print both the float and the integer values.
# Write a Python program that prompts the user to enter their age, and then cast the input to an integer. After that, assign their age in the next decade (age + 10) to a new variable and print it.

#
# Assigning name and age to variables
name = "Santhosh"
age = 19

print("Name:", name)
print("Age:", age)

age = 20

print("Updated Age:", age)

#

x = 10

x = x + 5

print("The value of x after reassignment is:", x)

#

user_input = input("Please enter a number: ")

number = int(user_input)

print("The integer value is:", number)

#

float_value = 10.75

integer_value = int(float_value)

print("Float value:", float_value)
print("Integer value:", integer_value)


#

user_input = input("Please enter your age: ")

age = int(user_input)

age_next_decade = age + 10

print("In ten years, you will be:", age_next_decade)

