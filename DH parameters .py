from math import sin, cos
from numpy import *
from functools import reduce


x = int(input("How many degree of Freedom You want to calculate?"))
a = []

for i in range(x):
    print()
    print ("Enter the", i, "-", i+1, "degree of freedom values")
    print()

    def DH_parameters(t1, t2, t3, t4):
        a = array ([[cos(radians(t1)), -sin(radians(t1)) * cos(radians(t2)), sin(radians(t1)) * sin(radians(t2)), t3 * cos(radians(t1))],
             [sin(radians(t1)), cos(radians(t1)) * cos(radians(t2)), -cos(radians(t1)) * sin(radians(t2)), t3 * sin(radians(t1))],
             [0, sin(radians(t2)), cos(radians(t2)), t4],
             [0, 0, 0, 1]])
        print()
        return a

    t1 = float(input("Enter the value of thetta"))
    t2 = float(input("Enter the value of alpha"))
    t3 = float(input("Enter the value of a"))
    t4 = float(input("Enter the value of d"))

    DH_parameters(t1, t2, t3, t4)
    a.append(DH_parameters(t1, t2, t3, t4))

ans = reduce (lambda x, y: matrix(x) * matrix(y) , a)
print ("The Total Transformstion Matrix is")
print (ans)












