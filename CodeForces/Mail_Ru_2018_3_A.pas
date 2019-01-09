var
a:array[-1000..100000]of longint;
x,n,i,q,j:longint;
begin
readln(N);
for i:=1 to n do begin
    read(q);
    for j:=1 to  q do begin
            read(x);
            inc(a[x]);
    end;
end;
for i:=1 to 1000 do if a[i]=n then write(i,' ');
end.