
hrs, mins = [int(x) for x in input().split(":")]
count = 0
while hrs//10 != mins % 10 or hrs % 10 != mins // 10:
    count +=1
    mins += 1
    if mins >= 60:
        mins %= 60
        hrs += 1
    if hrs >= 24:
        hrs %= 24
print(count)
'''
h,m,i=map(int,raw_input().split(':'))+[0]
while h/10!=m%10 or h%10!=m/10:
    h,m,i=(h+(m==59))%24,(m+1)%60,i+1
print i
'''
