class Leaderboard:

    def __init__(self):
        self.score_card = dict()

    def addScore(self, playerId: int, score: int) -> None:
        self.score_card[playerId] = self.score_card.get(playerId, 0) + score

    def top(self, K: int) -> int:
        return sum(sorted(self.score_card.values(), reverse=True)[:K])


    def reset(self, playerId: int) -> None:
        self.score_card[playerId] = 0



# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)