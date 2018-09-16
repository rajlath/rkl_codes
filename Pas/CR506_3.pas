
program CR506_3;
uses math;
 var
  a:array[1..200000]of longint;
  i,j,n,x,t:longint;
 begin
  read(n);t:=1;
  for i:=1 to n do read(a[i]);
  for i:=2 to n do
   if(a[i]<=a[i-1]*2) then x:=max(x,i-t+1)
    else t:=i;
  if x=0 then write(1) else write(x);
 end.
