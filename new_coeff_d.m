function coeff=new_coeff_d(coeff,net_size,coeff_bounds)

a=floor((net_size(3))*rand)+1;
b=floor((net_size(1)+net_size(2)+net_size(4))*rand)+1;
coeff.dilations(a,b)=(coeff_bounds(4)-coeff_bounds(3))*((0.2-0)*randn)+coeff_bounds(3);