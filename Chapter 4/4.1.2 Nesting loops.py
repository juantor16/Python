#what does this print? why?
for i in range(3):
    print ("a")
for j in range(3):
    print ("b")
print

# This next block of code is almost identical to the one above. The second for loop has been indented one tab stop so that it is now nested inside
# of the first for loop. This changes how the code runs significantly.
for i in range(3):
    print ("a")
    for j in range(3):
        print ("b")
 
print("Done")
print
