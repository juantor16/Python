for i in range(5):
    print ("i will not chew gum in class.")
# programers tend to use i, because it is short for increment. This variable helps track when the loop should end.
# The range function controls how many times the code in the loop is run. In this case, 5 times.

for i in range(5):
    print ("Please,")
print ("can i go to the mall?")
# This will print "Please," five times and "can i go to the mall?" only once. because the second print is not indented.

#This code takes the prior example and indents line 3. This change will cause the program to print "Please," and "Can I go to the mall?" 5 times.
#Since the statement has been indented "Can I go to the mall?" is now part of the for loop and will repeat 5 times just line the word "Please,".

for i in range(5):
    print ("Please,")
    print ("can i go to the mall?")

# The code below will print the numbers 0 to 9. Notice tat the loop starts a 0 and does not include the number 10. It is natura to assume that range (10) would include 10
# But it stops just short of it.
# Print the numbers 0 - 9
for lineNumber in range (10):
    print (lineNumber)
#the code above prints out from 0 - 9.

# to go from 1 to 10, there are a couple ways to do it.
# way 1: send the range function two numbers. One for the number to start at. The second number just increase from 10 to 11.

#prints the numbers 1 to 10, way 1:
for i in range (1,11):
    print (i)

#This code takes the prior example and indents line 3. This change will cause the program to print "Please," and "Can I go to the mall?" 5 times.
#Since the statement has been indented "Can I go to the mall?" is now part of the for loop and will repeat 5 times just line the word "Please,".

#print the numbers 1 to 10, way 2
for i in range(10):
    print(i+1)
