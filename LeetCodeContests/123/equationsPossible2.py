class Solution(object):
    def equationsPossible(self, equations):
        same = []
        equations.sort(key=lambda x: x[1], reverse=True)
        for a, o1, o2 , b in equations:
            if o1 == "=":
                for i, eq in enumerate(same):
                    if a in eq or b in eq:
                        same[i].update({a, b})
                        break
                    else:
                        same.append({a, b})
                    print(same)
            else:
                if a == b: return False
                for eq in same:
                    if a in eq and b in eq:
                        return False
        print(same)
        return True


print(Solution().equationsPossible(["b!=a","a==e","a!=f","d==f","a!=c"]))