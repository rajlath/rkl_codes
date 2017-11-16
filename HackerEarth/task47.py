a, b = 1, 15

perfect = [2, 3, 5]
y = []
cnt = 0
for x in perfect:
	if x >= a:
		c = a
		while  c <= b:
			if (c % x == 0 and c not in y):
				cnt += 1
				y.append(c)
			c += x	
			
print(cnt, y)			




'''
a,b=map(int,input().split());
a,
print(len(set([n if n%p==0 else 0 for p in [x for x in range(a,b) if sum(y for y in range(1,x) if x%y==0)==x] for n in range(a,b+1)]))-1)

fscanf(STDIN,"%d\n",$a);
fscanf(STDIN,"%d\n",$b);
$l=array(6,28,496,8128,33550336,8589869056,137438691328,2305843008139952128);
$x=array();
foreach($l as&$k){
    if ($k>=$a){
        $c=$k;
        while($c<=$b){
            if($c%$k==0&&!in_array($c,$x)){
                $r++;
                $x[]=$c;
            }
            $c+=$k;
        }
    }
}
'''
a, b = 1, 15
print(len(set([n if n%p==0 else 0 for p in [2, 3, 5] for n in range(a,b+1)]))-1)

