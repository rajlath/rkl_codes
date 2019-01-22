'''
nb_elems , nb_missing = [int(x) for x in input().split()]
elems = [int(x) for x in input().split()]
missing = sorted([int(x) for x in input().split()], reverse=True)
curr = 0
for i in range(nb_elems):
    if elems[i] == 0:
        elems[i] = missing[curr]
        curr += 1
print(elems)        
print(("No", "Yes")[elems == sorted(elems)])

'''
a, b =[int(i) for i in input().split()]
elem=[int(x) for x in input().split()]
miss= sorted([int(x) for x in input().split()], reverse=True)
curr=0
for i in range(a):
    if elem[i]==0:
        elem[i]=miss[curr]
        curr+=1

if elem==sorted(elem):
    print ("No")
else:
    print ("Yes")