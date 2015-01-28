#1. Write a program that prints a random integer from 1 to 10 (inclusive).
import random
x=random.randrange(11)
print x
print

#2. Write a program that prints a random floating point number somewhere between 1 and 10 (inclusive).
i=random.random()
print i
print

#3. Coin flip tosser
'''
Create a progra, that will print a random 0 or 1.
instead of 0 or 1, print heads or tails.
add a loop so that the program does this 50 times.
create a running total for the numer of heads flipped, and the number of tails.
'''
coins=["heads", "tails"]
heads=0
tails=0
for num in range(1,50):
    random_index=random.randrange(2)
    tails += random_index
    print coins[random_index]
print "there were ", 50 - tails, "heads"# heads
print "and ", tails," tails"

#4 rock, paper, scissors
'''
Write a program that plays rock, paper, scissors
Create a program that randomly prints 0, 1, or 2.
Expand the program so it randomly prints rock, paper, or scissors using if
statements. Don't select from a list, as shown in the chapter.
Add to the program so it first asks the user their choice.
It will be easier if you have them enter 1, 2, or 3.
Add conditional statement to figure out who wins.
'''
#paper=0
#rock=1
#scissor=2

print"paper = 0"
print"rock = 1"
print"scissors = 2"

print"Game time! rock, paper, scissors!,"
usernum=int(raw_input("Make your choice now: "))

for num in range (0,3):
    random_index=random.randrange(3)
if random_index==0:
    print "i chose paper"
elif random_index==1:
    print "i chose rock"
elif random_index==2:
    print "i chose scissor"
if usernum==0 and random_index==2:
    print "you lose"
if usernum==0 and random_index==0:
    print "It's a tie!"
if usernum==0 and random_index==1:
    print "You won!"
if usernum==1 and random_index==0:
    print "you lose"
if usernum==1 and random_index==1:
    print "It's a tie!"
if usernum==1 and random_index==2:
    print "You won!"
if usernum==2 and random_index==1:
    print "You lose"
if usernum==2 and random_index==2:
    print"It's a tie!"
if usernum==2 and random_index==0:
    print "You won!"

    
