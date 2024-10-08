import re

# Regex based on your conditions
condition = r'^[a-z]+[\._]?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,3}$'

Email = input("Enter your Email : ")

if re.search(condition, Email):
    print("Valid")
else:
    print("Invalid")


# first - a to z  jhotayash@gmail.com
# second - 0 to 9 cls
# third - . _ 1 time
# fourth - @ one time 
# fifth - . postion should be second or third from the last 


