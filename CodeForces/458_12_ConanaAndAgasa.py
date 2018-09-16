#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      rinfo
#
# Created:     31/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    input()
    a=[0]*(10**5+1)
    ans = "Agasa"
    for i in map(int,input().split()):
        a[i]+=1
    for i in a:
        if i%2:
            ans = "Conan"
            break
    print(ans)


if __name__ == '__main__':
    main()
