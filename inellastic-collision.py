__3ddy98__='dev'

import math

#m1v1+m2v2= (m1+m2)vf

print ("Welcome to Inellastic Calc")
	
mass1 = input("Enter the mass of object 1: ")
v1 = input("Enter the velocity value  for object 1: ")
mass2 = input("Enter the mass of object 2: ")
v2 =  input("Enter the velocity value of object 2: ")	
vf = ((mass1*v1)+(mass2*v2))/(mass1+mass2)

print("Your final velocity is:{}m/s".format(vf))
 	
