"""
This is a program to calculate the area of a sector using python programming language
Theta is the value of the angle given
r stands for the value of the radius
a stands for the area of the sector
"""
theta = int(input("what is the value of the angle given? \n"))
r = int(input("what is the value of the radius? \n"))
pi = 3.142
a = (theta / 360) * pi * r * r
print ("The value of the area of the sector equals ", a)
