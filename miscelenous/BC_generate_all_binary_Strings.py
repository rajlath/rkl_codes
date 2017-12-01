def generate_all_binary_string(n, A):
    '''
    generate all binary strings that can be formed using n bits
    param int
    ret a collection of string
    '''
    global B
    if n < 0:
        #print("".join(map(str,A)))
        B.append("".join(map(str,A)))
    else:
        A[n-1] = 0
        generate_all_binary_string(n - 1, A)
        A[n-1] = 1
        generate_all_binary_string(n - 1, A)

n = 4
A = [0]* (n)
B = []
generate_all_binary_string(n, A)
print(B)