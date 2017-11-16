for i in range(int(input())):
    str1 = [0]*26
    str2 = [0]*26
    st1 = input()
    for i in st1:
        str1[ord(i) - ord('a')] = 1
    st2 = input()
    for i in st2:
        str2[ord(i) - ord('a')] = 1
    for i in range(26):
        if str1[i] == 1 and str2[i] == 1:
            print("Yes")
            break
    if i == 25:print("No")      
        
