from math import gcd
class Solution():
    def is_match(self, str1, str2):
        for i in range(len(str1)):
            if str1[i] != str2[i % len(str2)]: return False
        return True

    def gcdOfStrings( self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        lene = gcd(len1, len2)
        str3 = str1[:lene]
        if self.is_match(str1, str3) and self.is_match(str2, str3): return str3
        return ""



