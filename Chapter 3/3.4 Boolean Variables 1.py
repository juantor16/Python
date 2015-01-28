# Boolean data type. This is legal!
a=True
b=False
if a:
    print ("a is true")
    
# How to use the not function
if not (a):
    print ("a is false")

# And and Or operators.
if a and b:
    print ("a and b are both true")

#asigning values to Boolean data types
x=3
y=3
# This next line is strange-looking, but legal.
# C will be true or false, depending if
# a and b are equal.
z=x==y
#prints value of c, in this case True.
print ("x is"),(x),(" y is"),(y),( "so z is"),(z)

if 1:
    print ("1")
if "A":
    print ("A")
# if the value in the if statement is zero, it will be treated as false.
# and value other than zero is cosidered True.
if 0:
    print("zero")
