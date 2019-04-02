%   PHYS 350 Project
%	March 17, 2019
    clc;
    clear;
    
	global Ixx Iyy Izz Ixz WA m g rho Cb WS AR e SM Cr v Fus G Ct zwing w k0 k1 FV
    Ixx     =   6231*10^-9;              %TODO: CALCULATE
    Iyy     =   37320*10^-9;
    Izz     =   34580*10^-9;
    Ixz     =   2646*10^-9;
    
    m = .005;
    g = -9.81;
    rho = 1.225;
       
    %dimensional constants for dart shaped paper airplane
    % sourced from: Natalia Cook's Thesis on paper airplane design
    Fus = .0525;      %mm    -- Fuselage depth
    w = .001;           %mm    -- Fuselage width
    WA = 8211.5E-6;     %mm^2  -- Wing Area
    WS = .139;        %mm    -- Wing Span
    FV = 9765E-9;       %mm^3  -- Fuselage Volume
    AR = 2.352;      %      -- Aspect Ratio
    Ct = .074;         %mm    -- Tip Chord
    Cr = .186;        %mm    -- Root Chord
    Cb = .138041;    %mm    -- Mean Aerodynamic Chord
    Ml = .140;        %mm    -- Mean Aerodynamic Chord Location
    CG = .081;         %mm    -- Center of Gravity
    SM = .059/Cr;      %mm    -- Static Margin
    G = 5*pi/180; %rad   -- Dihedral Angle
    e = 0.9;         %      -- Oswald Efficiency Factor
    zwing = -.02885;  %mm    -- Distance of quarter chord below centerline
    k0 = 0.075;      %      -- Wing Yaw First Order Coefficient
    k1 = 0.175;      %      -- Wing Yaw Second Order Coefficient

       
    %environmental and material constants
    v = 15.52*10^-6;       %mm^2/s -- Kinematic Viscosity of air @ 25 deg C
	
%   a) Equilibrium Glide at Maximum Lift/Drag Ratio
	z		=	1;			% Initial Height, m
	x		=	0;			% Initial x, m
    y       =   0;          % Initial y, m
	to		=	0;			% Initial Time, sec
	tf		=	.5;			% Final Time, sec
	tspan	=	[to tf];
	xo		=	[3 0 0 x y z 0 0 0 pi/3 -pi/4 pi/4]';         % Given as [u v w x y z p q r phi theta psi]
	[ta,xa]	=	ode23('EqMotion',tspan,xo);
    [tb,xb] =   ode23('EqMotion',tspan + tf, xa(end,:)');
    [tc,xc] =   ode23('EqMotion',tspan + 2*tf, xb(end,:)');
    

    plot3(xa(:,4),xa(:,5),xa(:,6))
    hold on
    plot3(xb(:,4),xb(:,5),xb(:,6))
    hold on
    plot3(xc(:,4),xc(:,5),xc(:,6))
	xlabel('Range X, m'), ylabel('Range Y, m'), zlabel('Height, m'), grid 