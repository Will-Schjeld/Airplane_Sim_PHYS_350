function eqns = EqMotion(t,x)

	global Ixx Iyy Izz Ixz WA m g rho Cb WS
    
    u = x(1);
    v = x(2);
    w = x(3);
    p = x(7);
    q = x(8);
    r = x(9);
    phi = x(10);
    theta = x(11);
    psi = x(12);
    
    Va = sqrt(u^2 + v^2 + w^2);
    beta = asin(v / Va);
    alpha = atan(w / u);
    qbar  =	0.5 * rho * Va^2;	% Dynamic Pressure, N/m^2
    gx = -g*sin(theta);
    gy = g*sin(phi)*cos(theta);
    gz = g*cos(phi)*cos(theta);
    
    coefs = GetCoefficients(x,alpha,beta,Va);
    
    %X-direction Body Force Coefficient (CX)
    CX = -coefs(1)*cos(alpha) + coefs(2)*sin(alpha);

    %Y-direction Body Force Coefficient (CY)
    CY = coefs(3);
    
    %Z-direction Body Force Coefficient (CZ)
    CZ = -coefs(1)*sin(alpha) - coefs(2)*cos(alpha);
 
    
    faero = [CX CY CZ]' * qbar * WA;
    
    L = coefs(4) * qbar * WA * WS;
    M = coefs(5) * qbar * WA * Cb;
    N = coefs(6) * qbar * WA * WS;
    
    %Cartesian Accelerations in direction of euler angles
    udot   = faero(1)/m + gx + r*v - q*w;
	vdot   = faero(2)/m + gy - r*u + p*w;
    wdot   = faero(3)/m + gz + q*u - p*v;
    
    %Roll, Pitch, Yaw Accelerations (Angular Accelerations)
    pdot   = (Izz*L + Ixz*N - (Ixz*(Iyy - Ixx - Izz) * p + (Ixz^2 + Izz*(Izz - Iyy))*r)*q) / (Ixx*Izz - Ixz^2);
    qdot   = (M - (Ixx - Izz)*p*r - Ixz*(p^2-r^2)) / Iyy;
    rdot   = (Ixz*L + Ixx*N + (Ixz*(Iyy - Ixx - Izz) * r + (Ixz^2 + Ixx*(Ixx - Iyy))*p)*q) / (Ixx*Izz - Ixz^2);
    
    %Standard Cartesian Cord Velocities
    xdot   = (cos(theta)*cos(psi))*u + (-cos(phi)*sin(psi) + sin(phi)*sin(theta)*cos(psi))*v + (sin(phi)*sin(psi) + cos(phi)*sin(theta)*cos(psi))*w;
    ydot   = (cos(theta)*sin(psi))*u + (cos(phi)*cos(psi) + sin(phi)*sin(theta)*sin(psi))*v + (-sin(phi)*cos(psi) + cos(phi)*sin(theta)*sin(psi))*w;
    zdot   = (-sin(theta)*u + (sin(phi)*cos(theta))*v + (cos(phi)*cos(theta)*w));
    
    %Euler Angles Rate of Change
    phidot = p + (q*sin(phi) + r*cos(phi))*tan(theta);
    thetadot = q*cos(phi) - r*sin(phi);
    psidot = (q*sin(phi) + r*cos(phi))*sec(theta);
    
	eqns	=	[udot vdot wdot xdot ydot zdot pdot qdot rdot phidot thetadot psidot]';