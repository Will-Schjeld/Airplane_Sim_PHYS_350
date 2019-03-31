%takes the angle of attack and pitch rate in the body frame
%and returns the static aerodynamic constants [CD, CL, CY, Cl, Cm, Cn]
%as an array
%
%@param x       double array    motion variables
%@param alpha   double          angle of attack
%@param beta    double          sideslip angle
%@param V       double          Earth relative speed
%
%@return [CD, CL, CY, Cl, Cm, Cn]   aerodynamic constants
function coefs = GetCoefficients(x, alpha, beta, V)

    global  WA Cb WS AR e SM Cr v Fus G Ct zwing w k0 k1 FV
    
    %Lift Coefficient (CL)
    CLo = 0;
    CLa = pi*AR/(1+sqrt(1+(AR/2)^2));
    CLqhat = -2*pi/3*CLa;
    CLq = CLqhat*Cb/(2*V);
    CL = CLo + CLa*alpha + CLq*x(5);

    %Drag Coefficient (CD)
    CDo = 0.02;
    epsilon = 1/(pi*e*AR);
    CD = CDo + epsilon*CL^2;

    %Pitching Moment Coefficient (Cm)
    Cmo = 0;
    Cma = -CLa*SM;
    Cmqhat = -pi/(3*AR);
    Cmq = Cmqhat*Cb/(2*V);
    Cm = Cmo + Cma*alpha + Cmq*x(8);

    %Side Force Coefficient (CY)
    CYo = 0;
    Re = V*Cr/v ;
    Sb = pi*Fus^2/4;
    S = WA;
    Swet = WA+Sb;
    Cf = 1.328/sqrt(Re);
    CDpwing = 0.135/(Cf*Swet/Sb)^(1/3)*Sb/S;
    k = pi*AR/(2*(1+sqrt(1+(AR/4)^2)));
    CYbwing = -CDpwing-k*G^2;
    CYbfus = -2*Sb/S;
    CYb = CYbwing + CYbfus;
    CY = CYo + CYb*beta;

    %Rolling Moment Coefficient (Cl)
    Clo = 0;
    taper = WS/Cb;
    tanA = (Cr-Ct)/(WS/2);
    Clbwing = (-1+2*taper)/(6*(1+taper))*(G*CLa + CL*tanA);
    Clbfus = 1.2*sqrt(AR)*(zwing*(Fus+w))/WS^2;
    Clb = Clbwing + Clbfus;
    Clphat = -pi*AR/32;
    Clrhat = Clphat;
    Clp = Clphat*WS/(2*V);
    Clr = Clrhat*WS/(2*V);
    Cl = Clo + Clb*beta + Clp*x(7) + Clr*x(9);

    %Yawing Moment Coefficient (Cn)
    Cno = 0;
    Cnbwing = k0*CL*G + k1*CL^2;
    K = (1-Fus/Cr)^1.3;
    Cnbfus = -2*K*FV/Sb;
    Cnb = Cnbwing + Cnbfus;
    Cnphat = -0.03;
    Cnrhat = -0.025;
    Cnp = Cnphat*WS/(2*V);
    Cnr = Cnrhat*WS/(2*V);
    Cn = Cno + Cnb*beta + Cnp*x(7) + Cnr*x(9);

    coefs = [CD, CL, CY, Cl, Cm, Cn];
    end

