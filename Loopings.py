# Write a Python program to find the sum of the first n natural numbers, where n is provided by the user.
# Write a Python program to print the multiplication table of a number entered by the user, up to 10.
# Write a Python program that prints all even numbers between 1 and n, where n is provided by the user.
# Write a Python program to print numbers from n to 1, where n is provided by the user.

#1

n = 4
sum = n
x = 0 
for i in range(1, n + 1):  
    x += i  
print(x)

#2
# y =int(input("Enter a number: "))

# for n in range(1, 11):
#     print(y, "x", n, "=", y * i)
    
#3
# w = int(input("Enter a number: "))

# for i in range(2, w + 1, 2):  
#     print(i)
    
#4
n = int(input("Enter a number: "))
for i in range(n, 0, -1):  
    print(i)
