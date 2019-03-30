import numpy as np 
from coefficients import getCoefficients
from tranformations import all
#solve paper airplane equations of motion
#based on code by Robert F. Stengel
#
#@author Jonah Gourlay
#@date March 29, 2019
#
#x(0)   =   Body-axis x inertial velocity, u,     m/s
#x(1)   =   Body-axis y inertial velocity, v,     m/s
#x(2)   =   Body-axis z inertial velocity, w,     m/s
#x(3)   =   Inertial x position of CM,     x,     m
#x(4)   =   Inertial y position of CM,     y,     m
#x(5)   =   Inertial z position of CM,    -z,     m
#x(6)   =   Body-axis roll rate,           p,     rad/s
#x(7)   =   Body-axis pitch rate,          q,     rad/s
#x(8)   =   Body-axis yaw rate,            r,     rad/s
#x(9)   =   Inertial roll angle,           phi,   rad
#x(10)  =   Inertial pitch angle,          theta, rad  
#x(11)  =   Inertial yaw angle,            psi,   rad 

#environmental constants @25 deg C and atmospheric pressure
dens = 1.1839   #kg/m^3     -- Density of Air
g = 9.81        #m/s^2      -- Acceleration due to gravity  

#return the body-axis windfield based on inertial windfield components
def wind(wx,wy,wz,x):
    return HIB(x[9],x[10],x[11])*np.matrix([[wx],[wy],[wx]])

#return the body-axis windfield 
def gravity(x):
    return HIB(x[9],x[10],x[11])*np.matrix([0],[0],[g])

#return the air relative velocity
def velocity(x,wind):
    Vair = np.matrix([[x[0]],[x[1]],[x[2]]])+wind
    return np.linalg.norm(Vair,2)

#return the 