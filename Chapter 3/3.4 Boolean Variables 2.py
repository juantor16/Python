# the first if statement will work, the problem is that it will always trigger
# as true even if the variable a is not equal to b. because b by itself is
# considered true.
a = "c"
if a=="B" or "b":
    print ("a is equal to b. Maybe.")

# This is a better way to do the if statement.
if a=="B" or a=="b":
    print ("a is equal to b.")

if a=="c":
    print ("in reality, a is equal to c")
    
input ("press <enter>")

