import sys

def get_input_output_object():
    args = sys.argv

    if len(args) >= 2:
        file_ins = open(sys.argv[1], "r")
        file_out = open(sys.argv[2], "w")
        return (file_ins, file_out)
    else:
        return (None, None)
def get_line(fobj):
    return fobj.readline().strip()

ins, out = get_input_output_object()
if ins is not None:
    test_nb = 1
    nb_test = int(get_line(ins))
    for _ in range(nb_test):
        nb_cards = int(get_line(ins))
        cards = []
        counts = 0
        for i in range(nb_cards):
            cards.append(get_line(ins))
        for i in range(1, nb_cards):
            if cards[i] < cards[i - 1]:
                j = i
                while j > 0:
                    if cards[j] < cards[j - 1]:
                        cards[j], cards[j - 1] = cards[j - 1], cards[j]
                    else:
                            j -= 1
                counts += 1
ans1 = "Case #{}: {}".format(test_nb,counts)
print(ans1, file = out)
test_nb += 1
else:
    print("Invalid input output File.")