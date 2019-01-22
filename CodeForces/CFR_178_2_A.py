nb_wires = int(input())
population = [0] + [int(x) for x in input().split()] + [0]
nb_shots = int(input())
for _ in range(nb_shots):
    wire_no, bird_no = [int(x) for x in input().split()]
    population[wire_no-1] += bird_no - 1
    population[wire_no+1] += population[wire_no] - bird_no
    population[wire_no] = 0
for i in range(1, nb_wires+1)    :
    print(population[i])