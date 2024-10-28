# Write a Python program to find the sum of the first n natural numbers, where n is provided by the user.
# Write a Python program to print the multiplication table of a number entered by the user, up to 10.
# Write a Python program that prints all even numbers between 1 and n, where n is provided by the user.
# Write a Python program to print numbers from n to 1, where n is provided by the user.

a = int(input("enter the number: "))
print(range(a))
sum = 0
for i in range(a+1):
    sum = sum + i
print(sum)

a= int(input("enter the number: "))
for i in range(1,10+1):
   print(a ,'X', i ,'=', a*i)

b=int(input("enter the number:"))
for i in range(1,b) :
    if i%2 == 0:
        print(i)

b=int(input("enter the number:"))
for i in range(b, 0,-1) :
    print (i)
