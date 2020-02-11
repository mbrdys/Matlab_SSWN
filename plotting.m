function []=plotting(wal_output,wal_net_out)



[a b] = size(wal_output);

sfigure(1);

for i=1:a
subplot(i,1,i),plot([1:b],wal_output(i,1:b),'r',[1:b],wal_net_out(i,1:b),'k');AXIS([1 b -1.1 1.1])
end