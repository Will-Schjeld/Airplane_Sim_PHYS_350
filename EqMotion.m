function xdot = EqMotion(t,x)
%	Fourth-Order Equations of Aircraft Motion

	global CL CD S m g rho
	
	V 	=	x(1);
	Gamma	=	x(2);
	q	=	0.5 * rho * V^2;	% Dynamic Pressure, N/m^2
    
    
	%a = (drag force + force of gravity)/m
    %Vx or Vy = Vsin(gam)
	xdot	=	[(-CD * q * S - m * g * sin(Gamma)) / m
				 (CL * q * S - m * g * cos(Gamma)) / (m * V)
				 V * sin(Gamma)
				 V * cos(Gamma)];
             