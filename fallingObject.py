print("This program calculates the distance an object has fallen and the velocity at a certain time")
time=input("Enter the amount of time the object has fallen for: ")
velocity = time*9.8
print("The speed of the object at {} seconds is {} m/s" .format(time,velocity))
position = ((9.8*9.8)*time)/2
print ("The position of the object at {} seconds is {} meters".format(time, position))
