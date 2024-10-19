import time  # Optional

print("Welcome to the Quiz!")
time.sleep(1)  # Wait for a seconds before proceeding

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Okay! Maybe next time!")
    quit()



print("Chalo, Let's play")
score = 0

question = input("What is the extension of Python? ")
if question.lower() == "py":
    print("Correct! The extension of Python is indeed 'py'.")
    score += 1
else:
    print("Incorrect! The extension of Python is 'py'.")

question = input("What is the extension of PowerBI? ")
if question.lower() == "pbix":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The extension is 'pbix'.")

question = input("What Does RAM Stands for? ")
if question.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")




print("You Scored:", score)
