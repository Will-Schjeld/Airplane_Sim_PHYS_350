%   PHYS 350 Project
%	March 17, 2019
    clc;
    clear;
    
	global Ixx Iyy Izz Ixz A m g rho c b
    Ixx     =   .5;              %TODO: CALCULATE
    Iyy     =   .5;
    Izz     =   .2;
    Ixz     =   .1;
    c       =   .2;             % chord length, m, complete guess ****************
    b       =   .1;              % ?????
    
	A		=	0.017;			% Reference Area, m^2
	AR		=	0.86;			% Wing Aspect Ratio. Wingspan / Chord
	e		=	0.9;			% Oswald Efficiency Factor;
	m		=	0.003;			% Mass, kg
	g		=	9.81;			% Gravitational acceleration, m/s^2
	rho		=	1.225;			% Air density at Sea Level, kg/m^3	
	CLa		=	pi * AR/(1 + sqrt(1 + (AR / 2)^2));
							% Lift-Coefficient Slope, per rad
	CDo		=	0.02;			% Zero-Lift Drag Coefficient
	epsilon	=	1 / (pi * e * AR);% Induced Drag Factor	
	CL		=	sqrt(CDo / epsilon);	% CL for Maximum Lift/Drag Ratio
	CD		=	CDo + epsilon * CL^2;	% Corresponding CD
	LDmax	=	CL / CD;			% Maximum Lift/Drag Ratio
	Gamma		=	-atan(1 / LDmax);	% Corresponding Flight Path Angle, rad
	V		=	sqrt(2 * m * g /(rho * A * (CL * cos(Gamma) - CD * sin(Gamma))));
							% Corresponding Velocity, m/s
	Alpha	=	CL / CLa;			% Corresponding Angle of Attack, rad
	
%   a) Equilibrium Glide at Maximum Lift/Drag Ratio
	z		=	2;			% Initial Height, m
	x		=	0;			% Initial x, m
    y       =   0;          % Initial y, m
	to		=	0;			% Initial Time, sec
	tf		=	1;			% Final Time, sec
	tspan	=	[to tf];
	xo		=	[1 0 0 0 0 0 x y z 0 0 0]';         % Given as [u v w p q r x y z phi theta psi]
	[ta,xa]	=	ode23('EqMotion',tspan,xo);
	
%	b) Oscillating Glide due to Zero Initial Flight Path Angle
%	xo		=	[V;0;z;x];
%   xb      = zeros(1,4);
%   [tb,xb]	=	ode23('EqMotion',tspan,xo);
	
    plot3(xa(:,7),xa(:,8),xa(:,9))
%    plot(xa(:,4),xa(:,3),xb(:,4),xb(:,3))
	xlabel('Range X, m'), ylabel('Range Y, m'), zlabel('Height, m'), grid 
% 	figure
% 	subplot(2,2,1)
% 	plot(ta,xa(:,1),tb,xb(:,1))
% 	xlabel('Time, s'), ylabel('Velocity, m/s'), grid
% 	subplot(2,2,2)
% 	plot(ta,xa(:,2),tb,xb(:,2))
% 	xlabel('Time, s'), ylabel('Flight Path Angle, rad'), grid
% 	subplot(2,2,3)
% 	plot(ta,xa(:,3),tb,xb(:,3))
% 	xlabel('Time, s'), ylabel('Altitude, m'), grid
% 	subplot(2,2,4)
% 	plot(ta,xa(:,4),tb,xb(:,4))
% 	xlabel('Time, s'), ylabel('Range, m'), grid