# -*- coding: utf-8 -*-
'''Write a line of code that will print your name.'''
print "Juan Torres"
'''How do you enter a comment in a program?'''
# it is entered by placing the # symbol before the message.
'''What do the following lines of code output?'''
print (2/3)
#0
print (2//3)
#0
''' Write a line of code that creates a variable called pi
#and sets it to an appropriate value.'''
pi = 25
'''
Why does this code not work?
A=22
print(a)
'''
# because A is uppercase and we are asking to print (a), which is not uppercase,
# therefore (a) has no numeric value.

'''All of the variable names below can be used. But which of these is the better variable name to use?

a
A
Area
AREA
area
areaOfRectangle
AreaOfRectangle'''
# the answer is areaOfRectangle, because it has the most information, along with the fact that it begins with a lowercase letter.

'''
Which of these variables names are not allowed in Python? (More than one might be wrong.)
apple
Apple
APPLE
Apple2
1Apple
account number
account_number
account.number
accountNumber
account#'''
#Apple
#APPLE
#Apple2
#1Apple
#account number
#account#

'''
Why does this code not work?
print(a)
a=45'''
#because the value for (a) has not been defined, yet it is asked for python to print out a variable that does not yet exist.
# the correct answer would be.
a = 45
print a

'''
Explain the mistake in this code:
pi = float(3.14)'''
# the programmer has left the "input" command out of the equation, making it impossible to create a float, the right input would be the following.

pi = float( input ("enter the value of pi: "))
print pi

'''
Explain the mistake in the following code:
radius=input("Radius:")
x=3.14
pi=x
area=pi*radius**2'''
# a float for radius is missing, making it impossible to turn the user input into numerals, the correct answer would be the following.
radius=float(input("Radius: "))
x=3.14
pi2=x
area=pi2*radius**2
print area

'''Explain the mistake in the following code:
a=((x)*(y))'''
# the equation would work perfectly with or without the parenthesis.

'''Explain the mistake in the following code:
radius = input(float("Enter the radius:"))'''
# the order is incorrect, thus making the equation invalid, the correct order would be the following.
radius = float(input("Enter the radius:"))

'''Explain the mistake in the following code:
area=π*radius**2'''
#Python would start by multiplying radius by istelf, then multiplying it by π, this is not what the programmer wants
#I believe the correct function should be the following.
#area=(π*adius)**2

'''Write a line of code that will ask the user for the length of a square's side and store
the result in a variable. Make sure to convert the value to an integer.'''
sideStore= float(input("Enter length of a square's side: "))

'''Write a line of code that prints the area of the square, using the number the user typed in that you stored in question 9.'''
print sideStore * pi


'''Do the same as in questions 14 and 15, but with the formula for the area of an ellipse. 
s=πab 
where a and b are the lengths of the major radii.'''
b=float(input("Semi-major axis length (a): "))
a=float(input("Semi-minor axis length (b): "))
s=pi*a*b
print s

'''Do the same as in questions 14 and 15, but with a formula to find the pressure of a gas. 
P=nRT/V 
where n is the number of mols, T is the absolute temperature, V is the volume, and R is the gas constant 8.3144.'''
n=float(input("enter number of mols: "))
t=float(input("enter absolute temperature: "))
v=float(input("enter the volume: "))
r=8.3144
p=(n*r*t)/v

print p

# this was really difficult, and easy to understand at the same time.


input ("Press <Enter>")



