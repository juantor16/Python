userName=str(raw_input("Welcome to trivia 1.0, please enter your name: "))
print("hello "),userName

print ("Question #1")
print ("how much is 2x2?")
print ("A = 2")
print ("B = 4")
print ("C = 2839")
x=0.0
first=str(raw_input("your answer is: "))
if first.lower()=="b":
       print("Correct")
       x=x+1.0
      
else:
       print("wrong")
print
print ("Question #2") 
second=str(raw_input("what is the name of a computer code based on only ones and zeros? "))
if second.lower()=="binary" or second.lower()=="binary code":
       print("correct")
       x=x+1.0
       
else:
       print("wrong, it is called: binary code")
print
print ("Question #3")
second=str(raw_input("what is the name of the largest country in the world? "))
if second.lower()=="russia":
       print("correct, Russia is the largest country in the world")
       x=x+1.0
else:
       print("wrong, the largest country in the world is Russia.")
print
print("Question #4")
third=str(raw_input("in which year did WW2 finish? "))
if third=="1945":
       print("correct, WW2 finished on the year 1945")
       x=x+1.0
else:
       print("wrong, WW3 finished on the year 1945")
print
print ("Question #5") 
fourth=str(raw_input("what is the Japanese word for heart? "))
if fourth.lower()=="kokoro":
       print ("Correct, kokoro means heart in Japanese")
       x=x+1.0
else:
       print("wrong, the correct answer is kokoro")
print
print ("Question #6") 
fifth=str(raw_input("what is the name of the first black president of the United States?"))
if fifth.lower()=="obama" or fifth.lower()== "barack"or fifth.lower()== "barack obama":
       print("correct")
       x=x+1.0
else:
       print("Wrong, his name is Barack Obama")
print 
print("Question #7") 
sixth=str(raw_input("what was hitler's first name?"))
if sixth.lower()=="adolf":
       print("Correct, his name was Adolf Hitler.")
       x=x+1.0
else:
       print("wrong, his name was Adolf Hitrler.")
print ("your score is: "),x,("of 7")

print ("you got"),x/7.0*100,("% percent right")

input ("press<enter>")





