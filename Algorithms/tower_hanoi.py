def tower_of_hanoi(num, src, dst, tmp):
    if num < 1:
        return
    tower_of_hanoi(num-1, src, tmp, dst)
    print("Move {} disk from peg {} to peg {}".format(num, src, dst))
    tower_of_hanoi(num-1, tmp, dst, src)

tower_of_hanoi(4, "A", "B", "C")

