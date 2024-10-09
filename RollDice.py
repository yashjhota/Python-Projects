import random

while True:
    choice = input("Roll the Dice ? (y/n):").lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
        if die1 == die2:                # optional just for fun
            print("Great!")             # you can remove it 
    elif choice =='n':
        print("Thanks for Coming")
        break
    else:
        print("Invalid Chocie")


# importing random library which have random fucntion to give random numbers
