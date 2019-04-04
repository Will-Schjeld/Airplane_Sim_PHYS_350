import numpy as np 
#calculate reference axes transformations
#
#@author Jonah Gourlay
#@date March 29, 2019

#bank angle
def mu(alpha, theta, phi, gamma):
    return np.arccos((np.cos(alpha)*np.cos(theta)*np.cos(phi)+np.sin(alpha)*np.sin(theta))/np.cos(gamma))

#Inertial to Intermediate 1
def HI1(psi):
    return np.matrix([[np.cos(psi),np.sin(psi),0],[-np.sin(psi),np.cos(psi),0],[0,0,1]])

#Intermediate 1 to Intermediate 2
def H12(theta):
    return np.matrix([[np.cos(theta),0,-np.sin(theta)],[0,1,0],[np.sin(theta),0,np.cos(theta)]])

#Intermediate 2 to Body
def H2B(phi):
    return np.matrix([[1,0,0],[0,np.cos(phi),np.sin(phi)],[0,-np.sin(phi),np.cos(phi)]])

#Inertial to Intermediate 4
def HI4(xi):
    return np.matrix([[np.cos(xi),np.sin(xi),0],[-np.sin(xi),np.cos(xi),0],[0,0,1]])

#Intermediate 4 to Velocity
def H4V(gamma):
    return np.matrix([[np.cos(gamma),0,-np.sin(gamma)],[0,1,0],[np.sin(gamma),0,np.cos(gamma)]])

#Velocity to Wind
def HVW(mu):
    return np.matrix([[1,0,0],[0,np.cos(mu),np.sin(mu)],[0,-np.sin(mu),np.cos(mu)]])

#Wind to Intermediate 3
def HW3(beta):
    return np.matrix([[np.cos(beta),-np.sin(beta),0],[np.sin(beta),np.cos(beta),0],[0,0,1]])

#Intermediate 3 to Body
def H3B(alpha):
    return np.matrix([[np.cos(alpha),0,-np.sin(alpha)],[0,1,0],[np.sin(alpha),0,np.cos(alpha)]])

#Inertial to Body
def HIB(psi,theta,phi):
    return H2B(phi)*H12(theta)*HI1(psi)

#Inertial to Velocity
def HIV(xi,gamma):
    return H4V(gamma)*HI4(xi)

#Inertial to Wind
def HIW(mu,gamma,xi):
    return HVW(mu)*HIV(xi,gamma)

#Wind to Body
def HWB(alpha,beta):
    return H3B(alpha)*HW3(-beta)





