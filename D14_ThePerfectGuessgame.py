import random


number = random.randint(1, 100)
attempt = 1
guess = int(input("Guess the number: "))

while(True):
    if(guess>number):
        guess = int(input("Guess another number. This is too big: "))
        attempt += 1
    elif(guess<number):
        guess = int(input("Guess another number. This is too less: "))
        attempt += 1

    # else:
    #     print(f"Yeah that's the number! You guessed it right in {attempt} attempts")
    #     break

