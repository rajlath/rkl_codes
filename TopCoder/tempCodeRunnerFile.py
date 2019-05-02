class FightMonsterDiv2():
    def damageDealt(self, attack, level, duration):
        power = (attack * level) // 100
        demage   = attack
        for i in range(duration):
            demage += power
        return demage


print(FightMonsterDiv2().damageDealt(100,10,3))


