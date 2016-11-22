__acrimony__ = 'dev'
__jluo0117__ ='dev2'

import math

print ("Welcome to Projectile Calculator")
angle = input("Enter the angle of launch in degrees: ")
velocity = input("Enter the velocity at launch in meters per second: ")
print("Acceleration of gravity on different planets/satellites: ")
print ("Earth = - 9.81")
print ("Mars = - 6.301")
print ("Moon = - 1.625")
gravity = input("Enter the acceleration of gravity ")
if gravity >0:
    gravity=gravity*-1
radian_angle = math.radians(angle) #converts the angle in degrees to radians
y_velocity = math.sin(radian_angle) # velocity #gets y-component of velocity

time_top = (-y_velocity)/gravity # calculates the time to the top of the trajectory

total_time = time_top*2 #conservation of energy, duh.

x_velocity = math.cos(radian_angle) * velocity # finds the x-component of velocity

distance = x_velocity * total_time # total distance traveled, 'nough said

print ("Total time traveled: {}".format(total_time))
print ("Total distance traveled: {}".format(distance))
