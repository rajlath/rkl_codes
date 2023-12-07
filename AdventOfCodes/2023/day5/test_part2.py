import sys
from dataclasses import *
from multiprocessing import *

global maps
@dataclass
class Range:
    start: int
    length: int

    def contains(self, value: int) -> bool:
        return self.start <= value < self.start + self.length

def check(loc: int) -> int | None:
    global seed_ranges
    global maps

    value = loc

    for m in maps:
        for trg_range, src_start in m:
            if trg_range.contains(value):
                value = src_start + (value - trg_range.start)
                break

    return loc if any(r.contains(value) for r in seed_ranges) else None

def main():
    global seed_ranges
    

    #data = sys.stdin.read().strip()
    with open("input.txt") as f:
        data = f.read()

#     raw_seeds = list(map(int, data.split("\n")[0].split(": ")[1].split(" ")))
#     seed_ranges = []
#     for i in range(0, len(raw_seeds), 2):
#         seed_ranges.append(Range(raw_seeds[i], raw_seeds[i + 1]))

#     maps = []

#     for sec in data.split("\n\n")[1:]:
#         lines = sec.split("\n")

#         m = []
#         for line in lines[1:]:
#             trg_start, src_start, length = map(int, line.split(" "))
#             m.append((Range(trg_start, length), src_start))

#         maps.append(m)

#     maps = maps[::-1]

#     with Pool(15) as pool:
#         for loc in pool.imap(check, range(int(1e9)), int(1e6)):
#             if loc is not None:
#                 print(loc)
#                 return

# if __name__ == "__main__":
#     main()
    seeds = [*map(int, data[0].split(": ")[1].split())]
    maps = [[[*map(int, n.split())] for n in i.split("\n")[1:]] for i in "\n".join(data[2:]).split("\n\n")]

    location = 0
    seed_pairs = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

    while True:
        result = location
        for _map in maps[::-1]:
            for dest, src, rng in _map:
                if dest <= result < dest + rng:
                    idx = result - dest
                    result = src + idx
                    break
                if any(pair[0] <= result <= pair[1] for pair in seed_pairs):
                    return location
                    break
            location += 1
print(main())        