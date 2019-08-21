def sortCodesignalUsers(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))

class CodeSignalUser(object):
    def __init__(self, *args):
        self.uname = args[0]
        self.id    = args[1]
        self.xp    = args[2]
    def __str__(self):
        return self.user

    def __str__(self):
        return self.uname

    def __lt__(self, o):
        return (self.xp, o.id) < (o.xp, self.id)

users = [["warrior", "1", "1050"],["Ninja!",  "21", "995"],["recruit", "3","995"]]
