% tic
% for i=1:10000000
%     a=abs(3-6.5);
% end
% toc
% 
% tic
% for i=1:10000000
%     a=(3-6.5)^2;
% end
% toc


for i=1:1000
a(i)=floor((net_size(2)+net_size(4))*rand)+1;
end
min(a)
max(a)