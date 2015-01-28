# -*- coding: cp1252 -*-
#1. Correct the following code:
'''temperature = float (input("Temperature")
if temperature > 90:
    print("It is hot outside.")'''

#answer
temperature = int(input("Temperature"))
if temperature>90:
    print ("it is hot outside")

#2. There are two things wrong with this code. One prevents it from running, and the other one is subtle.
'''
x == 4
if x >= 0:
    print("x is positive.")
else:
    print("x is not positive.")

'''

#answer
x = 4
if x>=0:
    print("x is positive.")
else:
    print("x is not positive.")

#3. There are four things wrong with this code. Copy it into a script in IDLE and find the errors.
'''
answer = input("What is the name of Dr. Bunsen Honeydew's assistant?")
if a = "Beaker":
    print("Correct!")
    else
    print("Incorrect! It is Beaker.")
'''

answer = str(raw_input ("What is the name of Dr. Bunsen Honeydew's assistant?"))
if answer == "Beaker":
    print("Correct!")
else:
    print("Incorrect! It is Beaker.")

#4. Correct the following code:
'''
userInput = input("A cherry is a:")
print("A. Dessert topping")
print("B. Desert topping")
if userInput=="A":
    print("Correct!")
'''
#answer
print("A. Dessert topping")
print("B. Desert topping")
userInput = str(raw_input("A cherry is a:"))
if userInput=="A":
    print("Correct!")
else:
    print("incorrect")

#5. What three things are wrong with the following code?
'''
x=input("Enter a number:")
if x=3
    print ("You entered 3")
'''
#answer
x=input("Enter a number:")
if x==3:
    print ("You entered 3")
else:
    print ("You entered "), x

#6. This program doesn't work correctly. What is wrong?
'''
x=input("How are you today?")
if x=="Happy" or "Glad":
    print ("That is good to hear!")
'''

#answer
# first input needs to be turned into a string, secondly the target for the or function must be specified.
x=str(raw_input("How are you today?"))
if x=="Happy" or x =="Glad":
    print ("That is good to hear!")

#7. Look at the code below. Write your best guess on what it will print. Next, run the code and see if you are correct.
'''
x = 5
y = x == 6
z = x == 5
print("x=",x)
print("y=",y)
print("z=",z)
if y:
    print ("Fizz")
if z:
    print ("Buzz")
'''
#answer
x=5
z=z
buzz
#correction
('x=', 5)
('y=', False)
('z=', True)
Buzz

#8. Correct the following code:
'''
answer = input("True or False, is 3+4 equal to 7?")
a=True
b=False
if a:
    print("Correct")
else:
    print("Incorrect")
'''

#answer:
a=True
b=False
answer = str(raw_input("True or False, is 3+4 equal to 7?"))
if answer == "a":
    print("Correct")
elif "b":
    print("Incorrect")

#9. Write a Python program that will take in a number from the user and print if it is positive, negative, or zero.
x=input("enter a number:")
if x == 0:
    print("you have chosen zero")
elif x<=-1:
    print ("you have chosen a negative number")
elif x>= 1:
    print ("you have chosen a positive number")

#10. Write a Python program that will take in a number from a user and print out “Success” if it is greater than -10 and less than 10, inclusive.
x=input("enter a number:")
if x>=-10 and x<=10:
    print ("success")
else:
    print ("failure")













                     
