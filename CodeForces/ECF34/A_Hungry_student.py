'''
Ivan wants to know if he can choose two non-negative integers a and b
in such a way that he can have 'a' numbers of  small portions(of 3 chunks)
and 'b' numbers of  large ones(of 7 chunks) totalling exactly x chunks

constraints: Nos of cases lies in 1<i<100
             Total Nos of chunks is in 1<c<100
Solution : Answers will be yes if Total Nos is either divisible by 3 or 7
           Plus 7 being consist of 3 + 3 + 1
           This makes it besides some initial counts all others from 11 onwards
           can be divided into group of 3 and 7
           so answer would be Yes for all chunk count greater than 11
           and no only for 1 2 4 5 8 and 11
input
2 #number of test cases
6
5
output
YES
NO
'''
for _ in range(int(input())):
    nos_of_chunks = int(input())
    if nos_of_chunks in [1, 2, 4, 5, 8, 11]:
        print("NO")
    else:
        print("YES")