# example of improper ordering if/elif/else
temperature=int(input("what is the temperature in Fahrenheit?" ))
if temperature > 90:
    print ("it is hot outside")
elif temperature > 110:
    print ("oh man, you could fri eggs on the pavement!")
elif temperature < 30:
    print ("it is cold outside")
else:
    print ("it is ok outside")
print ("done")

# This is proper!
print ("this is proper")
temperature=int(input("what is the temperature in Fahrenheit?" ))
if temperature > 110:
    print ("oh man, you could fri eggs on the pavement!")
elif temperature > 90:
    print ("it is hot outside")    
elif temperature < 30:
    print ("it is cold outside")
else:
    print ("it is ok outside")
print ("done")

input ("Press <Enter>")
