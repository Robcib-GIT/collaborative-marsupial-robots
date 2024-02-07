#!/usr/bin/env python
from libreria_IK import cinematica_inversa_cpr5dof
#from libreria_MV import movimiento
import math

print "------------"

"""Q = cinematica_inversa_cpr5dof.eval(-200.0, -200.0, 528.0, 20.0,0.0)
Q = cinematica_inversa_cpr5dof.eval(-100.0, -200.0, 528.0, -20.0,0.0)
Q = cinematica_inversa_cpr5dof.eval(200.0, -200.0, 528.0, 20.0,0.0)
Q = cinematica_inversa_cpr5dof.eval(300.0, -300.0, 528.0, 20.0,0.0)
Q = cinematica_inversa_cpr5dof.eval(300.0, -300.0, 528.0, 20.0,45.0)"""
Q = cinematica_inversa_cpr5dof.eval(1.0, 200.0, 480.0, 30.0,0.0)
Q = cinematica_inversa_cpr5dof.eval(1.0, -200.0, 480.0, 10.0,0.0)

Q = cinematica_inversa_cpr5dof.eval(-100.0, 100.0, 528.0, 10.0,0.0)
