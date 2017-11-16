noe, k_len = [int(x) for x  in input().split()]
arr = [int(x) for x  in input().split()] +[0,0]
for i in range(noe-(k_len - 1)):
    print(max(arr[i:i+k_len]), end=" ")
   
