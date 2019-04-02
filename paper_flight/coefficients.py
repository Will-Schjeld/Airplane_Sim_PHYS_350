import numpy as np
#calculate static aerodynamic coefficients
#
#@author: Jonah Gourlay
#@date: March 28, 2019

#dimensional constants for dart shaped paper airplane
#sourced from: Natalia Cook's Thesis on paper airplane design
Fus = 52.5e-3      #mm    -- Fuselage depth
w = 1e-3           #mm    -- Fuselage width
WA = 8211.5e-6     #mm^2  -- Wing Area
WS = 139e-3        #mm    -- Wing Span
FV = 9765e-9       #mm^3  -- Fuselage Volume
AR = 2.352         #      -- Aspect Ratio
Ct = 74e-3         #mm    -- Tip Chord
Cr = 186e-3        #mm    -- Root Chord
Cb = 138.041e-3    #mm    -- Mean Aerodynamic Chord
Ml = 140e-3        #mm    -- Mean Aerodynamic Chord Location
CG = 81e-3         #mm    -- Center of Gravity
SM = (59/Cr)*1e-3  #mm    -- Static Margin
G = 5*np.pi/180    #rad   -- Dihedral Angle
e = 0.9            #      -- Oswald Efficiency Factor
zwing = -28.85e-3  #mm    -- Distance of quarter chord below centerline
k0 = 0.075         #      -- Wing Yaw First Order Coefficient
k1 = 0.175         #      -- Wing Yaw Second Order Coefficient

#environmental and material constants
v = 15.52e-6       #mm^2/s -- Kinematic Viscosity of air @ 25 deg C

#takes the angle of attack and pitch rate in the body frame
#and returns the static aerodynamic constants [CD, CL, CY, Cl, Cm, Cn]
#as an array
#
#@param x       double array    motion variables
#@param alpha   double          angle of attack
#@param beta    double          sideslip angle
#@param V       double          Earth relative speed
#
#@return [CD, CL, CX, CY, CZ, Cl, Cm, Cn]   aerodynamic constants
def getCoefficients(x, alpha, beta, V):
    #Lift Coefficient (CL)
    CLo = 0
    CLa = np.pi*AR/(1+np.sqrt(1+(AR/2)**2))
    CLqhat = -2*np.pi/3*CLa
    CLq = CLqhat*Cb/(2*V)
    CL = CLo + CLa*alpha + CLq*x[7]

    #Drag Coefficient (CD)
    CDo = 0.02
    epsilon = 1/(np.pi*e*AR)
    CD = CDo + epsilon*CL**2

    #Pitching Moment Coefficient (Cm)
    Cmo = 0
    Cma = -CLa*SM
    Cmqhat = -np.pi/(3*AR)
    Cmq = Cmqhat*Cb/(2*V)
    Cm = Cmo + Cma*alpha + Cmq*x[7]

    #X-direction Body Force Coefficient (CX)
    CX = -CD*np.cos(alpha) + CL*np.sin(alpha)

    #Z-direction Body Force Coefficient (CZ)
    CZ = -CD*np.sin(alpha) - CL*np.cos(alpha)

    #Side Force Coefficient (CY)
    CYo = 0
    Re = V*Cr/v 
    Sb = np.pi*Fus**2/4
    S = WA
    Swet = WA+Sb
    Cf = 1.328/np.sqrt(Re)
    CDpwing = 0.135/(Cf*Swet/Sb)**(1/3)*Sb/S
    k = np.pi*AR/(2*(1+np.sqrt(1+(AR/4)**2)))
    CYbwing = -CDpwing-k*G**2
    CYbfus = -2*Sb/S
    CYb = CYbwing + CYbfus
    CY = CYo + CYb*beta

    #Rolling Moment Coefficient (Cl)
    Clo = 0
    taper = WS/Cb
    tanA = (Cr-Ct)/(WS/2)
    Clbwing = (-1+2*taper)/(6*(1+taper))*(G*CLa + CL*tanA)
    Clbfus = 1.2*np.sqrt(AR)*(zwing*(Fus+w))/WS**2
    Clb = Clbwing + Clbfus
    Clphat = -np.pi*AR/32
    Clrhat = Clphat
    Clp = Clphat*WS/(2*V)
    Clr = Clrhat*WS/(2*V)
    Cl = Clo + Clb*beta + Clp*x[6] + Clr*x[8]

    #Yawing Moment Coefficient (Cn)
    Cno = 0
    Cnbwing = k0*CL*G + k1*CL**2
    K = (1-Fus/Cr)**1.3
    Cnbfus = -2*K*FV/Sb
    Cnb = Cnbwing + Cnbfus
    Cnphat = -0.03
    Cnrhat = -0.025
    Cnp = Cnphat*WS/(2*V)
    Cnr = Cnrhat*WS/(2*V)
    Cn = Cno + Cnb*beta + Cnp*x[6] + Cnr*x[8]

    return [CD, CL, CX, CY, CZ, Cl, Cm, Cn]