function error=obj_fun(output,net_out,net_size)

threshold=net_size(4); %%% zmienna mowiaca ilu pierwszych wartosci na wyjsciu sieci nie bierzemy pod uwage przy obliczaniu bledu

for a=1:size(output,1)
    for b=1:size(output,2)
        err(a,b)=(net_out(a,b)-output(a,b))^2;
    end
    A=[0:1/(size(output,2)-threshold-1):1]';
    B=(err(a,threshold+1:size(output,2)));
%     errors(a)=mean(err(a,threshold+1:size(output,2)));
    errors(a)=B*A ;
    
    
end

error = mean(errors);