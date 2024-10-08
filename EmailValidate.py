Email = input("Enter your Email:") #g@g.in
k=0 # Just used for Getting update if there is an space in email it will update to one and print wrong email
j=0 
d=0
if len(Email)>=6:
    if Email[0].isalpha():
        if ("@" in Email) and (Email.count("@")==1):
            if (Email[-3]=='.') ^ (Email[-4]=='.'):  #XOR operator used because any one condition should be only true . In case using or operator if both or true it will be true.
                for i in Email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=='_' or i=='.' or i=='@':
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Wrong Email Space hai/UpperCase/,5")
            else:
                print("Dot(.) use kar be,4")
        else:
            print("Email should have @ symbol and it should be only once ,3")
    else:
        print("Email should start with a letter ,2")
else:
    print("Email is not valid, 1 Error")