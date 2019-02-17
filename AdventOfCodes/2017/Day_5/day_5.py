def get_lines():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append(line)
    return lines

lines = get_lines()
def do_part1(lines, update = None):
    lines = [int(x) for x in lines]

    i, count = 0, 0
    if update is None:
        update = lambda x: x + 1
    while 0 <= i < len(lines):
        jump = lines[i]
        lines[i] = update(lines[i])
        count += 1
        i += jump
    return count

def do_part2(lines):
    return do_part1(lines, update=lambda x: x + 1 if x < 3 else x - 1)

print(do_part1(lines))
print(do_part2(lines))




