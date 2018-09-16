def longest_Palind_SS(str):
    if str == str[::-1]: return str
    maxlen = 1
    start , end = 0, len(str)
    low   , high= 0, 0
    for i in range(1, len(str)):
        #evenlength
        low = i - 1
        high= i
        while low > 0 and high < len(str) and str[low] == str[high]:
            if high - low + 1 > maxlen:
                start = low
                maxlen = high - low + 1
            low -= 1
            high+= 1
        low = i -1
        high= i + 1
        while low > 0 and high < len(str) and str[low] == str[high]:
            if high - low + 1 > maxlen:
                start = low
                maxlen= high - low + 1
            low -= 1
            high+= 1
    print(str[start:start+maxlen])
    return maxlen

print(longest_Palind_SS("ccd"))

