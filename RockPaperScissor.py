import random

valid=('r','p','s')


while True:
    inp =input("Rock ,paper ,Scissor (r/p/s) :").lower()

    if inp not in valid:
        print("Invalid Choice")
        continue

    computer=random.choice(valid)

    print(f'You choose : {inp}')
    print(f'Computer choose: {computer}')

    if inp==computer:
        print(f"Both players selected {inp}. It's a tie!")
    elif inp=='s' and computer=='p':
        print("You win")
    elif inp=='r' and computer=='s':
        print("You win")
    elif inp=='p' and computer=='r':
        print("You win")
    else:
        print("You lose")

    should_continue=input("Continue (y/n)?").lower()
    if should_continue =='n':
        print("Good Game Dear")
        break






# Ask user to make a choice
# not valid print error
#let computer make choice
#print choice
#determine wineer
#continue y or no
# terminate if not