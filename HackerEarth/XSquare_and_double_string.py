from collections import Counter
for _ in range(int(input())):
    sc = Counter(input()).most_common()
    ans = "No"
    for i in sc:
        if i[1] > 1:
            ans = "Yes"
            break
    print(ans)        
            

