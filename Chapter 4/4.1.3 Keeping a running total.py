# The code below will total up all the numbers the user enters
total=0
for i in range(5):
    newNumber=int(input("Enter a number: "))
    total = total+newNumber 
print("the toal is:",total)

#the code below adds all the numbers from 1 to 100. Demonstrates a common patter where a running total is kept inside of a loop. This also uses
# a separate variable to track the running total.
#what is the value of sum?
sum=0
for i in range(1,101):
    sum=sum+i
print (sum)
print

#This code will count the number of times a user enters the number 0:
total=0
for i in range(5):
    newNumber=int(input("Enter a number"))
    if newNumber==0:
        total= total+1
print("you entered a total of ",total," zeros")
