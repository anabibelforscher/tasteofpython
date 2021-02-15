import random

def main ():
    number = random.randint(5,15)
    countdown(number)
    print ("End!")

def countdown(n):
    for i in range (n):
        print(n-i)

main ()

