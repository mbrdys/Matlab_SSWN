data=zeros(7,500);
b=0;
for i=1:11998
if length(restults{i,2})==5
    if restults{i,2}=='WIG20'
    ind=1;
    b=b+1;
    end
end
if length(restults{i,2})==6
if restults{i,2}=='MIDWIG'
   ind=2;   
end
end
if length(restults{i,2})==3
if restults{i,2}=='NIF'
    ind=3;
end
end
if length(restults{i,2})==6
if restults{i,2}=='mWIG40'
    ind=4;
end
end
if length(restults{i,2})==6
if restults{i,2}=='sWIG80'
    ind=5;    
end
end
if length(restults{i,2})==7
if restults{i,2}=='TECHWIG'
    ind=6;
end
end
if length(restults{i,2})==3
if restults{i,2}=='WIG'
    ind=7;
else
    ind=8;
end
end

data(ind,b)=restults{i,3};

end

