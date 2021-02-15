'''''
Write a program that picks a pseudorandom number between 
1 and 10, inclusive, and gives the user up to 3 chances to guess that number, 
each time printing some message 
informing the user whether or not their guess was correct.
'''''

import random

def main ():
    number = random.randint(1,10)
   
    for i in range (3):
        guess = int(input ("Try to guess the random number:"))
        if guess > number:
            print("Guess is too large")
        elif guess < number:
            print ("Guess is too small")
        else:
            print ("Correct!")
            return
    

main()