class FightMonsterDiv2():
    def damageDealt(self, attack, level, duration):
        power = (attack * level) // 100
        demage   = 0
        current  = attack
        for i in range(duration):
            demage += current
            current += power
        return demage


print(FightMonsterDiv2().damageDealt(100000,100,100000))


