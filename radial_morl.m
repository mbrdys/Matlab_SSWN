function [h]=radial_morl(dn,xn,tn,INP)
za=((diag(-dn))*(xn-tn)');
z=(za'*za)^0.5;
h=exp(-z^2/2)*cos(5*z);
% pause(1)