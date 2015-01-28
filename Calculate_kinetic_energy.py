# Calculate Kinetic Energy

print "this program calculates the kinetic energy of a moving object."
m_string = input ("Enter the object's mass in Kilograms: ")
m=float(m_string)
# m_string = input ("Enter the object's mass in Kilograms: ")
# m=float(m_string)
# is equal to:
#m_string = float(input ("Enter the object's mass in Kilograms: "))
v_string = input ("enter the object's speed in meters per second: ")
v=float (v_string)

e=0.5*m*v*v
print ("The object has "+str(e)+ " Joules of energy.")

raw_input ("press enter to exit ")

