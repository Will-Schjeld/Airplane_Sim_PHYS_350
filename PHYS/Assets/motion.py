import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import integrate
from equations import xdot
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
speed = 10;

def fly(xdot, tspan, x0, wind):
    h = 1e-2
    t0, tf = tspan[0], tspan[1]
    iter = round((tf-t0)/h)
    x = np.zeros((int(iter+1),len(x0)))
    x[0,:] = x0

    for i in range(0,iter):
        if(x[i,5] <= -1.2):
            t = np.linspace(t0,(i-1)*h,i)
            return [x,t]
        k1 = xdot(t0 + (i-1)*h, x[i,:], wind)
        k2 = xdot(t0 + (i-1)*h + h/2, x[i,:] + (h/2)*k1, wind)
        k3 = xdot(t0 + (i-1)*h + h/2, x[i,:] + (h/2)*k2, wind)
        k4 = xdot(t0 + (i-1)*h + h, x[i,:] + h*k3, wind)
        x[i+1,:] = x[i,:] + (h/6)*(k1+2*k2+2*k3+k4)

    t = np.linspace(t0,tf,iter+1)

    return [x,t]

[x,t] = fly(xdot, [0,5], np.array([speed,0,0,0,0,0,0,0,0,0,-1.6,0]), np.array([0,0,0]))

i = 0;
while i < len(x[:, 0]):
    print(x[i,3])
    print(x[i,4])
    print(x[i,5])
    print(x[i,9])
    print(x[i,10])
    print(x[i,11])
    i = i+4;
    