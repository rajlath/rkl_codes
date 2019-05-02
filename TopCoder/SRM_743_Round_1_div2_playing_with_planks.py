class PlayingWithPlanks(object):
    def canItBeDone(self, plankLength, pieces):
        should_be  = (pieces * (pieces + 1)) // 2
        if plankLength < should_be:
            return "impossible"
        else:
            return "possible"


print(PlayingWithPlanks().canItBeDone(9, 4))
