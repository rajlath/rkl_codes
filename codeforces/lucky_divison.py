'''
s = input()
ans = s.count("4") + s.count("7")==len(s) or not int(s)%4 or not int(s)%7
print("YES" if ans else "NO")
'''
print("YNEOS"[0::2])

#n=int(input())
#print('YNEOS'[all(set(str(i))-set('47')or n%i for i in range(n+1))::2])
