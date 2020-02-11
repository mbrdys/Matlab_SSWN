function coeff=init(net_size, coeff_bounds)

dim_weights=[(net_size(2)+net_size(4)),net_size(3)];                    %number of network weights
dim_dilat_coeff=[net_size(3),(net_size(1)+net_size(2)+net_size(4))];    %number of dilation coeff
dim_trans_coeff=[net_size(3),(net_size(1)+net_size(2)+net_size(4))];    %number of translation coeff

coeff.weights=(coeff_bounds(2)-coeff_bounds(1))*rand(dim_weights(1),dim_weights(2))+coeff_bounds(1);                                % generacja losowych wag sieci
coeff.dilations=(coeff_bounds(4)-coeff_bounds(3))*rand(dim_dilat_coeff(1),dim_dilat_coeff(2))+coeff_bounds(3);      % generacja losowych dilation coeffitions
coeff.translations=(coeff_bounds(6)-coeff_bounds(5))*rand(dim_trans_coeff(1),dim_trans_coeff(2))+coeff_bounds(4);   % generacja losowych translation coeffitions