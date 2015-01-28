import random
#randrange fuction creates random numbers from x to y.
#random number from 0 to 49
my_number=random.randrange(50)
print my_number

#random number from 100 to 200
my_number=random.randrange(100,201)
print my_number

my_list=["rock","paper","scissors"]
random_index=random.randrange(3)
print(my_list[random_index])
