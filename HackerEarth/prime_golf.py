k,P,pr=1,1,[]
while k<1001:pr.append(k if P%k else -1 );P*=k*k;k+=1
print(pr)