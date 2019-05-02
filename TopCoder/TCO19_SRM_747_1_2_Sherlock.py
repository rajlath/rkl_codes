
class Sherlock():
    def matches(self, a, b, maxs):
        matched = sum([1 for x in a if x in b])
        #print(matched)
        return  matched >= maxs
    def isItHim(self,fname, lname):
        invalid = "It is someone else"
        answer  = "It is him"
        if len(fname) < 7 or len(lname) < 7:
            answer = invalid
        elif fname[0] != "B" or lname[0] != "C":
            answer = invalid
        else:
            if not self.matches(fname, "BENEDICT", 3) or not self.matches(lname,"CUMBERBATCH", 5):
                answer = invalid
        return answer





print(Sherlock().isItHim("BUMBLESHACK", "CRUMPLEHORN"))



