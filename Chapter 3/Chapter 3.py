'''Variables used in the example if statements'''
a=4
b=5
# Basic comparisons
if a<b:
    print("A is less than B")

if a>b:
    print ("A is greater than B")

print ("Done")

if a<=b:
    print ("a is less than or equal to b")
 
if a>=b:
    print ("a is greater than or equal to b")

'''
example if statements: equal not equal'''

#equal

if a==b:
    print ("you win")

#not equal
if a !=b:
    print ("you lose")

'''The two most common mistakes in mixing the = and ==
operators are demonstrated below:'''
#this is wrong
a==1

#this is also wrong
#if a=1:
#    print("A is one")

'''3.2 Indentation
Indentation matters. Each line under the if statement that is indented will
only be executed if the statement is true:'''
x=1
if x==1:
    print ("if X is one, this will print")
    print ("so will this")
    print ("and this.")

print ("this will always print because it is not indented")

'''Indentation must be the same. This code doesn't work.'''

if x==1:
  print ("indented two spaces.")
    print ("indented four. This will generate an error")
   print ("the computer will want you to make up your mind.")
'''Once an if statement has been finished, it is not possible to reindent to
go back to it. The test has to be performed again.'''

if x==1:
    print ("if x is one, this will print.")
    print ("so will this.")

print ("this will always print because it is not indented")
    print ("this will generate an error. Why is it indented?")

'''An if statement can check multiple conditions by chaining together
comparisons with and and or.'''

'''example if statements, using /"and/" and/"or/"'''
#and
if a<b and a<c:
    print ("a is less than b and c")
#non-exclusive or
if a<b or a<c:
    print ("a is less thanb and c")

''' if statements and Boolean data types.'''
# Boolean data type. This is legal!
a=true
if a:
    print ("a is true")
# How to use the not function
if not (a):
    print ("a is false")
#It is also possible to use Boolean variables with and and or operators.
a = trie
b = false
if a and b:
    print ("a and b are both true")
