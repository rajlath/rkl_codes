from collections import defaultdict
class LongJumpCompetition():
    def recoverStandings(self, jumps):
        max_jumps = defaultdict(list)
        i = 0
        p = 0
        while i < len(jumps):
            curr = max(jumps[i : i + 3])
            max_jumps[curr].append(p)
            i += 3
            p += 1
        max_jump_all = max(max_jumps.keys())
        return sorted(max_jumps[max_jump_all])[0]



print(LongJumpCompetition().recoverStandings([100, 120, 110, 130, 120, 111, 147, 92, 0]))