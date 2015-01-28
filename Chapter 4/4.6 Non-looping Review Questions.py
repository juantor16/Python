#5. what does the following program print out?
x=3
x+1
print(x)
# answer: 3

#6.Correct the following code:
'''
user_name=input("Enter your name: ")
'''
#answer
user_name=str(raw_input("Enter your name: "))

#7. Correct the following code
'''
value=int(input(print("Enter your age")))
'''
#answer
value=int(input("Enter your age: "))
print value

#correct the following code:
'''
temperature=float(input("Temperature"))
if temperature>=90:
    print("it is hot outside")
'''
#answer
temperature = float (input("Temperature"))
if temperature >= 90:
    print("It is hot outside.")

#9. Correct the following code:
'''
print("Welcome to Oregon Trail")
userInput=input("what is your occupation?")

print("A. Banker")
print("B. Carpenter")
print("C. Farmer")

if userInput=A:
    money=100
else if userInput=B:
    money=70
else if userInput=C:
    money=50
'''
#answer

print("Welcome to oregon trail")
print("A. Banker")
print("B. Carpenter")
print("C. Farmer")
userInput=str(raw_input("What is your occupation?"))
if userInput.lower()=="a":
    money=100
elif userInput.lower()=="b":
    money=70
elif userInput.lower()=="c":
    money=50
print(money)
print("you have "),money,(" dollars")

#10 What is wrong with this code?
'''
x=input("Enter a number: ")
if x>100
    print ("you entered a large number.")
else
    print("You did not enter a large number.")
'''
#answer
x=float(input("Enter a number: "))
if x>=100:
    print ("You entered a large number.")
else:
    print("You did not enter a large number.")

# write a program that asks the user how many quarters and nickles they have, then prints the total amount of money those coins are worth.
quarter=0.25
nickle=0.05
quarters=float(input("quarters: "))
nickles=float(input("nickles:" ))
print("you have "),(quarters/4)+(nickles/20),("Dollars.")


