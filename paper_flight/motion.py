import numpy as np 
import matplotlib.pyplot as plt
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

