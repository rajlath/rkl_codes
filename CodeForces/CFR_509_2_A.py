nb_keyboard = int(input())
keyboard    = [int(x) for x in input().split()]
print((1 + max(keyboard) - min(keyboard) ) - nb_keyboard)
