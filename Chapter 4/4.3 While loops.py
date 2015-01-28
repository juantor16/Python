# this is a for loop
for i in range(10):
    print (i)
print
#using a while loop to print the numbers 0 to 9
i=0 #this is a sentinel (i)
while i<10:
    print (i)
    i+=1

#example infinite loop (not good)
'''
    while range(10):
        print(i)
'''

#short hand code of i=i+1 is i+=1

#this can be done with substraction and multiplication as well. Example:
print
i=0
while i<10:
    print (i)
    i+=1
print

#What would this print?
i=1
while i <= 2**32:
    print(i)
    i *= 2
print

#Looping until the user wants to quit
quit="n"
while quit=="n":
    quit=raw_input("Do you want to quit? ")
print

#looping until the game is over or the user wants to quit
done=False
while not(done):
    quit=raw_input("do you want to quit? ")
    if quit == "y":
        done=True;

    attack=raw_input("does your elf attack the dragon? ")
    if attack=="y":
        print ("Bad choice, you died.")
        done =True;
print
#This isn't perfect though, because if the user says she wants to quit, the code will still ask if she wants to attack the dragon.

#Here is an example of using a while loop where the code repeats until the value gets close enough to zero:
value=0
increment=.5
while value<0.999:
    value+=increment
    increment*=0.5 
    print(value)

