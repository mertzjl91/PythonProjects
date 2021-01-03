import random

n=random.randint(1,20)

guess = int(input("Enter a number 1 to 20:"))
while n != "guess":
    print()
    if guess < n:
        print("Guess is too low, try again!")
        guess = int(input("Enter a number 1 to 20, better get it right this time!"))
    elif guess > n:
        print("Guess is too high, try again!")
        guess = int(input("Enter a number 1 to 20, better get it right this time, dummy!"))
    else:
        print("Oh my god you finally got it that took forever. Thank god! \nCongratulations on your... achievement")
        break
    print()



