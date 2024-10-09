import random 

Guess=random.randint(1,100)

while True:
    try:
        number = int(input("Guess the number between 1-100:"))
        if number<Guess:
            print("Too low")
        elif number>Guess:
            print("To high")
        else:
            print("Congrats🫶 , You guessed it right!")
            break
    except:
        print("Invalid input")



# Generate a random number
#loop
    # make user to guess
    # valid true nehi toh erro
    # if num<guess
    # low
    # if num>guess
    # high
    # if num==guess
    # win

