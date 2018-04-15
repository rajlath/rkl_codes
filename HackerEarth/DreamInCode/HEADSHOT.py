all_fibo = [0, 1]
mods     = 1000000007
def get_fibo(n):
    global all_fibo
    cl = len(all_fibo)
    if cl <= n:
        for i in range(cl, n+1):
            nexts = (all_fibo[i-1]%mods + all_fibo[i-2]%mods)%mods
            all_fibo.append(nexts)
    return all_fibo[n]

print(get_fibo(int(input())))