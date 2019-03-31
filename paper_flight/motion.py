import numpy as np 
import matplotlib.pyplot as plt
import scipy
import equations
#integrate ode for given time interval
#
#@author Jonah Gourlay
#@date March 30, 2019
#
#x(0)   =   Body-axis x inertial velocity, u,     m/s
#x(1)   =   Body-axis y inertial velocity, v,     m/s
#x(2)   =   Body-axis z inertial velocity, w,     m/s
#x(3)   =   Inertial x position of CM,     x,     m
#x(4)   =   Inertial y position of CM,     y,     m
#x(5)   =   Inertial z position of CM,     z,     m
#x(6)   =   Body-axis roll rate,           p,     rad/s
#x(7)   =   Body-axis pitch rate,          q,     rad/s
#x(8)   =   Body-axis yaw rate,            r,     rad/s
#x(9)   =   Inertial roll angle,           phi,   rad
#x(10)  =   Inertial pitch angle,          theta, rad  
#x(11)  =   Inertial yaw angle,            psi,   rad 

def fly(x0,t0,tf):
    t = np.linspace(t0,tf,100)
    x = np.zeros((len(t),len(x0)))
    x[0, :] = x0
    r = integrate.ode(xdot).set_integrator("dopri15")
    r.set_initial_value(x0,t0)
    for i in range(1, t.size):
        x[i, :] = r.integrate(t[i])
        if not r.successful():
            raise RuntimeError("Could not integrate")
    return [x,t]

xt = fly([0,0,0,0,0,0,0,0,0,0,0,0],0,2)