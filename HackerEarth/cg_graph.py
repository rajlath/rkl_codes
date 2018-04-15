
n=input()
while n-4:p=3+int('1yrof7i9b1lsi207bozyzg2m7sclycst0zsczde5oks6zt8pedmnup5omwfx56b29',36)/10**n%10;print n,"is %d."%p;n=p
print"4 is magic."

s = int('1yrof7i9b1lsi207bozyzg2m7sclycst0zsczde5oks6zt8pedmnup5omwfx56b29',36)
print len(`s`)
print s

n=input()
while n-4:p=(922148248>>n/10*3&7)+(632179416>>n%10*3&7)+(737280>>n&1)+4*(n<1);print n,'is %d.'%p;n=p
print'4 is magic.'

while(<>){for(split){s/^([^aeiou]+)(.*)/$2$1ay / or $_.='way ';print}}

i=input;x=i();y=i();print x-x/y*y


a=input()
i=0
while a>=1e3:a/=1e3;i+=1
print"%%.%d"%input()%a+" kMGTPE"[i]

t=p=0
for r in raw_input():n=10**(205558%ord(r)%7)%9995;t+=n-2*p%n;p=n
print t