function coeff=new_coeff_w(coeff,net_size,coeff_bounds)

a=floor((net_size(2)+net_size(4))*rand)+1;
b=floor((net_size(3))*rand)+1;
coeff.weights(a,b)=(coeff_bounds(2)-coeff_bounds(1))*rand+coeff_bounds(1);