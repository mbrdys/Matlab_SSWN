function coeff=new_coeff_t(coeff,net_size,coeff_bounds)

a=floor((net_size(3))*rand)+1;
b=floor((net_size(1)+net_size(2)+net_size(4))*rand)+1;
coeff.translations(a,b)=(coeff_bounds(4)-coeff_bounds(3))*rand+coeff_bounds(3);