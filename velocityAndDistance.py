import math

print ("Welcome to distance and velocity calculator")
accleration = input ("Enter the object's accleration in meters per second square: ")
intVelocity = input ("Enter the object's initial velocity in meters per second: ")
time = input ("Enter the amount of time the object will travel for in terms of seconds: ")

distance = .5*(accleration*(time*time))
distance = distance + (intVelocity*time)

velocity = intVelocity + (accleration*time)

print ("Total distance traveled: {} meters".format(distance))
print ("Final velocity: {} meters per second".format(velocity))
