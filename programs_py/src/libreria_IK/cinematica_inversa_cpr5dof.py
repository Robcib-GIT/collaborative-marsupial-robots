#!/usr/bin/env python
import math
import numpy as np

def eval(x,y,z,alpha,beta):

    x=float(x)
    y=float(y)
    z=float(z)
    alpha=float(alpha)
    beta=float(beta)
    # definicion de constantes de los links del robot
    x1=228.0
    x1=float(x1)
    x2=270.0
    x2=float(x2)
    x3=240.0
    x3=float(x3)
    x4=170.0
    x4=float(x4)
    # calculo de la cinematica
    print "IK_Solver ******"
    # Q1
    Q1 = math.degrees(math.atan(y/x))
    Q1 = float(Q1)
    r  = math.sqrt(pow(x,2)+pow(y,2))
    r  = float(r)
    # CALCULO Q2
    z0 = z-x1-x4*math.sin(math.radians(alpha))
    z0 = float(z0)
    x0 = r-x4*math.cos(math.radians(alpha))
    x0 = float(x0)

    r0 = math.sqrt(pow(x0,2)+pow(z0,2))
    r0 = float(r0)
    b  = math.atan(z0/x0)
    b  = float(b)
#    print z0
#    print z
#    print x1
#    print r0
    f  = math.acos((pow(r0,2)+pow(x2,2)-pow(x3,2))/(2*x2*r0))
#    print "f", f
    # Q2
    Q2 = math.degrees(b+f)
    if x==0 and z==0:
        Q2= -90
    Q2 = float(Q2)

    # Q3
    Q3 = math.degrees(math.acos((pow(x2,2)+pow(x3,2)-pow(r0,2))/(2*x2*x3)))
    Q3 = float(Q3)
#    Q3 = 180-Q3
    if Q3>0:
        Q3 = (Q3-180)
#        print "Q3"
    if x==0 and y==0:
        Q3 = 0
#        print "Q3----"

    # Q4
    Q4 = (+alpha-Q2-Q3)
    Q4 = float(Q4)
    # Q5
    Q5 = beta
    Q5 = float(Q5)

    Q1 = math.radians(Q1)
#    Q2 = math.radians(85-Q2)
#    Q3 = math.radians(Q3+84)
    Q2 = math.radians(85-Q2)
    Q3 = math.radians(Q3+90)
    Q4 = math.radians(Q4-65)
    Q5 = math.radians(Q5)

    if x==680 and z==228:
        Q1=0
        Q2=0
        Q3=0
        Q4=0
        Q5=0
        print "---"
        print ""
        print "Valores en grados"
        print math.degrees(Q1),math.degrees(Q2),math.degrees(Q3),math.degrees(Q4),math.degrees(Q5)
        return Q1, Q2, Q3, Q4, Q5
    else:
        print ""
        print "Valores en grados"
        print math.degrees(Q1),math.degrees(Q2),math.degrees(Q3),math.degrees(Q4),math.degrees(Q5)
        return Q1, Q2, Q3, Q4, Q5
