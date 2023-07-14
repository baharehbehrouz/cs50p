import random
while True:
    digit = input("Level:")
    if digit.isdigit():
        if int(digit) > 0:
            break
digit = int(digit)
rndNumber = random.randint(1, digit)

a=True
while a:
    Guess = input("Guess:")
    if Guess.isdigit():
        Guess = int(Guess)
        if Guess > 0 and Guess<=digit:
            if Guess > rndNumber:
                print("Too large!")
            elif Guess < rndNumber:
                print("Too small!")
            elif Guess == rndNumber:
                print("Just right!")
                a=False
                break