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

def fly(xdot, tspan, x0):
    h = 1e-2
    t0, tf = tspan[0], tspan[1]
    iter = round((tf-t0)/h)
    x = np.zeros((int(iter+1),len(x0)))
    x[0,:] = x0

    for i in range(0,iter):
        if(x[i,5] <= -1.2):
            t = np.linspace(t0,(i-1)*h,i)
            return [x,t]
        k1 = xdot(t0 + (i-1)*h, x[i,:])
        k2 = xdot(t0 + (i-1)*h + h/2, x[i,:] + (h/2)*k1)
        k3 = xdot(t0 + (i-1)*h + h/2, x[i,:] + (h/2)*k2)
        k4 = xdot(t0 + (i-1)*h + h, x[i,:] + h*k3)
        x[i+1,:] = x[i,:] + (h/6)*(k1+2*k2+2*k3+k4)

    t = np.linspace(t0,tf,iter+1)

    return [x,t]
    
#test flight
[x,t] = fly(xdot, [0,5], np.array([10,4,5,0,0,0,0,0,0,0,0,0]))
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x[0:len(t),3],x[0:len(t),4],x[0:len(t),5])
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_zlim(-1.2,3)
plt.show()