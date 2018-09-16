def solve(cur, iq, k, DP, mod, arr):


     if DP[cur][iq] != -1:
         return DP[cur][iq]
     res = 0
     for i in range(arr[cur]+1):
         if iq - i < 0:break
         res += solve(cur+1, iq - 1, k, DP, mod, arr) % mod
     return dp[cur][iq]



def main():
    nots = int(input())
    mod=100000009
    for _ in range(nots):
        n, k = [int(x) for x in input().split()]
        DP = [-1] * (n+ 1)
        arr= [int(x) for x in input().split()]
        solve(0, n, k, DP, mod, arr)

if __name__ == "__main__":
    main()
