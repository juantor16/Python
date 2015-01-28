# incorrect comparison
userName = str(raw_input("What is your name? "))

if userName == "Paul":
    print ("You have a nice name.")
else:
    print ("Your name is ok.") 
'''
#this does not work! it will always be true
if userName == "Paul" or "Mary":

#this works
if userName == "Paul" or userName == "Mary"
'''
#Case-insensitive text comparison

userName = str(raw_input("What is your name? "))
if userName.lower() == "paul":
    print ("You have a nice name.")
else:
    print ("Your name is ok.") 
