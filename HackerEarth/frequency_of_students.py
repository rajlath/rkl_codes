'''
SAMPLE INPUT 
5
sumit
ambuj
himanshu
ambuj
ambuj

SAMPLE OUTPUT 
ambuj 3
himanshu 1
sumit 1
'''

names = {}
for _ in range(int(input())):
    curr = input()
    names[curr] = names.get(curr, 0) + 1
for key in sorted(names):
    print("%s: %s" % (key, names[key]))
