import numpy as np 
from coefficients import getCoefficients
from transformations import all
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
#x(5)   =   Inertial z position of CM,     z,     m
#x(6)   =   Body-axis roll rate,           p,     rad/s
#x(7)   =   Body-axis pitch rate,          q,     rad/s
#x(8)   =   Body-axis yaw rate,            r,     rad/s
#x(9)   =   Inertial roll angle,           phi,   rad
#x(10)  =   Inertial pitch angle,          theta, rad  
#x(11)  =   Inertial yaw angle,            psi,   rad 

#environmental constants @25 deg C and atmospheric pressure
dens = 1.1839   #kg/m^3 -- Density of Air
g = -9.81       #m/s^2  -- Acceleration due to gravity 

#material and geometric constants
S = 8211.5e-6   #m^2    -- Wing Area
b = 139e-3      #m      -- Wing Span
m = 5e-3        #kg     -- Plane Mass
Ixx = 4984.8e-9 #kg*m^2 -- X Area moment of Inertia
Iyy = 29856e-9  #kg*m^2 -- Y Area Moment of Inertia
Izz = 27664e-9  #kg*m^2 -- Z Area Moment of Inertia
Ixz = 27664e-9  #kg*m^2 -- XZ Area Moment of Inertia

#return the state equations
def xdot(x):
    #body relative windfield
    wind = HIB(x[9],x[10],x[11])*np.matrix([[wx],[wy],[wx]])

    #air relative velocity field
    Vair = np.matrix([[x[0]],[x[1]],[x[2]]])+wind

    #body relative gravity field
    g = HIB(x[9],x[10],x[11])*np.matrix([0],[0],[g])

    #constants
    V = np.linalg.norm(Vair,2)
    alpha = np.arctan(Vair[2]/Vair[0])
    beta = np.arcsin(Vair[1]/V)
    qbar = 0.5*dens*V**2
    y = np.transpose(HIB(x[9],x[10],x[11]))*np.matrix([[x[0]],[x[1]],[x[2]]])

    #coefficients
    coef = getCoefficients(x,alpha,beta,V)
    CD = coef[0]
    CL = coef[1]
    CX = coef[2]
    CY = coef[3]
    CZ = coef[4]
    Cl = coef[5]
    Cm = coef[6]
    Cn = coef[7]

    #body forces and moments
    X = CX*qbar*S
    Y = CY*qbar*S
    Z = CZ*qbar*S
    L = Cl*qbar*S
    M = Cm*qbar*S
    N = Cn*qbar*S

    #dynamic equations of motions
    du = X/m + g[0] + x[8]*x[1] - x[7]*x[2]
    dv = Y/m + g[1] - x[8]*x[0] + x[6]*x[2]
    dw = Z/m + g[2] + x[7]*x[0] - x[6]*x[1]
    dx = y[0]
    dy = y[1]
    dz = y[2]
    dp = (Izz*L + Ixz*N - (Ixz*(Iyy - Ixx - Izz)*x[6] + (Ixz**2 + Izz*(Izz - Iyy))*x[8])*x[7])
    dq = (M - (Ixx - Izz)*x[6]*x[8] - Ixz*(x[6]**2 - x[8]**2))/Iyy
    dr = (Ixz*L + Ixx*N + (Ixz*(Iyy - Ixx - Izz)*x[8] + (Ixz**2 + Ixx*(Ixx - Iyy))*x[6])*x[7])
    dphi = x[6] + (x[7]*np.sin(x[9]) + x[8](np.cos(x[9])))*np.tan(x[10])
    dtheta = x[7]*np.cos(x[10]) - x[8]*np.sin(x[10])
    dpsi = (x[7]*np.sin(x[10]) + x[8]*np.cos(x[10]))/np.cos(x[10])

    return np.matrix([[du],[dv],[dw],[dx],[dy],[dz],[dp],[dq],[dr],[dphi],[dtheta],[dpsi]])