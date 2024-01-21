from random import randint  
x=randint(1,100)

print("i m thinking of a number between 1 and 100.can you guess what is ?")
n=int(input("Enter your guess:"))


while n != x:
    if n<x:
        print("Your guess is too low. Guess again")
    elif n>x:
        print("Your guess is too high. Guess again")
    

    n=int(input("Enter your guess:"))
print("Congratulations! You guessed the number correctly!")


