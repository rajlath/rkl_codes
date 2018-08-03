# https://app.codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/longest_password
# Python 3.6.0
from string import ascii_uppercase, ascii_lowercase, digits
def solution(A):
    '''
    type A : array of words
    rtype  : integer
    '''
    lets = ascii_uppercase + ascii_lowercase + digits
    def validate(s):
        letters = 0
        digits  = 0
        for i in s:
            if i not in lets:
                return False
            if i in "0123456789":
                digits += 1
            else:
                letters += 1

        return letters%2==0 and digits%2==1

    maxs = int(-10e9)
    AW = [x for x in A.split()]

    for i in AW:
        if validate(i):
            maxs = max(maxs, len(i))
    return -1 if maxs == int(-10e9) else maxs


print(solution("test 5 a0A pass007 ?xy1"))





