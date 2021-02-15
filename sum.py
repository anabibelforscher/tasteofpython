'''''
Write a program that asks the user to type in ten integers as input and then prints their sum.
'''''

total = 0
for i in range(10):
    number = int (input("Insert a number: "))
    total += number
print ("The sum of the numbers is: ", total)

