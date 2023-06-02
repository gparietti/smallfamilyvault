import time
key = "weloveourdog"                                                #This is the password that will be required once family membership has been verified. You can change it.
key2 = "4"                                                          #This is the answer to the security question that will only be asked after entering the password.You can change it.
login = ("John Green", "Brianna Red", "Pablo Green", "Anna Green")  #These are the members of the family; each name among the " represents a person. (the first word is the name, the second the surname.)
print("SMALL FAMILY VAULT by gparietti")
time.sleep(2)
user = input("insert your name:")
print("looking for your name in the family..." + " " + user)
time.sleep(2)
print(user + ", " + "your surname?")
cog = input ("")
print("checking..." + " " + cog)
time.sleep(2)
print("wait...")
time.sleep(3)
print("trying to log in as:" + "     " + "Name:" + " " + user + "  " + "Surname:" + " " + cog)
time.sleep(2)
if user + " " + cog in login:
        print(" ")
        print(" ")
        print("                 SMALL FAMILY VAULT welcomes you!                    ")
        print(" ")
        print(" ")
        time.sleep(3)
        for i in range (3, 0 , -1):                                 #The number 3 represents the number of attempts available to try the password.                  
            attempt = input("enter the family password:")
            if attempt == key:
                break
            else:
                print("wrong password, please retry!")
                time.sleep(1)

        if i == 1:
            print("access denied. It is no longer possible to enter the password, then log in.")
        else:
            time.sleep(1)
            print("correct key!")
            time.sleep(2)
            attempt2 = input("Security question: How many members are you in the family?")
            if attempt2 == key2:
                print("let me check..." + key2)
                time.sleep(2)
                print(" ")
                print("here you can add your secure things...")
                time.sleep(3)
            else:
                print("sccess denied. You should know that...")
                time.sleep(2)
                
else:
    print("not a family member...")
    time.sleep(3)
#gparietti idea's
