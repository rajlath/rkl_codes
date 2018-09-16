'''
Example
Sample Input
ELLY
KRIS
Sample Output
29

TOPCODER
TCOINDIA
57

AWIODJGWAMBAUWNMQEROAIQWYRZSVEPTT
BNSIAELDALCGAWOPIWEQTYCNAZEKJXVYU
105
'''
def get_nearest(c, BB):
    mins = 100
    for i in BB:
        cnt = 0
        iao, ibo = ord(c), ord(i)
        if ibo > iao : cnt = ibo - iao
        else: cnt = 26 -iao + ibo
        if cnt < mins:
            lets, mins = i, cnt
    return lets, mins

def anagram(A, B):
    '''
    A  : string
    B  : string
    ret Count int
    '''
    count = 0
    al = list(A)
    bl = (list(B))
    for i in al:
        if i in bl:
            bl.pop(bl.index(i))
            continue
        r, d = get_nearest(i, bl)
        bl.remove(r)
        count += d
    return count


#print(anagram("SULBDXWINJRHKZLCO","VSZVHECDBLJPQEBHC"))

def tester(testname):
    folder = testname+"_tests"
    for i in range(1,51):
        s = str(i)
        if i < 10:s = "0"+str(i)
        infile_name = folder + "\\" +testname+"."+s+"."+"in"
        oufile_name = folder + "\\" +testname+"."+s+"."+"sol"

        in_file = open(infile_name)
        a, b = [x.strip() for x in in_file]
        ou_file = open(oufile_name)
        ans  = int(ou_file.readline())
        man  = anagram(a, b)
        print(s +" "+ ["Failed", "Passed"][ans == man])
        in_file.close()
        ou_file.close()




tester("Anagrams")

