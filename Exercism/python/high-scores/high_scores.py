class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def scores(self):
        return self.scores
    def latest(self):
        return self.scores[-1]
    def personal_best(self):
        return max(self.scores)

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        best = max(self.scores)
        last = self.scores[-1]
        if best > last:
            return "Your latest score was {}. That's {} short of your personal best!".format(last, best - last)
        if best < last:
            return "Your latest score was {}. That's your personal best!".format(last)
        else:
            return "Your latest score was {}. That's your personal best!".format(last)



