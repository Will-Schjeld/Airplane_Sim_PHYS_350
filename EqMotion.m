function eqns = EqMotion(t,x)

	global Ixx Iyy Izz Ixz A m g rho c b
    
    u = x(1);
    v = x(2);
    w = x(3);
    p = x(4);
    q = x(5);
    r = x(6);
    phi = x(10);
    theta = x(11);
    psi = x(12);
    
    Va = sqrt(u^2 + v^2 + w^2);
    %beta = asin(v / Va);
    alpha = atan(w / u);
    qbar  =	0.5 * rho * Va^2;	% Dynamic Pressure, N/m^2
    gx = -g*sin(theta);
    gy = g*sin(phi)*cos(theta);
    gz = g*cos(phi)*cos(theta);
    
    Cx = .001;
    Cy = .001;
    Cz = .001;
    Cn = 2*(sin(alpha))^2; %eqn 2.4-3
    Cl = Cn*cos(alpha);  %eqn 2.4-4a look at 4b for a better approximation
    Cm = 1; %eqn 2.4-43
    
    X = Cx * qbar * A;
    Y = Cy * qbar * A;
    Z = Cz * qbar * A;
    L = Cl * qbar * A * b;
    M = Cm * qbar * A * c;
    N = Cn * qbar * A * b;
    
    %Cartesian Accelerations
    udot   = X/m + gx + r*v - q*w;
	vdot   = Y/m + gy - r*u + p*w;
    wdot   = Z/m + gz + q*u - p*v;
    
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
    
	eqns	=	[udot vdot wdot pdot qdot rdot xdot ydot zdot phidot thetadot psidot]';