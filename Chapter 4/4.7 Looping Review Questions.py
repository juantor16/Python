#1. Write a Python program that will use a for loop to print your name 10 times, and then the word "Done" at the end.
for i in range(10):
    print("Juan")
print("done")
print

#2. Write a Python program that will use a for loop to print "Red" and then "Gold" 20 times.
for i in range(20):
    print("Red")
    print("Gold")
print

#3. Write a Python program that will use a for loop to print the even numbers from 2 to 100, inclusive.
for i in range (2,101,2):
    print (i)
print

#4. Write a Python program that will use a while loop to count form 10 down to, and including, 0. Then print the words "Blast Off!"
i=11
while i>=1:
    i-=1
    print(i)
print

#5. There are four thigs wrong with this program. Find and correct them.
'''
print ("This program takes three numbers and returns the sum.")
total=0

for i in range(3):
    x=input("Enter a number: ")
    total=total+i
    print("The total is: ",x)
'''
#answer
print("This program takes three numbers and returns the sum.")
total=0
for i in range(3):
    x=int(input("Enter a number: "))
    total+=x

print("The total is: "),total
print

#6. write a Python program that:
# ~asks the user for seven numbers
# ~prints the total sum of the numbers
# ~prints the count of the positive entries, the number entries equal to zero, and the number of negative entries.
neg=0
pos=0
zer=0
total=0
for i in range(7):
    x=int(raw_input("Enter a number, negative, positive or zero: "))
    if x<0:
        neg+=1
    elif x==0:
        zer+=1
    else:
        pos+=1

total+=x
print("The total sum of your numbers was: "),total,(" from which: "),neg,(" were negative numbers, "),pos,(" were positive numbers, and "),zer,("were zeros")

