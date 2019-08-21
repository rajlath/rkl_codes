class Team(object):
    def __init__(self, names):
        self.names = names

    def __non_zero__(self):
        first = [f[0] for f in self.names]
        last = [f[-1] for f in self.names]
        print(first, last)


def isCoolTeam(team):
    return bool(Team(team))


print(isCoolTeam(["Ron", "Harry"]))
