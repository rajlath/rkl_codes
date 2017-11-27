'''
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:
Input:
formula = "H2O"
Output: "H2O"
Explanation:
The count of elements are {'H': 2, 'O': 1}.
Example 2:
Input:
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation:
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:
Input:
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation:
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Note:

All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
'''

import string

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        n = len(formula)
        if n == 0:
            return ""
        s = []
        p = 0
        while p <= n:
            if p == n or formula[p] == ')':
                t = p + 1
                while t < n and formula[t] in string.digits:
                    t += 1
                digits = int(formula[p + 1:t]) if p + 1 != t else 1
                p = t
                d = dict()
                while len(s) > 0 and s[len(s) - 1] != '(':
                    cur = s.pop()
                    for k in cur:
                        if k in d:
                            d[k] += cur[k]
                        else:
                            d[k] = cur[k]
                for k in d:
                    d[k] *= digits
                if len(s) > 0 and s[len(s) - 1] == '(':
                    s.pop()
                s.append(d)
            elif formula[p] == '(':
                s.append('(')
                p += 1
            else:
                t = p + 1
                while t < n and formula[t] in string.ascii_lowercase:
                    t += 1
                token = formula[p:t]
                p = t
                while t < n and formula[t] in string.digits:
                    t += 1
                digits = int(formula[p:t]) if p != t else 1
                p = t
                s.append({token: digits})
        resd = s[0]
        keys = resd.keys()
        res = ""
        keys.sort()
        for i in range(len(keys)):
            res += keys[i]
            if resd[keys[i]] > 1:
                res += str(resd[keys[i]])
        return res
