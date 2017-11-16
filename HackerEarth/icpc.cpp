#copied
/*
It's an ad-hoc problem. You may get tricked into believing that this problem has a lot to do with string algorithms, or the likes, but to solve this one: you don't need any of those tricks. You need to notice that all you need is the length of strings to be stored, and since the value of n is very low (1000) - all the lengths can be easily hashed in an array of 1000, and then we could simply iterate over the array where all the lengths are hashed and if we find any value which modulo is NOT equal to zero, we would know that there are not enough people of that given length to form a group in a camp.

You may look at the implementation of the tester and setter for clarification.

*/
tc = int(raw_input())
assert(tc>0 and tc<51)
for i in xrange(tc):
	n, k = map(int, raw_input().split())
	l = [0]*1000
	ok = True
	assert(n>0 and n<1001)
	assert(k>0 and k<1001)
	assert(n>=k)
	assert(n%k==0)
	for j in xrange(n):
		a = raw_input()
		l[len(a)] +=1
	for z in l:
		if z%k!=0:
			ok = False
			break
	if (ok):
		print "Possible"
	else:
		print "Not possible"

