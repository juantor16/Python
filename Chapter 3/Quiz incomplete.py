# Lab Quiz
print ("Welcome to quiz 1.0!")
userName = raw_input("First of all, please enter your name: ")
print ("Hello"),userName,("Thank you for taking this quiz!")

x = str(raw_input("are you ready?"))
if x == "yes":        
        print("Great!!! let's get started")
if x != "yes":
        print ("well, too bad, with that attitude you will not win!")
print ("Question Numero uno: ")
first = str(raw_input("What is the capital of Argentina?"))
if first.lower() == "buenos aires":
    print ("That is correct!")
elif first.lower() != "buenos aires":
    print ("Ouch! that is incorrect, the right answer is: Buenos Aires")
print ("Question Numero dos:")
second = input("How much is 5x4?")
if second == 20:
    print ("Correct!")
elif second!=20:
    print("looks like someone needs to go back to first grade!")
else:
    print("looks like someone needs to go back to first grade!")
print("Question Numero tres:")
third = input("What year was the Altair 8800 (The first computer ever) built?")
if third == 1975:
    print ("correct!")
elif third!= 1975:
    print ("You are using a computer thanks to this invetion! praise the year 1975!")
