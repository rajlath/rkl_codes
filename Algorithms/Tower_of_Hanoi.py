moves = 0
def tower_of_hanoi(number_of_disks, start_peg = 1, endpeg=3):
    global moves
    if number_of_disks:
        moves +=1
        tower_of_hanoi(number_of_disks - 1, start_peg, 6 - start_peg - endpeg)
        print("Move disk {} from peg {} to peg {}".format(number_of_disks, start_peg, endpeg))
        tower_of_hanoi(number_of_disks - 1, 6 - start_peg - endpeg, endpeg)


tower_of_hanoi(4)
print(moves)
