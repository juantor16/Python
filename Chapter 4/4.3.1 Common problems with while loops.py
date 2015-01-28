#The programmer wants to count fown from 10. What is wrong and how can it be fixed?
'''
i = 10
while i == 0:
    print (i)
    i -= 1
'''
#fix:
i=10
while i>=0:
    print (i)
    i-=1
print
#what is wrong with the loop that tries to count to 10? What will happen when its run? How should it be fixed?
'''
i=1
while i < 10:
    print (i)
'''
#fix
i=0
increment=1
while i <= 9:
    i+=increment
    print (i)
print

