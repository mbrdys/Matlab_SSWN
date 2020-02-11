function net_out=sswn(net_input,coeff,net_size);

INP=net_size(1)+net_size(2)+net_size(4);
dn=zeros(1,INP);
tn=zeros(1,INP);
xn=zeros(1,INP);

for k=1:size(net_input,2)

    for f=1:net_size(2)+net_size(4)  
        if k>1
           net_input(INP-(net_size(2)+net_size(4))+f,k)=y(f,k-1);
        else
           net_input(INP-(net_size(2)+net_size(4))+f,k)=0; 
        end
    end
   
    for i=1:net_size(3)
        dn(:)=coeff.dilations(i,:);
        tn(:)=coeff.translations(i,:);
        xn=net_input(1:INP,k)';
        v(i)=radial_morl(dn,xn,tn,INP); 
    end    
           
    for f=1:net_size(2)+net_size(4)
        vs(f,1:net_size(3))=v(1:net_size(3)).*coeff.weights(f,1:net_size(3));
        y(f,k)= sum(vs(f,:));
    end

end

net_out=y(1:net_size(2),:);